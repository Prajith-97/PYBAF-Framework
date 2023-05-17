from reuseablefunctions.reporting import Reporting


class Teardown:
    objReporting = Reporting()

    def closeBrowser(self, driver):
        try:
            driver.close()
            reportMessage = "Browser closed"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def quitBrowser(self, driver):
        try:
            driver.quit()
            reportMessage = "Quit Browser"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def teardown(self, driver, teardownType):
        try:
            match teardownType.upper():
                case 'CLOSE':
                    self.closeBrowser(driver)
                case 'QUIT':
                    self.quitBrowser(driver)
        except Exception as e:
            raise Exception(e)
