import datetime
import os
from behave.model import StepControl
from behave import fixture
from behave import use_fixture
from configuretest.createfolder import Createfolder
from configuretest.createoutputfile import createJson
from configuretest.webdriver_manager import WebDriverManagerInstance
from reuseablefunctions.reporting import Reporting
from tests.test_forgotyourpassword import Test_forgotpassword
from tests.test_homepage import Test_homepage
from reuseablefunctions.teardown import Teardown
import time

objJson = createJson()
objreport = Reporting()


@fixture
def oneTimeSetup(context):
    # create report folder
    try:
        obj = Createfolder()
        obj.folder()
    except:
        print("Folder Exists")


@fixture
def getDriver(context):
    my_param = int(os.environ.get('MY_PARAM'))
    objDriver = WebDriverManagerInstance()
    context.driver = objDriver.LaunchBrowser(my_param)
    yield
    objTeardown = Teardown()
    objTeardown.teardown(context.driver, "close")


@fixture
def stepDetails(context):
    stepName = context.step.name
    if hasattr(context, "exception"):
        reportMsg = "Step failed, An exception occurred in step:" + stepName
        context.status = "Failed"
        objreport.writeLog(reportMsg, context.exception)
        objreport.screenshot(context.driver, context.status)
        objJson.append("screenshot", objreport.path, "step")
        objJson.append("status", context.status, "step")
        objJson.append("errorMsg", str(context.exception), "step")
        del context.exception
    else:
        reportMsg = "Step passed:" + stepName
        context.status = "Passed"
        objreport.writeLog(reportMsg, None)
        objreport.screenshot(context.driver, context.status)
        objJson.append("screenshot", objreport.path, "step")
        objJson.append("status", context.status, "step")
        objJson.append("errorMsg", "", "step")


@fixture
def time(context):
    # current_time = str(datetime.datetime.now())
    t = datetime.datetime.now()
    current_time = t.strftime("%Y-%m-%d %H:%M:%S")
    return current_time


@fixture
def scenarioStatus(context):
    if not any(d['step']['status'] == 'Failed' or d['step']['status'] == 'Skipped' for d in objJson.listSteps):
        objJson.append("status", "PASSED", "scenario")
    elif all(d['step']['status'] == 'Skipped' for d in objJson.listSteps):
        objJson.append("status", "SKIPPED", "scenario")
    else:
        objJson.append("status", "FAILED", "scenario")


@fixture
def featureStatus(context):
    if not any(d['scenario']['status'] == 'FAILED' for d in objJson.listScenarios):
        objJson.append("FeatureStatus", "PASSED", "feature")
    else:
        objJson.append("FeatureStatus", "FAILED", "feature")


def before_all(context):
    try:
        use_fixture(oneTimeSetup, context)
        objJson.Json()
    except Exception as e:
        objreport.writeLog("Not executed before all", e)


def after_all(context):
    try:
        objJson.structureJson()
    except Exception as e:
        objreport.writeLog("Not executed after all", e)


def before_feature(context, feature):
    try:
        objJson.clear_feature()
        use_fixture(getDriver, context)
        current_time = use_fixture(time, context)
        featureName = context.feature.name
        description = context.feature.description[0]
        objJson.append("name", featureName, "feature")
        objJson.append("description", description, "feature")
        objJson.append("starttime", current_time, "feature")
    except Exception as e:
        objreport.writeLog("Not executed before feature", e)


def after_feature(context, feature):
        featureName = context.feature.name
        platform = (objJson.dictFeature.get('platform'))
        current_time = use_fixture(time, context)
        objJson.append("endtime", current_time, "feature")
        use_fixture(featureStatus, context)
        objJson.dict_feature(featureName, 'platform')


def before_scenario(context, scenario):
        objJson.clear_scenario()
        scenarioName = context.scenario.name
        objJson.append("name", scenarioName, "scenario")
        objJson.append("severity", "", "scenario")
        tg = []
        t = scenario.tags
        for i in range(len(t)):
            tag = scenario.tags[i]
            tg.append(str(tag))
            objJson.append("tags", tg, "scenario")
        if any(d['scenario']['status'] == 'FAILED' for d in objJson.listScenarios):
            raise StepControl(skip=True)

        # objects, passing driver instance to the classes
        context.objLink = Test_homepage(context.driver)
        context.objForgotPassword = Test_forgotpassword(context.driver)


def after_scenario(context, scenario):
        duration = context.scenario.duration
        t = duration * 1000
        time = int(round(t, 0))
        objJson.append("duration", time, "scenario")
        if not any(d['scenario']['status'] == 'FAILED' for d in objJson.listScenarios):
            use_fixture(scenarioStatus, context)
            objJson.dict_scenario()
        else:
            for scenario_step in context.scenario.steps:
                objJson.clear_step()
                if scenario_step.status == 'untested':
                    objJson.append("name", scenario_step.name, "step")
                    objJson.append("screenshot", "", "step")
                    objJson.append("status", "Skipped", "step")
                    objJson.append("errorMsg", "", "step")
                    objJson.dict_step()
            use_fixture(scenarioStatus, context)
            objJson.dict_scenario()


def before_step(context, step):
        context.step = step
        objJson.clear_step()
        stepName = context.step.name
        objJson.append("name", stepName, "step")


def after_step(context, step):
        use_fixture(stepDetails, context)
        objJson.dict_step()
        if context.status == "Failed":
            for scenario_step in context.scenario.steps:
                objJson.clear_step()
                if scenario_step.status == 'untested':
                    objJson.append("name", scenario_step.name, "step")
                    objJson.append("screenshot", "", "step")
                    objJson.append("status", "Skipped", "step")
                    objJson.append("errorMsg", "", "step")
                    objJson.dict_step()
            raise StepControl(skip=True)


