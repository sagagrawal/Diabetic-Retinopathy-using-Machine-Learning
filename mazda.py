from pywinauto import application, findwindows
import os
import glob
import time

class mazda:
    def __init__(self):
        self.startrun()

    def startrun(self):
        if not os.path.exists("output\\Reports"):
            os.mkdir("output\\Reports")
        images = glob.glob("output\\*.bmp")
        app = application.Application()
        app.Start(r"C:\Sagar_Agrawal\Projects\ML\MaZda 4.6\MaZda.exe")
        time.sleep(5)
        app.MaZda.MenuSelect("File -> Run macro...")
        app.Runmacro.Edit.TypeKeys(r"C:\Sagar_Agrawal\Projects\ML\Codes\macro.txt")
        app.Runmacro.Open.Click()
        time.sleep(300)  # specify time in seconds
        app.Kill_()
