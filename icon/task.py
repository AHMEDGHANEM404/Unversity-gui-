from typing import Counter, NewType
from PyQt5 import *
from PySide2 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

class mainwindows(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,400)
        self.counter=0
        self.show()

    def greeting(self):
        
        self.counter+=1
        print(self.counter)
        self.update()

def main():
    app=QtWidgets.QApplication(sys.argv)
    window= mainwindows()
    window.greeting()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#     def print_name(self):
#         print(self.name)
        
#     def give_me_a_printer_function(self):
#         return self.print_name

# spam = Foo('Spam')
# my_function1 = spam.print_name
# my_function2 = spam.give_me_a_printer_function()
# my_function1()
# my_function2()
