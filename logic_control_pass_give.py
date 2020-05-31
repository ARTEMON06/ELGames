from PyQt5 import QtWidgets, QtGui
from init_control_pass_give import Ui_control_pass_give
from resurse_lib import Resurse
import subprocess as sub
import sys

class control_pass_give(QtWidgets.QMainWindow):
	def __init__(self):
		super(control_pass_give, self).__init__()
		self.ui = Ui_control_pass_give()
		self.ui.setupUi(self)
		self.ui.go.clicked.connect(self.go)
		self.ui.porol.setFocus()
		self.ui.porol.returnPressed.connect(self.go)
		self.ui.porol.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ui.home.clicked.connect(self.home)

	def go(self):
		text = self.ui.porol.text()
		porol = Resurse("password", "password").read()

		if text != porol:
			self.ui.error.setText("Неверный пароль!")
			self.ui.porol.clear()
			self.ui.porol.setFocus()
			self.ui.error.setVisible(True)
			if Resurse("theme").read() == "css_style.txt":
				self.ui.porol.setStyleSheet("border-right: 5px ridge darkred;\nborder-bottom: 5px ridge darkred;\n")
			else:
				self.ui.porol.setStyleSheet("border: 3px solid red")

		else:
			self.ui.error.setVisible(False)
			sub.Popen(["python.exe", "logic_control.py"])
			sys.exit()

	def home(self):
		sub.Popen(["python.exe", "logic_options.py"])
		sys.exit()





app = QtWidgets.QApplication([])
application = control_pass_give()
application.show()
sys.exit(app.exec())