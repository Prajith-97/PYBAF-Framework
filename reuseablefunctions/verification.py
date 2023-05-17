from reuseablefunctions.getAttribute import ReadAttribute
from reuseablefunctions.reporting import Reporting


class Verification(ReadAttribute):
    objReporting = Reporting()

    def equalsTo(self, driver, locator_path, locator_name, propertyType, expectedValue):
        try:
            self.getAttribute(driver, locator_path, locator_name, propertyType)
            assert self.attributeValue == expectedValue
            reportMessage = "Assertion Passed, Actual value equals to Expected value"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def contains(self, driver, locator_path, locator_name, propertyType, expectedValue):
        try:
            self.getAttribute(driver, locator_path, locator_name, propertyType)
            assert self.attributeValue in expectedValue
            reportMessage = "Assertion Passed, Actual value contains Expected value"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def greaterThanOrEqualTo(self, driver, locator_path, locator_name, propertyType, expectedValue):
        try:
            self.getAttribute(driver, locator_path, locator_name, propertyType)
            assert self.attributeValue >= expectedValue
            reportMessage = "Assertion Passed, Actual value is greater than or equals to Expected value"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def lessThanOrEqualTo(self, driver, locator_path, locator_name, propertyType, expectedValue):
        try:
            self.getAttribute(driver, locator_path, locator_name, propertyType)
            assert self.attributeValue <= expectedValue
            reportMessage = "Assertion Passed, Actual value is less than or equals to Expected value"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def enabled(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            self.webelement.is_enabled()
            reportMessage = "Assertion Passed, Element is enabled"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def disabled(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            isDisabled = not self.webelement.is_enabled()
            assert isDisabled, "Element disabled"
            reportMessage = "Assertion Passed, Element is disabled"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def displayed(self, driver, locator_path, locator_name):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            self.webelement.is_displayed()
            reportMessage = "Assertion Passed, Element is displayed"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def verifyObjectProperty(self, driver, loc_path, loc_name, validationType, propType=None, expectedValue=None):
        try:
            match validationType.upper():
                case 'EQUALS':
                    self.equalsTo(driver, loc_path, loc_name, propType, expectedValue)
                case 'CONTAINS':
                    self.contains(driver, loc_path, loc_name, propType, expectedValue)
                case 'GREATERTHANOREQUALTO':
                    self.greaterThanOrEqualTo(driver, loc_path, loc_name, propType, expectedValue)
                case 'LESSTHANOREQUALTO':
                    self.lessThanOrEqualTo(driver, loc_path, loc_name, propType, expectedValue)
                case 'ENABLED':
                    self.enabled(driver, loc_path, loc_name)
                case 'DISABLED':
                    self.disabled(driver, loc_path, loc_name)
                case 'DISPLAYED':
                    self.displayed(driver, loc_path, loc_name)
        except Exception as e:
            raise Exception(e)
