from reuseablefunctions.reporting import Reporting


class Handle:
    objReporting = Reporting()

    def windowHandle(self, driver):
        try:
            handles = driver.window_handles
            for handle in handles:
                driver.switch_to.window(handle)
            reportMessage = "Moved to another tab"
            self.objReporting.writeLog(reportMessage, None)
        except Exception as e:
            raise Exception(e)


