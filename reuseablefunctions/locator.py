from selenium.webdriver.common.by import By
from reuseablefunctions.reporting import Reporting


class Locator:
    objReporting = Reporting()

    def __init__(self):
        self.webelement = None

    def xpath(self, driver, locator_path):
        try:
            self.webelement = driver.find_element(By.XPATH, locator_path)
            reportMessage = "Located element using xpath"
            self.objReporting.writeLog(reportMessage, None)
            return self.webelement
        except Exception as e:
            raise Exception(e)

    def id(self, driver, locator_path):
        try:
            self.webelement = driver.find_element_by_id(locator_path)
            reportMessage = "Located element using id"
            self.objReporting.writeLog(reportMessage, None)
            return self.webelement
        except Exception as e:
            raise Exception(e)

    def className(self, driver, locator_path):
        try:
            self.webelement = driver.find_element_by_class_name(locator_path)
            reportMessage = "Located element using class"
            self.objReporting.writeLog(reportMessage, None)
            return self.webelement
        except Exception as e:
            raise Exception(e)

    def css(self, driver, locator_path):
        try:
            self.webelement = driver.find_element_by_css_selector(locator_path)
            reportMessage = "Located element using css"
            self.objReporting.writeLog(reportMessage, None)
            return self.webelement
        except Exception as e:
            raise Exception(e)

    def linkText(self, driver, locator_path):
        try:
            self.webelement = driver.find_element(By.LINK_TEXT, locator_path)
            reportMessage = "Located element using link text"
            self.objReporting.writeLog(reportMessage, None)
            return self.webelement
        except Exception as e:
            raise Exception(e)

    def partialLinkText(self, driver, locator_path):
        try:
            self.webelement = driver.find_element_by_partial_link_text(locator_path)
            reportMessage = "Located element using partial link text"
            self.objReporting.writeLog(reportMessage, None)
            return self.webelement
        except Exception as e:
            raise Exception(e)

    def name(self, driver, locator_path):
        try:
            self.webelement = driver.find_element_by_name(locator_path)
            reportMessage = "Locate element using name"
            self.objReporting.writeLog(reportMessage, None)
            return self.webelement
        except Exception as e:
            raise Exception(e)

    def tagName(self, driver, locator_path):
        try:
            self.webelement = driver.find_element_by_tag_name(locator_path)
            reportMessage = "Not able to locate element using tag"
            self.objReporting.writeLog(reportMessage, None)
            return self.webelement
        except Exception as e:
            raise Exception(e)

    def selectLocator(self, driver, locator_path, locator_name):
        try:
            match locator_name.upper():
                case 'XPATH':
                    self.xpath(driver, locator_path)
                case 'ID':
                    self.id(driver, locator_path)
                case 'CLASSNAME':
                    self.className(driver, locator_path)
                case 'CSS':
                    self.css(driver, locator_path)
                case 'LINKTEXT':
                    self.linkText(driver, locator_path)
                case 'PARTIALLINKTEXT':
                    self.partialLinkText(driver, locator_path)
                case 'NAME':
                    self.name(driver, locator_path)
                case 'TAGNAME':
                    self.tagName(driver, locator_path)
        except Exception as e:
            raise Exception(e)
