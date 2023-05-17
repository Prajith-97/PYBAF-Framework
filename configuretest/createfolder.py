import datetime
import time
import os


class Createfolder:

    today = datetime.datetime.now()
    Day = today.strftime("%d")
    Month = today.strftime("%m")
    Year = today.strftime("%Y")
    Time = time.strftime(" %H%M%S", time.localtime())
    # get the current working directory
    current_directory = os.getcwd()

    # get the absolute path of the project directory
    Dir = os.path.abspath(os.path.join(current_directory, ".."))
    Reportfolder = "TestReports"
    Datefolder = Day + "-" + Month + "-" + Year
    Date_Time_folder = Day + "-" + Month + "-" + Year + Time
    Screenshot_folder = "Screenshots"

    def __init__(self):
        self.foldername = None

    def folder(self):
        try:
            # print(self.project_directory)
            if os.path.isdir(self.Dir + "\\" + self.Reportfolder) == False:
                os.mkdir(self.Dir+ "\\"+self.Reportfolder)
                os.mkdir(self.Dir+ "\\"+self.Reportfolder + "\\" +self.Datefolder)
                os.mkdir(self.Dir+ "\\"+self.Reportfolder + "\\" + self.Datefolder + "\\" + self.Date_Time_folder)
                os.mkdir(self.Dir+ "\\"+ self.Reportfolder + "\\" + self.Datefolder + "\\" + self.Date_Time_folder + "\\" +self.Screenshot_folder)
            else:
                if os.path.isdir(self.Dir+ "\\"+self.Reportfolder) == True:
                    if os.path.isdir(self.Dir+ "\\"+self.Reportfolder + "\\" +self.Datefolder) == True:
                        print(self.Date_Time_folder)
                        os.mkdir(self.Dir+ "\\"+self.Reportfolder + "\\" + self.Datefolder + "\\" + self.Date_Time_folder)
                        os.mkdir(self.Dir+ "\\"+self.Reportfolder + "\\" + self.Datefolder + "\\" + self.Date_Time_folder + "\\" +self.Screenshot_folder)
                    else:
                        os.mkdir(self.Dir+ "\\"+self.Reportfolder + "\\" +self.Datefolder)
                        os.mkdir(self.Dir+ "\\"+self.Reportfolder + "\\" + self.Datefolder + "\\" + self.Date_Time_folder)
                        os.mkdir(self.Dir+ "\\"+self.Reportfolder + "\\" + self.Datefolder + "\\" + self.Date_Time_folder + "\\" +self.Screenshot_folder)
        except Exception as e:
            raise Exception(e)


