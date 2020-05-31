

from resurse_lib import Resurse

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu_rebus(object):
	def setupUi(self, Menu_rebus):
		Menu_rebus.setObjectName("Menu_rebus")
		Menu_rebus.resize(666, 394)
		with open(Resurse("theme").read(), "r") as file:
			text = file.read()
			Menu_rebus.setStyleSheet(text)
		self.icon = QtWidgets.QLabel(Menu_rebus)
		self.icon.setGeometry(QtCore.QRect(240, 40, 171, 151))
		self.icon.setStyleSheet("background-color: none;\nborder: none;")
		self.icon.setText("")
		self.icon.setPixmap(QtGui.QPixmap(Resurse("logo").read()))
		self.icon.setScaledContents(True)
		self.icon.setWordWrap(False)
		self.icon.setOpenExternalLinks(False)
		self.icon.setObjectName("icon")
		self.icon_2 = QtWidgets.QLabel(Menu_rebus)
		self.icon_2.setGeometry(QtCore.QRect(10, 10, 61, 61))
		self.icon_2.setStyleSheet("background-color: none;\nborder: none;")
		self.icon_2.setText("")
		self.icon_2.setPixmap(QtGui.QPixmap(Resurse("option").read()))
		self.icon_2.setScaledContents(True)
		self.icon_2.setWordWrap(False)
		self.icon_2.setOpenExternalLinks(False)
		self.icon_2.setObjectName("icon_2")
		self.pushButton = QtWidgets.QPushButton(Menu_rebus)
		self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 61))
		self.pushButton.setStyleSheet("background-color: none;\nborder: none")
		self.pushButton.setText("")
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayoutWidget = QtWidgets.QWidget(Menu_rebus)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 270, 581, 52))
		self.horizontalLayoutWidget.setStyleSheet("")
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.butMenu = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.butMenu.setContentsMargins(0, 0, 0, 0)
		self.butMenu.setSpacing(1)
		self.butMenu.setObjectName("butMenu")
		self.zadacha = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.zadacha.setStyleSheet("")
		self.zadacha.setObjectName("zadacha")
		self.butMenu.addWidget(self.zadacha)
		self.rebus = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.rebus.setStyleSheet("")
		self.rebus.setObjectName("rebus")
		self.butMenu.addWidget(self.rebus)
		self.heart = QtWidgets.QLabel(Menu_rebus)
		self.heart.setGeometry(QtCore.QRect(490, 50, 31, 31))
		self.heart.setStyleSheet("background-color: none;\nborder: none;")
		self.heart.setText("")
		self.heart.setPixmap(QtGui.QPixmap(Resurse("heart").read()))
		self.heart.setScaledContents(True)
		self.heart.setObjectName("heart")
		self.bals = QtWidgets.QLabel(Menu_rebus)
		self.bals.setGeometry(QtCore.QRect(530, 50, 121, 31))
		self.bals.setStyleSheet("font: 75 14pt \"Verdana\";\n"
		"background-color: none;\n border: none;")
		self.bals.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.bals.setObjectName("bals")
		self.home = QtWidgets.QPushButton(Menu_rebus) 
		self.home.setGeometry(QtCore.QRect(560, 350, 91, 31))
		self.home.setObjectName("home")

		self.retranslateUi(Menu_rebus)
		QtCore.QMetaObject.connectSlotsByName(Menu_rebus)

	def retranslateUi(self, Menu_rebus):
		_translate = QtCore.QCoreApplication.translate
		Menu_rebus.setWindowTitle(_translate("Menu_rebus", "Form"))
		self.bals.setText(_translate("Menu_rebus", "<html><head/><body><p>0</p></body></html>"))
		self.home.setText(_translate("Menu_rebus", "назад"))
		self.zadacha.setText(_translate("Menu_rebus", "Загадки"))
		self.rebus.setText(_translate("Menu_rebus", "Ребусы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu_rebus = QtWidgets.QWidget()
    ui = Ui_Menu_rebus()
    ui.setupUi(Menu_rebus)
    Menu_rebus.show()
    sys.exit(app.exec_())
