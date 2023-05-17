import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from configuretest.ReadTestData import ReadTestData
from configuretest.createoutputfile import createJson
from xml.dom import minidom


class WebDriverManagerInstance:
    objJson = createJson()

    def LaunchBrowser(self, n):
        global driver
        try:
            project_root = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(project_root, 'configuretest\systemproperties.xml')
            file = minidom.parse(path)
            # use getElementsByTagName() to get tag
            browsers = file.getElementsByTagName('browser')
            # one specific item attribute
            BROWSER_STATUS = (browsers[n].childNodes[0].data)
            BROWSER_NAME = (browsers[n].attributes['name'].value)
            r = ReadTestData()
            URL = r.getTestData("URL", "url")
            if BROWSER_NAME.upper() == "CHROME" and BROWSER_STATUS.upper() == "TRUE":
                self.objJson.append("platform", BROWSER_NAME, "feature")
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get(URL)
                driver.maximize_window()

            elif BROWSER_NAME.upper() == "FIREFOX" and BROWSER_STATUS.upper() == "TRUE":
                self.objJson.append("platform", BROWSER_NAME, "feature")
                driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
                driver.get(URL)
                driver.maximize_window()

            elif BROWSER_NAME.upper() == "EDGE" and BROWSER_STATUS.upper() == "TRUE":
                self.objJson.append("platform", BROWSER_NAME, "feature")
                driver = webdriver.Edge(EdgeChromiumDriverManager().install())
                driver.get(URL)
                driver.maximize_window()
            return driver
        except Exception as e:
            raise Exception(e)


