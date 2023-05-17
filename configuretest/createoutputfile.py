import json
import os
from copy import copy, deepcopy
from reuseablefunctions.reporting import Reporting


class createJson:
    objReport = Reporting()
    # --------
    list = []
    dict = {}

    # -----------------
    listFeatures = []
    dictFeatures = {}

    # ------------------
    listFeature = []
    dictFeature = {}

    # ------------------
    listScenarios = []
    dictScenarios = {}

    # ------------------
    listSteps = []
    dictSteps = {}
    # --------------------
    dictScenario = {}

    # ----------
    dictStep = {}
    dictsteps = {}

    current_directory = os.getcwd()
    Dir = os.path.abspath(os.path.join(current_directory, ".."))

    # creates or open json when execution starts
    def Json(self):
        try:
            with open(self.Dir + "\\" + "output.json", 'w') as f:
                pass
        except Exception as e:
            self.objReport.writeLog("Not able to create or open json", e)

    def structureJson(self):
        try:
            with open(self.Dir + "\\" + "output.json", 'a') as f:
                json.dump(self.list, f, indent=2)
        except Exception as e:
            self.objReport.writeLog("Failed to dump value to json", e)

    def clear_step(self):
        try:
            self.dictStep.clear()
        except Exception as e:
            self.objReport.writeLog("Failed to clear previous step", e)

    def clear_scenario(self):
        try:
            self.listSteps.clear()
        except Exception as e:
            self.objReport.writeLog("Failed to clear previous scenario", e)

    def clear_feature(self):
        try:
            self.listScenarios.clear()
            self.listFeature.clear()
            self.listFeatures.clear()
            self.dictFeature.clear()
            self.dict.clear()
        except Exception as e:
            self.objReport.writeLog("Failed to clear previous feature", e)

    def append(self, key, value, dictName):
        try:
            if dictName == "feature":
                self.dictFeature[key] = value
            if dictName == "scenario":
                self.dictScenario[key] = value
            if dictName == "step":
                self.dictStep[key] = value
            if dictName == "scenarios":
                self.dictScenarios[key] = value
        except Exception as e:
            self.objReport.writeLog("Failed to append value to dictionary", e)

    def dict_step(self):
        try:
            self.dictSteps["step"] = self.dictStep
            self.listSteps.append(deepcopy(self.dictSteps))
        except Exception as e:
            self.objReport.writeLog("Failed to append value to list steps", e)

    def dict_scenario(self):
        try:
            self.dictScenario["steps"] = self.listSteps
            self.dictScenarios["scenario"] = self.dictScenario
            self.listScenarios.append(deepcopy(self.dictScenarios))
        except Exception as e:
            self.objReport.writeLog("Failed to append value to list scenarios", e)

    def dict_feature(self, featurename, platform):
        try:
            if len(self.list) == 0 or not any(d['name'] == featurename for d in self.list) and (
            d['paltform'] == platform
            for d in self.listFeature):
                self.dict['name'] = featurename
                self.dictFeature["scenarios"] = self.listScenarios
                self.listFeature.append(self.dictFeature)
                self.dictFeatures["feature"] = self.listFeature
                self.listFeatures.append(self.dictFeatures)
                self.dict["features"] = self.listFeatures
                self.list.append(deepcopy(self.dict))
            else:
                for d in self.list:
                    if d['name'] == featurename and (dic['paltform'] == platform for dic in self.listFeature):
                        self.dict['name'] = featurename
                        self.listFeatures = d['features']
                        self.list.remove(d)
                        self.dictFeature["scenarios"] = self.listScenarios
                        self.listFeature.append(self.dictFeature)
                        self.dictFeatures["feature"] = self.listFeature
                        self.listFeatures.append(self.dictFeatures)
                        self.dict["features"] = self.listFeatures
                        self.list.append(deepcopy(self.dict))
                        break
        except Exception as e:
            self.objReport.writeLog("Failed to append value to list features", e)
