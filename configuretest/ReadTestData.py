import json
import os


class ReadTestData:
    def getTestData(self,arrayName,keyValue):
        try:
            project_root = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(project_root, 'configuretest\TestData.json')
            f = open(path)
            data = json.load(f)
            jsonData = data[arrayName]
            for x in jsonData:
                dataValue=x[keyValue]
                return dataValue
            f.close()
        except Exception as e:
            raise Exception(e)


