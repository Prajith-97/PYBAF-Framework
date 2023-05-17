from selenium.webdriver import ActionChains
from reuseablefunctions.locator import Locator
from reuseablefunctions.reporting import Reporting


class Action(Locator):
    objReporting = Reporting()

    def sendkeys(self, driver, locator_path, locator_name, variable):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            self.webelement.send_keys(variable)
            reportMessage = "Entered text to the field"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def clear(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            self.webelement.clear()
            reportMessage = "Cleared the text"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def click(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            self.webelement.click()
            reportMessage = "Clicked on the element"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def doubleclick(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            action = ActionChains(driver)
            action.double_click(self.webelement).perform()
            reportMessage = "Double clicked on the element"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def moveToElement(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            action = ActionChains(driver)
            action.move_to_element(self.webelement).perform()
            reportMessage = "Cursor is moved to particular element"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def contextClick(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            action = ActionChains(driver)
            action.context_click(self.webelement).perform()
            reportMessage = "Performed context click on particular element"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def selectActions(self, driver, loc_path, loc_name, actionName, textVar=None):
        try:
            match actionName.upper():
                case 'SENDKEYS':
                    self.sendkeys(driver, loc_path, loc_name, textVar)
                case 'CLEAR':
                    self.clear(driver, loc_path, loc_name)
                case 'CLICK':
                    self.click(driver, loc_path, loc_name)
                case 'DOUBLECLICK':
                    self.doubleclick(driver, loc_path, loc_name)
                case 'MOVETOELEMENT':
                    self.moveToElement(driver, loc_path, loc_name)
                case 'CONTEXTCLICK':
                    self.contextClick(driver, loc_path, loc_name)
                case _:
                    print("Not found")
        except Exception as e:
            raise Exception(e)
