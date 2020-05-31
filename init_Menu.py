# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from resurse_lib import Resurse
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
	def setupUi(self, Menu):
		Menu.setObjectName("Menu")
		Menu.setFixedSize(666, 360)
		with open(Resurse("theme").read(), "r") as file:
			text = file.read()
			Menu.setStyleSheet(text)
		self.heart = QtWidgets.QLabel(Menu)
		self.heart.setGeometry(QtCore.QRect(490, 50, 31, 31))
		self.heart.setStyleSheet("background-color: none;\nborder: none;")
		self.heart.setText("")
		self.heart.setPixmap(QtGui.QPixmap(Resurse("heart").read()))
		self.heart.setScaledContents(True)
		self.heart.setObjectName("heart")
		self.bals = QtWidgets.QLabel(Menu)
		self.bals.setGeometry(QtCore.QRect(530, 50, 121, 31))
		self.bals.setStyleSheet("font: 75 14pt \"Verdana\";\n"
		"background-color: none;\nborder: none;")
		self.bals.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.bals.setObjectName("baenels")
		self.horizontalLayoutWidget = QtWidgets.QWidget(Menu)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 223, 581, 50))
		self.horizontalLayoutWidget.setStyleSheet("")
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.butMenu = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.butMenu.setContentsMargins(0, 0, 0, 0)
		self.butMenu.setSpacing(1)
		self.butMenu.setObjectName("butMenu")
		self.ex = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.ex.setStyleSheet("")
		self.ex.setObjectName("ex")
		self.butMenu.addWidget(self.ex)
		self.games = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.games.setStyleSheet("")
		self.games.setObjectName("games")
		self.butMenu.addWidget(self.games)
		self.reb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.reb.setStyleSheet("")
		self.reb.setObjectName("reb")
		self.butMenu.addWidget(self.reb)
		self.icon = QtWidgets.QLabel(Menu)
		self.icon.setGeometry(QtCore.QRect(240, 40, 171, 151))
		self.icon.setStyleSheet("background-color: none;\nborder: none;")
		self.icon.setText("")
		self.icon.setPixmap(QtGui.QPixmap(Resurse("logo").read()))
		self.icon.setScaledContents(True)
		self.icon.setWordWrap(False)
		self.icon.setOpenExternalLinks(False)
		self.icon.setObjectName("icon")
		self.icon_2 = QtWidgets.QLabel(Menu)
		self.icon_2.setGeometry(QtCore.QRect(10, 10, 61, 61))
		self.icon_2.setStyleSheet("background-color: none;\nborder: none;")
		self.icon_2.setText("")
		self.icon_2.setPixmap(QtGui.QPixmap(Resurse("option").read()))
		self.icon_2.setScaledContents(True)
		self.icon_2.setWordWrap(False)
		self.icon_2.setOpenExternalLinks(False)
		self.icon_2.setObjectName("icon_2")
		self.pushButton = QtWidgets.QPushButton(Menu)
		self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 61))
		self.pushButton.setStyleSheet("background-color: none;\nborder: none")
		self.pushButton.setText("")
		self.pushButton.setObjectName("pushButton")


		self.retranslateUi(Menu)
		QtCore.QMetaObject.connectSlotsByName(Menu)

	def retranslateUi(self, Menu):
		_translate = QtCore.QCoreApplication.translate
		Menu.setWindowTitle(_translate("Menu", "Form"))
		self.bals.setText(_translate("calc", "<html><head/><body><p>0</p></body></html>"))
		self.ex.setText(_translate("Menu", "Примеры"))
		self.games.setText(_translate("Menu", "Задачки"))
		self.reb.setText(_translate("Menu", "Загадки и Ребусы"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu_ = QtWidgets.QWidget()
    ui = Ui_Menu()
    ui.setupUi(Menu_)
    Menu_.show()
    sys.exit(app.exec_())
