# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Artem/Desktop/АРТЕМ/ELGames/QT_control.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from resurse_lib import Resurse


class Ui_control(object):
	def setupUi(self, control):
		control.setObjectName("control")
		control.resize(671, 524)
		with open(Resurse("theme").read(), "r") as file:
				text = file.read()
				control.setStyleSheet(text)
		self.label = QtWidgets.QLabel(control)
		self.label.setGeometry(QtCore.QRect(0, 20, 671, 61))
		self.label.setStyleSheet("background-color: none;\n"
"font: 75 22pt \"Calibri\";")
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(control)
		self.label_2.setGeometry(QtCore.QRect(340, 110, 311, 71))
		self.label_2.setWordWrap(True)
		self.label_2.setObjectName("label_2")
		self.home = QtWidgets.QPushButton(control)
		self.home.setGeometry(QtCore.QRect(550, 480, 101, 31))
		self.home.setObjectName("home")
		self.hour = QtWidgets.QSpinBox(control)
		self.hour.setGeometry(QtCore.QRect(20, 150, 101, 31))
		self.hour.setObjectName("hour")
		self.min = QtWidgets.QSpinBox(control)
		self.min.setGeometry(QtCore.QRect(170, 150, 101, 31))
		self.min.setObjectName("min")
		self.label_3 = QtWidgets.QLabel(control)
		self.label_3.setGeometry(QtCore.QRect(20, 110, 101, 31))
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(control)
		self.label_4.setGeometry(QtCore.QRect(170, 110, 101, 31))
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(control)
		self.label_5.setGeometry(QtCore.QRect(20, 210, 101, 31))
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(control)
		self.label_6.setGeometry(QtCore.QRect(170, 210, 101, 31))
		self.label_6.setAlignment(QtCore.Qt.AlignCenter)
		self.label_6.setObjectName("label_6")
		self.hour_2 = QtWidgets.QSpinBox(control)
		self.hour_2.setGeometry(QtCore.QRect(20, 250, 101, 31))
		self.hour_2.setObjectName("hour_2")
		self.min_2 = QtWidgets.QSpinBox(control)
		self.min_2.setGeometry(QtCore.QRect(170, 250, 101, 31))
		self.min_2.setObjectName("min_2")
		self.label_7 = QtWidgets.QLabel(control)
		self.label_7.setGeometry(QtCore.QRect(340, 210, 311, 71))
		self.label_7.setWordWrap(True)
		self.label_7.setObjectName("label_7")
		self.textEdit = QtWidgets.QTextEdit(control)
		self.textEdit.setGeometry(QtCore.QRect(20, 310, 251, 131))
		self.textEdit.setObjectName("textEdit")
		self.label_8 = QtWidgets.QLabel(control)
		self.label_8.setGeometry(QtCore.QRect(340, 310, 311, 131))
		self.label_8.setWordWrap(True)
		self.label_8.setObjectName("label_8")

		self.retranslateUi(control)
		QtCore.QMetaObject.connectSlotsByName(control)

	def retranslateUi(self, control):
		_translate = QtCore.QCoreApplication.translate
		control.setWindowTitle(_translate("control", "Form"))
		self.label.setText(_translate("control", "Родительский контроль"))
		self.label_2.setText(_translate("control", "Настройка максимального времени игры."))
		self.home.setText(_translate("control", "Сохранить"))
		self.label_3.setText(_translate("control", "Часы"))
		self.label_4.setText(_translate("control", "Минуты"))
		self.label_5.setText(_translate("control", "Часы"))
		self.label_6.setText(_translate("control", "Минуты"))
		self.label_7.setText(_translate("control", "Настройка времени между запусками приложения."))
		self.textEdit.setHtml(_translate("control", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ты играешь уже достаточно много!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пора отдохнуть...</p></body></html>"))
		self.label_8.setText(_translate("control", "Настройка текста, выводящегося по достижению максимального времени игры."))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	control = QtWidgets.QWidget()
	ui = Ui_control()
	ui.setupUi(control)
	control.show()
	sys.exit(app.exec_())
