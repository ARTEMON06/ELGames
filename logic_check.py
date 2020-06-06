from PyQt5 import QtWidgets, QtGui
from init_check import Ui_check
from resurse_lib import Resurse
import subprocess as sub
import sys

class check(QtWidgets.QMainWindow):
	"""docstring for check"""
	def __init__(self):
		super (check, self).__init__()
		self.ui = Ui_check()
		self.ui.setupUi(self)
		self.ui.yes.clicked.connect(self.yes)
		self.ui.no.clicked.connect(self.no)

	def yes(self):
		Resurse("баллы").write(0)
		sub.Popen(["python.exe", "logic_options.py"])
		sys.exit()

	def no(self):
		sub.Popen(["python.exe", "logic_options.py"])
		sys.exit()

app = QtWidgets.QApplication([])
application = check()
application.show()
sys.exit(app.exec())
		