
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import pyodbc
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QBoxLayout, QLineEdit, QMainWindow, QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from PyQt5.uic import loadUiType
MainUi, _ = loadUiType('untitled.ui')

conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=E:\project\project\filter.accdb;')
cursor = conn.cursor()
cursor.execute(f"SELECT student_id,student_name  FROM student ")
studentDetails = cursor.fetchall()
# print(studentDetails)
ids = []
names = []
for item in range(len(studentDetails)):
        ids.append(studentDetails[item][0])
        names.append(studentDetails[item][1])
# print(ids,names)
# --------------------------------------------------------------------------------------------
edit = []
# print(num6)
x = ["ID", "name", "s1", "s2", "s3", "s4"]

y = 0


class Dlg(QDialog):

    def __init__(self, nb_row, nb_col,item):
        QDialog.__init__(self)
        self.layout = QGridLayout(self)
        self.label1 = QLabel('النتيجة ')
        self.btn = QPushButton('تم ')
        self.btn.setFixedWidth(100)
        self.nb_row = nb_row
        self.nb_col = nb_col
        self.sending=item

        # creating empty table
        # data = [[] for i in range(self.nb_row)]
        # # self.querys("name",names)

        # for i in range(self.nb_row):
        #     for j in range(self.nb_col):
        #         data[i].append('')
        # self.combo_box = QComboBox(self)

        # for i in x:

        #     self.combo_box.addItem(i)

        list = []
        conn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=E:\project\year\code\exe project\project v1.0\v1\filter.accdb;')
        cursor = conn.cursor()
        fq=int(self.sending)
        if fq:
            sql = f'''select * from student where student_id={self.sending}'''
        else:
            sql = f'''select * from student where student_name={self.sending}'''

        cursor.execute(sql)

        for row in cursor.fetchall():
            print(row)
            list.append(row)
            print(row[0])
            # ALL columns value
            # num1.append(row[0])
            # num2.append(row[1])
            # num3.append(row[2])
            # num4.append(row[3])
            # num5.append(row[4])
            # num6.append(row[5])

        self.table1 = QTableWidget()
        delegate = Delegate1(self.table1)

        self.table1.setItemDelegate(delegate)

        self.table1.setRowCount(self.nb_row)
        self.table1.setColumnCount(self.nb_col)

        self.table1.setHorizontalHeaderLabels(
            ['Id', 'name', "s1", "s2"])
        for row in range(self.nb_row):
            for col in range(self.nb_col):
                item = QTableWidgetItem(str(list[row][col]))
                self.table1.setItem(row, col, item)

        self.layout.addWidget(self.label1, 0, 0)
        # self.layout.addWidget(self.combo_box, 1, 0)
        self.layout.addWidget(self.table1, 2, 0)
        self.layout.addWidget(self.btn, 4, 0)
        self.btn.clicked.connect(self.print_table_values)
    def print_table_values(self, data):
        for row in range(self.nb_row):
            for col in range(self.nb_col):
                print(row, col, self.table1.item(row, col).text())
                edit.append(self.table1.item(row, col).text())
        print(edit)
    # ['Id', 'name', "s1", "s2", "s3", "s4"]
        #  code of ===>>>>>>> update
        conn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=E:\project\year\code\exe project\project v1.0\v1\filter.accdb;')
        cursor = conn.cursor()
       
        sql = f'''UPDATE student SET marks= {int(edit[3])}  where student_id={self.sending}'''
        

            # sql = f'UPDATE student SET  studentlevel={int(x[5])} where student_id={([0])}'
        cursor.execute(sql)
        conn.commit()

        # print("edit 1")


class Delegate1(QtWidgets.QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        if index.column() == 3:
            return super(Delegate1, self).createEditor(parent, option, index)


# -----------------------------------------------------------------------------------------------
class Delegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        if index.data() == "None":
            return super(Delegate, self).createEditor(parent, option, index)



class Home(QMainWindow, MainUi):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon/logo.png"))
        self.setWindowTitle("الازهر")
        self.pushButton.clicked.connect(self.onFire)
        delegate = Delegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        # print(self.tableWidget.currentRow())
        # print(self.tableWidget.currentColumn())

    def onFire(self):
        # self.lineEdit
        if ~ self.pushButton.isChecked():
            text = self.lineEdit.text()
            # غير مكان الداتا بيز
            conn = pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=E:\project\project\filter.accdb;')
            cursor = conn.cursor()

            try:
                text = int(text)
                # WHERE StudentName={text}
                cursor.execute(
                    f"SELECT student_id,student_name  FROM student WHERE student_id={text}")
                data = cursor.fetchall()
                try:
                    if ~ ids.index(text):
                        print(data[0])
                        self.tableWidget.setColumnCount(len(data[0]))
                except ValueError:
                    print("error")
                    QMessageBox.about(self, "Not Found",
                                      f"""{text} not Found! try anotner data  """)
                self.tableWidget.setRowCount(len(data))
                for j in range(len(data)):
                    for i in range(2):
                        self.tableWidget.setHorizontalHeaderLabels(
                            ['Id', 'name'])
                        self.tableWidget.setItem(
                            j, i, QTableWidgetItem(str(data[j][i])))
                        # print(data[j][i])
                        # QMessageBox.about(self, "Title", "Message")
            except:
                text = str(text)
                cursor.execute(
                    f"SELECT student_id,student_name FROM student WHERE student_name='{text}'")
                data = cursor.fetchall()
                try:
                    if ~ names.index(text):
                        print(data[0])
                        self.tableWidget.setColumnCount(len(data[0]))
                except ValueError:
                    print("error")
                    QMessageBox.about(self, "Not Found !",
                                      f"""{text} not Found! try anotner data  """)

                self.tableWidget.setRowCount(len(data))
                for j in range(len(data)):
                    for i in range(2):
                        self.tableWidget.setHorizontalHeaderLabels(
                            ['Id', 'name'])
                        self.tableWidget.setItem(
                            j, i, QTableWidgetItem(str(data[j][i])))
                        # print(data[j][i])
        else:
            print("Unpressed")


    def cell_was_clicked(self, row, column):
        # print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.itemAt(row, column).text()
        print(item)
        if self.lineEdit.text() != "":
            app = QApplication.instance()
            w = Dlg(1, 4,item)
            w.resize(750, 300)
            # print(w.on_combobox_changed())
            w.setWindowTitle('الازهر')
            w.setWindowIcon(QIcon("icon/logo.png"))
            # w.setWindowFlags(Qt.WindowStaysOnTopHint)
            w.show()
            # sys.exit(w.exec_())
            if w.exec_():
                app1 = QApplication(sys.argv)
                window = Home()
                window.show()
                sys.exit(app1.exec())

            

    
            

            
            


def main():
    app1 = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app1.exec())


if __name__ == "__main__":
    main()
