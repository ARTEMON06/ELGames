import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess as sub
from resurse_lib import Resurse
from init_Menu import Ui_Menu


class Menu(QtWidgets.QWidget):
    def __init__(self):
        super(Menu, self).__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.option)
        self.ui.reb.clicked.connect(self.reb)
        self.ui.ex.clicked.connect(self.exercises)
        self.heart()

    def reb(self):
        sub.Popen(["python.exe", "logic_Menu_rebus.py"])
        sys.exit()

    def exercises(self):
    	sub.Popen(["python.exe", "logic_calc.py"])
    	sys.exit() 

    def option(self):
        opt = Resurse("настройки")
        opt.write("logic_Menu")
        sub.Popen(["python.exe", "logic_options.py"])
        sys.exit()

    def heart(self):
        self.ui.bals.setText(str(Resurse("баллы").read()))

s = sub.Popen(["python.exe", "# START PROGRAM #.py"])

app = QtWidgets.QApplication([])
application = Menu()
application.show()
s.kill()
sys.exit(app.exec())
