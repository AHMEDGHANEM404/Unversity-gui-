import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
MainUi,_=loadUiType('design.ui')
class Home(QMainWindow,MainUi):
    def __init__(self,parent=None):
        super(Home,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon/logo.png"))
        self.setWindowTitle("الازهر")
        #connectDb#################
        # self.Db_connect()
        # clicking #################
        # هنا هشوف لو اليوزر ادمن ولا مسجلش لو مسجلش هيتفتح ليه تسجيل الدخول فقط فقط 
        # if user-> is_super == اعرض كل حاجه 
        # مسجلش يبقي ميتعرض ليه حاجه خالص غير انه يستعلم 
        self.BlockTabs()
        self.openLogin()
        self.tabsInfo()
        self.LoginLogo()
        self.LoginBtn()
        # self.studentTab()
        # self.tabsprint()
        # self.tabsEditing()
        # self.tabsReports()
    def Ui_changes(self):
        # self.tabs.setTabVisible(1,False)
        pass
        # self.tabs.studentsBar(2).setVisibale(False)
        # self.tabs.studentsBar(3).setVisibale(False)
    def BlockTabs(self):
        self.tabs.setTabVisible(1,False)
        self.tabs.setTabVisible(2,False)
        self.tabs.setTabVisible(3,False)
        self.tabs.setTabVisible(4,False)
        self.tabs.setTabVisible(5,False)
        # self.tabs.setTabVisible(6,False)
        self.student.setVisible(False)
        self.student.setVisible(False)
        self.PrintingBtn.setVisible(False)
        self.Editing.setVisible(False)
        # Reports
        self.Reports.setVisible(False)







    


    def Db_connect():
        pass
    def HandelButn(self):
        pass
    def Handel_Login(self):
        pass
    def Handel_password(self):
        pass
    def veiws(self):
        # show all student in any grad 
        pass
    # ##################################################################
    def studentsBarhow(self):
        pass
    def showAllGrads(self):
        pass
    def showAllFaculty(self):
        pass
    def showAllSubjects(self):
        pass
    # ####################################################################
    # 
    # buttons
    def LoginLogo(self):
        self.info_2.clicked.connect(self.openLogo)

    def LoginBtn(self):
        self.log.clicked.connect(self.openLogin)
    def studentTab(self):
        self.student.clicked.connect(self.openStudent)
        # دي كمان هتتغير لما اربط اليوزر
        self.studenttabs.setCurrentIndex(0)
    def tabsprint(self):
        self.PrintingBtn.clicked.connect(self.openPrintPage)
    def tabsInfo(self):
        self.info.clicked.connect(self.OpeninfoBtn)
        # Editing
    def tabsEditing(self):
        self.Editing.clicked.connect(self.OpenEditingPage)
    # Reports
    def tabsReports(self):
        self.Reports.clicked.connect(self.OpenReportsPage)


    #  
    # 
    # pages && buttons 
    def openLogin(self):
        self.tabs.setCurrentIndex(0)
        print("login page")


    def openStudent(self):
        self.tabs.setCurrentIndex(1)
        self.studenttabs.setCurrentIndex(0)

        print("student page")
        # student tabs
    def openPrintPage(self):
        self.tabs.setCurrentIndex(2)
        print("print page")
    # OpenEditingPage
    def OpenEditingPage(self):
        self.tabs.setCurrentIndex(4)
        print("Info page")
    # Reports
    def OpenReportsPage(self):
        self.tabs.setCurrentIndex(5)
        print("Info page")
    # info
    def openLogo(self):
        self.tabs.setCurrentIndex(6)
        print("login page")
    def OpeninfoBtn(self):
        self.tabs.setCurrentIndex(6)
        print("Info page")

# ===================================================================#
# Login Page




# # ===================================================================#
# Reports page 
# 





# # ===================================================================#
# Printing page









# # ===================================================================#
# StaticsPage










# # ===================================================================#
# Editing Page




# # ===================================================================#
# about 




# ===================================================================#






def main():
    app=QApplication(sys.argv)
    window=Home()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()
