from selenium.webdriver.support.ui import Select
from reuseablefunctions.locator import Locator
from reuseablefunctions.reporting import Reporting


class Dropdown(Locator):
    objReporting = Reporting()

    def selectByVisibleText(self, driver, locator_path, locator_name, text):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            dropdown = Select(self.webelement)
            dropdown.select_by_visible_text(text)
            reportMessage = "Selected element from dropdown using text"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def selectByIndex(self, driver, locator_path, locator_name, index):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            dropdown = Select(self.webelement)
            dropdown.select_by_index(index)
            reportMessage = "Selected element from dropdown using index"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def selectByValue(self, driver, locator_path, locator_name, value):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            dropdown = Select(self.webelement)
            dropdown.select_by_value(value)
            reportMessage = "selected element from dropdown using value"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def selectDropdown(self, driver, selectElementBy, loc_path, loc_name, text=None, index=None, value=None):
        try:
            match selectElementBy.upper():
                case 'TEXT':
                    self.selectByVisibleText(driver, loc_path, loc_name, text)
                case 'INDEX':
                    self.selectByIndex(driver, loc_path, loc_name, index)
                case 'VALUE':
                    self.selectByValue(driver, loc_path, loc_name, value)
        except Exception as e:
            raise Exception(e)
