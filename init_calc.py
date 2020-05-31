# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_calc.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from resurse_lib import Resurse

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calc(object):
	def setupUi(self, calc):
		calc.setObjectName("calc")
		calc.resize(666, 394)
		with open(Resurse("theme").read(), "r") as file:
			text = file.read()
			calc.setStyleSheet(text)
		self.heart = QtWidgets.QLabel(calc)
		self.heart.setGeometry(QtCore.QRect(490, 50, 31, 31))
		self.heart.setStyleSheet("background-color: none;\nborder: none;")
		self.heart.setText("")
		self.heart.setPixmap(QtGui.QPixmap(Resurse("heart").read()))
		self.heart.setScaledContents(True)
		self.heart.setObjectName("heart")
		self.bals = QtWidgets.QLabel(calc)
		self.bals.setGeometry(QtCore.QRect(530, 50, 121, 31))
		self.bals.setStyleSheet("font: 75 14pt \"Verdana\";\n"
		"background-color: none;\nborder: none;")
		self.bals.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.bals.setObjectName("bals")
		self.quest = QtWidgets.QLabel(calc)
		self.quest.setGeometry(QtCore.QRect(20, 210, 341, 71))
		self.quest.setStyleSheet("")
		self.quest.setText("")
		self.quest.setObjectName("quest")
		self.ask = QtWidgets.QPushButton(calc)
		self.ask.setGeometry(QtCore.QRect(530, 210, 121, 71))
		self.ask.setStyleSheet("")
		self.ask.setObjectName("ask")
		self.svaip = QtWidgets.QPushButton(calc)
		self.svaip.setGeometry(QtCore.QRect(530, 290, 121, 31))
		self.svaip.setObjectName("svaip")
		self.icon = QtWidgets.QLabel(calc)
		self.icon.setGeometry(QtCore.QRect(270, 20, 131, 111))
		self.icon.setStyleSheet("background-color: none;\nborder: none;")
		self.icon.setText("")
		self.icon.setPixmap(QtGui.QPixmap(Resurse("logo").read()))
		self.icon.setScaledContents(True)
		self.icon.setWordWrap(False)
		self.icon.setOpenExternalLinks(False)
		self.icon.setObjectName("icon")
		self.otvet = QtWidgets.QLineEdit(calc)
		self.otvet.setGeometry(QtCore.QRect(370, 210, 151, 71))
		self.otvet.setStyleSheet("")
		self.otvet.setObjectName("otvet")
		self.home = QtWidgets.QPushButton(calc)
		self.home.setGeometry(QtCore.QRect(560, 350, 91, 31))
		self.home.setObjectName("home")
		self.true_l = QtWidgets.QLabel(calc)
		self.true_l.setGeometry(QtCore.QRect(375, 170, 121, 31))
		self.true_l.setStyleSheet("background-color: none;\ncolor: green;\nborder: none;")
		self.true_l.setAlignment(QtCore.Qt.AlignCenter)
		self.true_l.setObjectName("true_l")
		self.true_l.setVisible(0)
		self.label_3 = QtWidgets.QLabel(calc)
		self.label_3.setGeometry(QtCore.QRect(375, 170, 141, 31))
		self.label_3.setStyleSheet("background-color: none;\ncolor: red;\nborder: none;")
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.label_3.setVisible(0)
		self.icon_2 = QtWidgets.QLabel(calc)
		self.icon_2.setGeometry(QtCore.QRect(10, 10, 61, 61))
		self.icon_2.setStyleSheet("background-color: none;\nborder: none;")
		self.icon_2.setText("")
		self.icon_2.setPixmap(QtGui.QPixmap(Resurse("option").read()))
		self.icon_2.setScaledContents(True)
		self.icon_2.setWordWrap(False)
		self.icon_2.setOpenExternalLinks(False)
		self.icon_2.setObjectName("icon_2")
		self.pushButton = QtWidgets.QPushButton(calc)
		self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 61))
		self.pushButton.setStyleSheet("background-color: none;\nborder: none")
		self.pushButton.setText("")
		self.pushButton.setObjectName("pushButton")
		self.lol = QtWidgets.QPushButton(calc)
		self.lol.setGeometry(QtCore.QRect(370, 290, 151, 31))
		self.lol.setObjectName("lol")

		self.retranslateUi(calc)
		QtCore.QMetaObject.connectSlotsByName(calc)

	def retranslateUi(self, calc):
		_translate = QtCore.QCoreApplication.translate
		calc.setWindowTitle(_translate("calc", "Form"))
		self.bals.setText(_translate("calc", "<html><head/><body><p>0</p></body></html>"))
		self.ask.setText(_translate("calc", "ОТВЕТИТЬ!"))
		self.svaip.setText(_translate("calc", "Пропустить"))
		self.home.setText(_translate("calc", "назад"))
		self.true_l.setText(_translate("calc", "Правильно"))
		self.label_3.setText(_translate("calc", "Неправильно"))
		self.lol.setText(_translate("calc", "Показать ответ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calc = QtWidgets.QWidget()
    ui = Ui_calc()
    ui.setupUi(calc)
    calc.show()
    sys.exit(app.exec_())
