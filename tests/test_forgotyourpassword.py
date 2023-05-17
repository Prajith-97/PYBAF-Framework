from configuretest.ReadTestData import ReadTestData
from configuretest.createoutputfile import createJson
from pageobjects.forgotyourpassword import forgotyourpassword
from pageobjects.homepage import homepage
from reuseablefunctions.action import Action
from reuseablefunctions.reporting import Reporting


class Test_forgotpassword(Reporting):
    objact = Action()
    objhomepage_path = homepage()
    objforgotpassword_path = forgotyourpassword()
    objJson = createJson()
    r = ReadTestData()

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def click_myAccount(self):
        try:
            self.objact.selectActions(self.driver, self.objforgotpassword_path.myAccountBtn, "xpath", "click", None)
        except Exception as e:
            raise Exception(e)

    def click_login(self):
        try:
            self.objact.selectActions(self.driver, self.objforgotpassword_path.loginBtn, "xpath", "click",None)
        except Exception as e:
            raise Exception(e)

    def enterEmailID(self):
        try:
            username = self.r.getTestData("Credentials", "username")
            self.objact.selectActions(self.driver, self.objforgotpassword_path.emailTextBox_id, "id", "sendkeys", username)
        except Exception as e:
            raise Exception(e)

    def clickBusBtn(self):
        try:
            self.objact.selectActions(self.driver, self.objforgotpassword_path.busBtn, "xpath", "click", None)
        except Exception as e:
            raise Exception(e)

    def clickSearchBusBtn(self):
        try:
            self.objact.selectActions(self.driver, self.objforgotpassword_path.searchBusBtn, "xpath", "click", None)
        except Exception as e:
            raise Exception(e)

    # def bus_SLP(self):
        # try:
            # if self.driver.title == "Yatra.com | Delhi to Jaipur Bus":
            #     status = "Passed"
            #     reportMsg = "Test is passed"
            #     self.screenshot(self.driver, status, True)
            #     self.writeLog(reportMsg, None)
            #     self.objJson.append("screenshot", self.path, "step")
            #     self.objJson.append("status", status, "step")
            #     self.objJson.append("errorMsg", " ", "step")
        # except Exception as e:
        #     status = "Failed"
        #     reportMsg = "Test Failed"
        #     self.write_execution_status(self.driver, status, reportMsg, True, e)
        #     self.objJson.append("screenshot", self.path, "step")
        #     self.objJson.append("status", status, "step")
        #     self.objJson.append("errorMsg", str(e), "step")
