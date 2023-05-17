import os
from xml.dom import minidom
from behave import __main__ as behave_executable
from configuretest.ReadTestData import ReadTestData
from reuseablefunctions.reporting import Reporting

project_root = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(project_root, 'configuretest\systemproperties.xml')
file = minidom.parse(path)

browsers = file.getElementsByTagName('browser')
length = len(browsers)
objreport = Reporting()


class BehaveRunner:
    def __init__(self, args):
        self.args = args

    def runTests(self, i):
        try:
            r = ReadTestData()
            journeyPath = r.getTestData("Journey", "path")
            os.environ['MY_PARAM'] = str(i)
            # Pass the behave arguments to the behave executable
            return behave_executable.main(journeyPath)
        except Exception as e:
            objreport.writeLog("Run test method is not executed", e)


if __name__ == "__main__":
    try:
        for i in range(length):
            if browsers[i].childNodes[0].data == "True":
                runner = BehaveRunner(["behave"])
                runner.runTests(i)
    except Exception as e:
        objreport.writeLog("Run test method is not executed", e)
