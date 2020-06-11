from PyQt5 import QtWidgets, QtGui
from init_control_pass_take import Ui_control_pass_take
from resurse_lib import Resurse
import subprocess as sub
import sys

class control_pass_take(QtWidgets.QMainWindow):
	def __init__(self):
		super(control_pass_take, self).__init__()
		self.ui = Ui_control_pass_take()
		self.ui.setupUi(self)
		self.ui.home.clicked.connect(self.home)
		self.ui.go.clicked.connect(self.go)
		self.ui.porol.returnPressed.connect(self.go)
		self.ui.porol.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ui.porol.setFocus()

	def error(self):
		if Resurse("theme").read() == "css_style.txt":
			self.ui.porol.setStyleSheet("border-right: 5px ridge darkred;\nborder-bottom: 5px ridge darkred;\n")
		else:
			self.ui.porol.setStyleSheet("border: 3px solid red")


	def go(self):
		text = self.ui.porol.text()

		if len(text)==0:
			self.ui.error.setText("Это поле не должно быть пустым!")
			self.ui.error.setVisible(True)
			self.error()

		else:
			self.ui.error.setVisible(False)
			Resurse("password", "password").write(text)
			Resurse("password").write(1)
			sub.Popen(["python.exe", "logic_control.py"])
			sys.exit()

	def home(self):
		sub.Popen(["python.exe", "logic_options.py"])
		sys.exit()

app = QtWidgets.QApplication([])
application = control_pass_take()
application.show()
sys.exit(app.exec())