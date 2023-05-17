from reuseablefunctions.locator import Locator
from reuseablefunctions.reporting import Reporting


class Scroll(Locator):
    objReporting = Reporting()

    def scrollTo(self, driver, pixel):
        try:
            driver.execute_script("window.scrollTo(0," + pixel + ")")
            reportMessage = "Scrolled the window to respective pixel"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def scrollIntoView(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            driver.execute_script("arguments[0].scrollIntoView();", self.webelement)
            reportMessage = "Scrolled to respective webelement"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def scrollBy(self, driver):
        try:
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            reportMessage = "Scrolled to bottom of the window"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def selectScroll(self, driver, scrollType, pixel=None, locator_path=None, locator_name=None):
        try:
            match scrollType.upper():
                case 'SCROLLTO':
                    self.scrollTo(driver, pixel)
                case 'SCROLLINTOVIEW':
                    self.scrollIntoView(driver, locator_path, locator_name)
                case 'SCROLLBY':
                    self.scrollBy(driver)
        except Exception as e:
            raise Exception(e)
