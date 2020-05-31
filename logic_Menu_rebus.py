from PyQt5 import QtWidgets, QtGui
from init_Menu_rebus import Ui_Menu_rebus
from resurse_lib import Resurse
import subprocess as sub
import sys

class Menu_rebus(QtWidgets.QMainWindow):
	def __init__(self):
		super(Menu_rebus, self).__init__()
		self.ui = Ui_Menu_rebus()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.option)
		self.ui.home.clicked.connect(self.home)
		self.ui.rebus.clicked.connect(self.reb)
		self.heart()

	def reb(self):
		sub.Popen(["python.exe", "logic_rebus.py"])
		sys.exit()

	def home(self):
		sub.Popen(["python.exe", "logic_Menu.py"])
		sys.exit()

	def heart(self):
		self.ui.bals.setText(str(Resurse("баллы").read()))

	def option(self):
		opt = Resurse("настройки")
		opt.write("logic_Menu_rebus")
		sub.Popen(["python.exe", "logic_options.py"])
		sys.exit()


app = QtWidgets.QApplication([])
application = Menu_rebus()
application.show()
sys.exit(app.exec())