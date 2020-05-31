from PyQt5 import QtWidgets, QtGui
from INITFILE import INITCLASS
from resurse_lib import Resurse
import subprocess as sub
import sys

class NAME(QtWidgets.QMainWindow):
	def __init__(self):
		super(NAME, self).__init__()
		self.ui = INITCLASS()
		self.ui.setupUi(self)
		self.ui.





app = QtWidgets.QApplication([])
application = NAME()
application.show()
sys.exit(app.exec())