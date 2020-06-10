# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Artem/Desktop/АРТЕМ/ELGames/QT_end.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from resurse_lib import Resurse
import sys

class Ui_end(object):
	def setupUi(self, end):
		end.setObjectName("end")
		end.resize(402, 228)
		with open(Resurse("theme").read(), "r") as file:
				text = file.read()
				end.setStyleSheet(text)
		self.textBrowser = QtWidgets.QTextBrowser(end)
		self.textBrowser.setGeometry(QtCore.QRect(10, 10, 381, 201))
		self.textBrowser.setObjectName("textBrowser")
		with open("text_control", "r") as file:
			self.textBrowser.setText(file.read())
		self.retranslateUi(end)
		QtCore.QMetaObject.connectSlotsByName(end)
		QTimer.singleShot(5000, lambda: sys.exit())

	def retranslateUi(self, end):
		_translate = QtCore.QCoreApplication.translate
		end.setWindowTitle(_translate("end", "Form"))


if __name__ == "__main__":
	
	app = QtWidgets.QApplication(sys.argv)
	end = QtWidgets.QWidget()
	ui = Ui_end()
	ui.setupUi(end)
	end.show()
	sys.exit(app.exec_())
