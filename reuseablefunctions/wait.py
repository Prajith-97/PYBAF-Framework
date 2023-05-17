from telnetlib import EC
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from reuseablefunctions.locator import Locator


class Wait(Locator):

    # ...............................................EXPLICIT WAIT.....................................................

    def waitElementClickable(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.element_to_be_clickable(self.webelement)).click()
            reportMessage = "Wait till element was clickable"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitTitleContains(self, driver, text, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            wait.until(EC.title_contains(text))
            reportMessage = "Title contains particular text"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitVisibilityOf(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.visibility_of(self.webelement))
            reportMessage = "Wait till particular element is visible"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitVisibilityOfAllElementsLocated(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.visibility_of_all_elements_located(self.webelement))
            reportMessage = "Wait till VisibilityOfAllElementsLocated"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitElementSelectionState(self, driver, locator_path, locator_name, time, state):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.element_selection_state_to_be(self.webelement, state))
            reportMessage = "ElementSelectionState is working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitPresenceOfElementLocated(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.presence_of_element_located(self.webelement))
            reportMessage = "PresenceOfElementLocated is working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitVisibilityOfElementLocated(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.visibility_of_element_located(self.webelement))
            reportMessage = "VisibilityOfElementLocated is working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitTitleIs(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.title_is(self.webelement))
            reportMessage = "TitleIs working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitInvisibilityOfElementLocated(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.invisibility_of_element_located(self.webelement))
            reportMessage = "InvisibilityOfElementLocated is working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitStalenessOf(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.staleness_of(self.webelement))
            reportMessage = "StalenessOf is working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitUrlContains(self, driver, time, text):
        try:
            wait = WebDriverWait(driver, timeout=time)
            wait.until(EC.url_contains(text))
            reportMessage = "UrlContains working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def waitElementLocatedToBeSelected(self, driver, locator_path, locator_name, time):
        try:
            wait = WebDriverWait(driver, timeout=time)
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.element_located_to_be_selected(self.webelement))
            reportMessage = "ElementLocatedToBeSelected working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    #     .....................................FLUENT WAIT.............................................................
    def fluentWait(self, driver, locator_path, locator_name, time, pollfreequency):
        try:
            wait = WebDriverWait(driver, timeout=time, poll_frequency=pollfreequency,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            self.selectLocator(driver, locator_path, locator_name)
            wait.until(EC.element_to_be_clickable(self.webelement))
            reportMessage = "FluentWait working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    # ......................................IMPLICIT WAIT..............................................................
    def implicitWait(self, driver, time):
        try:
            driver.implicitly_wait(time)
            reportMessage = "ImplicitWait working as excepted"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def addWait(self, driver, waitName, loc_path, loc_name, time, state=None, text=None, pollFrequency=None):
        try:
            match waitName.upper():
                case 'ELEMENTCLICKABLE':
                    self.waitElementClickable(driver, loc_path, loc_name, time)
                case 'TITLECONTAINS':
                    self.waitTitleContains(driver, text, time)
                case 'VISIBILITYOF':
                    self.waitVisibilityOf(driver, loc_path, loc_name, time)
                case 'VISIBILITYOFALLELEMENTSLOCATED':
                    self.waitVisibilityOfAllElementsLocated(driver, loc_path, loc_name, time)
                case 'ELEMENTSELECTIONSTATE':
                    self.waitElementSelectionState(driver, loc_path, loc_name, time, state)
                case 'PRESENCEOFELEMENTLOCATED':
                    self.waitPresenceOfElementLocated(driver, loc_path, loc_name, time)
                case 'VISIBILITYOFELEMENTLOCATED':
                    self.waitVisibilityOfElementLocated(driver, loc_path, loc_name, time)
                case 'TITLEIS':
                    self.waitTitleIs(driver, loc_path, loc_name, time)
                case 'INVISIBILITYOFELEMENTLOCATED':
                    self.waitInvisibilityOfElementLocated(driver, loc_path, loc_name, time)
                case 'STALENESSOF':
                    self.waitStalenessOf(driver, loc_path, loc_name, time)
                case 'URLCONTAINS':
                    self.waitUrlContains(driver, time, text)
                case 'ELEMENTLOCATEDTOBESELECTED':
                    self.waitElementLocatedToBeSelected(driver, loc_path, loc_name, time)
                case 'FLUENTWAIT':
                    self.fluentWait(driver, loc_path, loc_name, time, pollFrequency)
                case 'IMPLICITWAIT':
                    self.implicitWait(driver, time)
        except Exception as e:
            raise Exception(e)
