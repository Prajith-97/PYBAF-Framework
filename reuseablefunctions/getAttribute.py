from reuseablefunctions.locator import Locator
from reuseablefunctions.reporting import Reporting


class ReadAttribute(Locator):

    objReporting = Reporting()

    def __init__(self):
        super().__init__()
        self.attributeValue = None

    def getAttribute(self, driver, locator_path, locator_name, attributeName):
        try:
            self.selectLocator(driver, locator_path, locator_name)
            self.attributeValue = self.webelement.get_attribute(attributeName)
            return self.attributeValue
        except Exception as e:
            raise Exception(e)

