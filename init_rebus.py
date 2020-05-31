# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_rebus.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from resurse_lib import Resurse

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rebus(object):

    def setupUi(self, rebus):
        rebus.setObjectName("rebus")
        rebus.resize(666, 394)
        with open(Resurse("theme").read(), "r") as file:
            text = file.read()
            rebus.setStyleSheet(text)
        self.bals = QtWidgets.QLabel(rebus)
        self.bals.setGeometry(QtCore.QRect(530, 50, 121, 31))
        self.bals.setStyleSheet("font: 75 14pt \"Verdana\";\n"
                                "background-color: none;\nborder: none;")
        self.bals.setAlignment(QtCore.Qt.AlignLeading |
                               QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.bals.setObjectName("bals")
        self.heart = QtWidgets.QLabel(rebus)
        self.heart.setGeometry(QtCore.QRect(490, 50, 31, 31))
        self.heart.setStyleSheet("background-color: none;\nborder: none;")
        self.heart.setText("")
        self.heart.setPixmap(QtGui.QPixmap(Resurse("heart").read()))
        self.heart.setScaledContents(True)
        self.heart.setObjectName("heart")
        self.icon_2 = QtWidgets.QLabel(rebus)
        self.icon_2.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.icon_2.setStyleSheet("background-color: none;\nborder: none;")
        self.icon_2.setText("")
        self.icon_2.setPixmap(QtGui.QPixmap(Resurse("option").read()))
        self.icon_2.setScaledContents(True)
        self.icon_2.setWordWrap(False)
        self.icon_2.setOpenExternalLinks(False)
        self.icon_2.setObjectName("icon_2")
        self.pushButton = QtWidgets.QPushButton(rebus)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.pushButton.setStyleSheet("background-color: none;\nborder: none")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.home = QtWidgets.QPushButton(rebus)
        self.home.setGeometry(QtCore.QRect(560, 350, 91, 31))
        self.home.setObjectName("home")
        self.reb = QtWidgets.QLabel(rebus)
        self.reb.setGeometry(QtCore.QRect(150, 40, 331, 161))
        self.reb.setStyleSheet("background-color: none;\nborder: none;")
        self.reb.setText("")
        self.reb.setPixmap(QtGui.QPixmap("Ресурс_ребусы/0.jpg"))
        self.reb.setScaledContents(True)
        self.reb.setWordWrap(False)
        self.reb.setObjectName("reb")
        self.otvet = QtWidgets.QLineEdit(rebus)
        self.otvet.setGeometry(QtCore.QRect(150, 260, 331, 51))
        self.otvet.setStyleSheet("")
        self.otvet.setAlignment(QtCore.Qt.AlignCenter)
        self.otvet.setObjectName("otvet")
        self.ask = QtWidgets.QPushButton(rebus)
        self.ask.setGeometry(QtCore.QRect(150, 320, 331, 31))
        self.ask.setStyleSheet("")
        self.ask.setObjectName("ask")
        self.lol = QtWidgets.QPushButton(rebus)
        self.lol.setGeometry(QtCore.QRect(490, 260, 141, 51))
        self.lol.setObjectName("lol")
        self.label = QtWidgets.QLabel(rebus)
        self.label.setGeometry(QtCore.QRect(200, 210, 231, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.svaip = QtWidgets.QPushButton(rebus)
        self.svaip.setGeometry(QtCore.QRect(490, 210, 141, 41))
        self.svaip.setObjectName("svaip")
        self.green = QtWidgets.QLabel(rebus)
        self.green.setGeometry(QtCore.QRect(150, 210, 41, 41))
        self.green.setText("")
        self.green.setPixmap(QtGui.QPixmap("Ресурс/green_reb.png"))
        self.green.setObjectName("green")
        self.red1 = QtWidgets.QLabel(rebus)
        self.red1.setGeometry(QtCore.QRect(150, 210, 41, 41))
        self.red1.setText("")
        self.red1.setPixmap(QtGui.QPixmap("Ресурс/red_reb.jpg"))
        self.red1.setObjectName("red1")
        self.red = QtWidgets.QLabel(rebus)
        self.red.setGeometry(QtCore.QRect(440, 210, 41, 41))
        self.red.setText("")
        self.red.setPixmap(QtGui.QPixmap("Ресурс/red_reb.jpg"))
        self.red.setObjectName("red")
        self.green1 = QtWidgets.QLabel(rebus)
        self.green1.setGeometry(QtCore.QRect(440, 210, 41, 41))
        self.green1.setText("")
        self.green1.setPixmap(QtGui.QPixmap("Ресурс/green_reb.png"))
        self.green1.setObjectName("green1")
        self.green.setVisible(False)
        self.red.setVisible(False)
        self.green1.setVisible(False)
        self.red1.setVisible(False)
        self.retranslateUi(rebus)
        QtCore.QMetaObject.connectSlotsByName(rebus)

    def retranslateUi(self, rebus):
        _translate = QtCore.QCoreApplication.translate
        rebus.setWindowTitle(_translate("rebus", "Form"))
        self.bals.setText(_translate(
            "rebus", "<html><head/><body><p>0</p></body></html>"))
        self.home.setText(_translate("rebus", "назад"))
        self.ask.setText(_translate("rebus", "ОТВЕТИТЬ!"))
        self.lol.setText(_translate("rebus", "Показать ответ"))
        self.label.setText(_translate("rebus", "↓ Напиши слово ↓"))
        self.svaip.setText(_translate("rebus", "Пропустить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rebus = QtWidgets.QWidget()
    ui = Ui_rebus()
    ui.setupUi(rebus)
    rebus.show()
    sys.exit(app.exec_())
