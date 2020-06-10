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
		self.ui.hour_2.setMinimum(0)
		self.ui.hour_2.setMaximum(23)
		self.ui.min_2.setMinimum(0)
		self.ui.min_2.setMaximum(59)
		self.ui.min.valueChanged.connect(self.min)
		self.ui.hour.valueChanged.connect(self.hour)
		self.ui.min_2.valueChanged.connect(self.min_2)
		self.ui.hour_2.valueChanged.connect(self.hour_2)
		self.ui.hour.setToolTip("Заданные настройки заработают при следующем включении!")
		self.ui.min.setToolTip("Заданные настройки заработают при следующем включении!")
		self.ui.hour_2.setToolTip("Заданные настройки заработают при следующем включении!")
		self.ui.min_2.setToolTip("Заданные настройки заработают при следующем включении!")
		with open("text_control.txt", "r", encoding = "utf-8") as file:
			self.ui.textEdit.setText(file.read())
		self.resTime()
		self.hours = Resurse("hour").read()
		self.hours_2 = Resurse("hour_2").read()
		self.minutes = Resurse("min").read()
		self.minutes_2 = Resurse("min_2").read()

	def resTime(self):
		self.ui.min.setValue(int(Resurse("min").read()))
		self.ui.hour.setValue(int(Resurse("hour").read()))
		self.ui.min_2.setValue(int(Resurse("min_2").read()))
		self.ui.hour_2.setValue(int(Resurse("hour_2").read()))

	def hour(self, value):
		self.hours = value

	def min(self, value):
		self.minutes = value

	def hour_2(self, value):
		self.hours_2 = value

	def min_2(self, value):
		self.minutes_2 = value
		

	def home(self):
		Resurse("min").write(self.minutes)
		Resurse("hour").write(self.hours)
		Resurse("min_2").write(self.minutes_2)
		Resurse("hour_2").write(self.hours_2)
		with open("text_control.txt", "w", encoding = "utf-8") as file:
			file.write(self.ui.textEdit.toPlainText())
		sub.Popen(["python.exe", "logic_options.py"])
		sys.exit()

app = QtWidgets.QApplication([])
application = control()
application.show()
sys.exit(app.exec())