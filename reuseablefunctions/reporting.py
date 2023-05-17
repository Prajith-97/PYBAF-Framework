import logging
import time
import os
from configuretest.ReadTestData import ReadTestData
from configuretest.createfolder import Createfolder
from PIL import ImageGrab


class Reporting:
    readData = ReadTestData()
    objfolder = Createfolder()

    # add screenshot status in testdata.json file on configureTest directory
    screenshotStatus = readData.getTestData("Reports", "Screenshot")

    def __init__(self):
        super().__init__()
        self.path = None
        self.logger = None

    def capture_screenshot(self, driver):
        try:
            Time = time.strftime(" %H%M%S", time.localtime())
            foldername = os.path.basename(os.path.dirname(self.objfolder.Dir + "\\" + self.objfolder.Reportfolder + "\\" + self.objfolder.Datefolder + "\\" + self.objfolder.Date_Time_folder + "\\" + self.objfolder.Screenshot_folder))
            driver.get_screenshot_as_file(self.objfolder.Dir + "\\" + self.objfolder.Reportfolder + "\\" + self.objfolder.Datefolder + "\\" + foldername + "\\" + self.objfolder.Screenshot_folder + "\\" + Time + ".png")
            self.path = os.path.abspath(self.objfolder.Dir + "\\" + self.objfolder.Reportfolder + "\\" + self.objfolder.Datefolder + "\\" + foldername + "\\" + self.objfolder.Screenshot_folder + "\\" + Time + ".png")
            return self.path
        except Exception:
            screenshot = ImageGrab.grab()
            screenshot.save(self.objfolder.Dir + "\\" + self.objfolder.Reportfolder + "\\" + self.objfolder.Datefolder + "\\" + foldername + "\\" + self.objfolder.Screenshot_folder + "\\" + Time + ".png")
            self.path = os.path.abspath(self.objfolder.Dir + "\\" + self.objfolder.Reportfolder + "\\" + self.objfolder.Datefolder + "\\" + foldername + "\\" + self.objfolder.Screenshot_folder + "\\" + Time + ".png")
            return self.path

    def writeLog(self, ReportMessage, e):
        try:
            foldername = os.path.basename(os.path.dirname(
                self.objfolder.Dir + "\\" + self.objfolder.Reportfolder + "\\" + self.objfolder.Datefolder + "\\" + self.objfolder.Date_Time_folder + "\\" + self.objfolder.Screenshot_folder))
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            fh = logging.FileHandler(
                self.objfolder.Dir + "\\" + self.objfolder.Reportfolder + "\\" + self.objfolder.Datefolder + "\\" + foldername + "\\""Log.log")
            f = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            fh.setFormatter(f)
            self.logger.addHandler(fh)
            self.logger.info(ReportMessage, exc_info=e)
            self.logger.removeHandler(fh)
        except:
            print("Not able to log message")

    def screenshot(self, driver, stepStatus):
        try:
            if self.screenshotStatus.upper() == "ALL":
                self.capture_screenshot(driver)
            elif self.screenshotStatus.upper() == "FAIL" and stepStatus.upper() == "FAILED":
                self.capture_screenshot(driver)
            elif self.screenshotStatus.upper() == "FAIL" and stepStatus.upper() == "PASSED":
                self.path = ""
                return self.path
        except:
            pass
