from reuseablefunctions.reporting import Reporting


class Frames:
    objReporting = Reporting()

    def switchToFrame(self, driver, frameName):
        try:
            driver.switch_to.frame(frameName)
            reportMessage = "Switched to particular frame"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def defaultContent(self, driver):
        try:
            driver.switch_to.default_content()
            reportMessage = "Switched to default content"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)

    def selectFrame(self, driver, frameType, frameName=None):
        try:
            match frameType.upper():
                case 'SWITCHTOFRAME':
                    self.switchToFrame(driver, frameName)
                case 'DEAFULTCONTENT':
                    self.defaultContent(driver)
        except Exception as e:
            raise Exception(e)
