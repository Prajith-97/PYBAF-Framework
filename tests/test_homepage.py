from configuretest.ReadTestData import ReadTestData
from configuretest.createoutputfile import createJson
from pageobjects.forgotyourpassword import forgotyourpassword
from pageobjects.homepage import homepage
from reuseablefunctions.getAttribute import ReadAttribute
from reuseablefunctions.scroll import Scroll
from reuseablefunctions.wait import Wait
from reuseablefunctions.action import Action
from reuseablefunctions.verification import Verification
from reuseablefunctions.frames import Frames
from reuseablefunctions.reporting import Reporting


class Test_homepage(Reporting):
    objact = Action()
    objhomepage_path = homepage()
    objforgotpassword_path = forgotyourpassword()
    objJson = createJson()
    objscroll = Scroll()
    objwait = Wait()
    objattribute = ReadAttribute()
    objVerify = Verification()
    r = ReadTestData()

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def launch_Homepage(self):
        try:
            URL = self.r.getTestData("URL", "url")
            self.driver.get(URL)
            self.objVerify.verifyObjectProperty(self.driver, self.objhomepage_path.holidayBtn, "xpath", "displayed")
        except Exception as e:
            raise Exception(e)

    def click_holidayBtn(self):
        try:
            self.objact.selectActions(self.driver, self.objhomepage_path.holidayBtn, "xpath", "click")
        except Exception as e:
            raise Exception(e)

    def click_searchHolidayBtn(self):
        try:
            self.objact.selectActions(self.driver, self.objhomepage_path.searchHolidayBtn, "xpath", "click")
            self.objwait.addWait(self.driver, "implicitwait", None, None, 30)
        except Exception as e:
            raise Exception(e)

    def holiday_SLP(self):
        try:
            self.objVerify.verifyObjectProperty(self.driver, self.objhomepage_path.slpHeader, "xpath", "displayed")
        except Exception as e:
            raise Exception(e)

    def scrollSLP(self):
        try:
            self.objscroll.selectScroll(self.driver, "SCROLLTO", "50")
        except Exception as e:
            raise Exception(e)

