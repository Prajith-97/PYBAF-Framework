import pytest
from configuretest.webdriver_manager import WebDriverManagerInstance
from reuseablefunctions.teardown import Teardown
from configuretest.createfolder import Createfolder


# @pytest.fixture(scope="session", autouse=True)
# def oneTimeSetup():
#     obj = Createfolder()
#     obj.folder()

# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture
def getDriver(request):
    _driver = None  # _driver means which is specific to this method, not a global variable
    objDriver = WebDriverManagerInstance()
    _driver = objDriver.LaunchBrowser()
    request.cls.driver = _driver  # request cls is used to make this variable as a class level variable. so any class which is using this fixture can use the driver object
    yield request.cls.driver
    objTeardown = Teardown()
    objTeardown.teardown(_driver, "close")
