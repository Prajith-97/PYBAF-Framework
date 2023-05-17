from reuseablefunctions.reporting import Reporting


class Alert:
    objReporting = Reporting()

    def accept(self, driver):
        try:
            driver.switch_to.alert.accept()
            reportMessage = "Accepted the alert"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def dismiss(self, driver):
        try:
            driver.switch_to.alert.dismiss()
            reportMessage = "Dismissed the alert"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def sendkeys(self, driver, text):
        try:
            driver.switch_to.alert.send_keys(text)
            reportMessage = "Text is send to alert"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def selectAlert(self, driver, actionOnAlert, text=None):
        try:
            match actionOnAlert.upper():
                case 'ACCEPT':
                    self.accept(driver)
                case 'DISMISS':
                    self.dismiss(driver)
                case 'SENDKEYS':
                    self.sendkeys(driver, text)
        except Exception as e:
            raise Exception(e)
