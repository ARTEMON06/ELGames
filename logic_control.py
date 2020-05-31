from PyQt5 import QtWidgets, QtGui
from init_control import Ui_control
from resurse_lib import Resurse
import subprocess as sub
import sys

class control(QtWidgets.QMainWindow):
	def __init__(self):
		super(control, self).__init__()
		self.ui = Ui_control()
		self.ui.setupUi(self)
		self.ui.home.clicked.connect(self.home)
		self.ui.hour.setMinimum(0)
		self.ui.hour.setMaximum(23)
		self.ui.min.setMinimum(0)
		self.ui.min.setMaximum(59)
		self.ui.min.valueChanged.connect(self.min)
		self.ui.hour.valueChanged.connect(self.hour)
		self.resTime()

	def resTime(self):
		self.ui.min.setValue(int(Resurse("min").read()))
		self.ui.hour.setValue(int(Resurse("hour").read()))

	def hour(self, value):
		self.hours = value

	def min(self, value):
		self.minutes = value
		

	def home(self):
		Resurse("min").write(self.minutes)
		Resurse("hour").write(self.hours)
		sub.Popen(["python.exe", "logic_options.py"])
		sys.exit()

app = QtWidgets.QApplication([])
application = control()
application.show()
sys.exit(app.exec())