# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Artem/Desktop/АРТЕМ/ELGames/QT_tasks.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from resurse_lib import Resurse


class Ui_tasks(object):

    def setupUi(self, task):
        task.setObjectName("task")
        task.resize(666, 394)
        with open(Resurse("theme").read(), "r") as file:
            text = file.read()
            task.setStyleSheet(text)
        self.bals = QtWidgets.QLabel(task)
        self.bals.setGeometry(QtCore.QRect(530, 50, 121, 31))
        self.bals.setStyleSheet(
            "font: 75 14pt \"Verdana\";\nbackground-color: none;\nborder: none;")
        self.bals.setAlignment(QtCore.Qt.AlignLeading |
                               QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.bals.setObjectName("bals")
        self.heart = QtWidgets.QLabel(task)
        self.heart.setGeometry(QtCore.QRect(490, 50, 31, 31))
        self.heart.setStyleSheet("background-color: none")
        self.heart.setText("")
        self.heart.setPixmap(QtGui.QPixmap(Resurse("heart").read()))
        self.heart.setScaledContents(True)
        self.heart.setObjectName("heart")
        self.heart.setStyleSheet("background-color: none;\nborder: none;")
        self.icon_2 = QtWidgets.QLabel(task)
        self.icon_2.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.icon_2.setStyleSheet("background-color: none")
        self.icon_2.setText("")
        self.icon_2.setPixmap(QtGui.QPixmap(Resurse("option").read()))
        self.icon_2.setScaledContents(True)
        self.icon_2.setWordWrap(False)
        self.icon_2.setOpenExternalLinks(False)
        self.icon_2.setObjectName("icon_2")
        self.icon_2.setStyleSheet("background-color: none;\nborder: none;")
        self.pushButton = QtWidgets.QPushButton(task)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.pushButton.setStyleSheet("background-color: none;\nborder: none;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.home = QtWidgets.QPushButton(task)
        self.home.setGeometry(QtCore.QRect(560, 350, 91, 31))
        self.home.setObjectName("home")
        self.otvet = QtWidgets.QLineEdit(task)
        self.otvet.setGeometry(QtCore.QRect(150, 260, 331, 51))
        self.otvet.setStyleSheet("")
        self.otvet.setAlignment(QtCore.Qt.AlignCenter)
        self.otvet.setObjectName("otvet")
        self.ask = QtWidgets.QPushButton(task)
        self.ask.setGeometry(QtCore.QRect(150, 320, 331, 31))
        self.ask.setStyleSheet("")
        self.ask.setObjectName("ask")
        self.lol = QtWidgets.QPushButton(task)
        self.lol.setGeometry(QtCore.QRect(490, 260, 141, 51))
        self.lol.setObjectName("lol")
        self.label = QtWidgets.QLabel(task)
        self.label.setGeometry(QtCore.QRect(200, 210, 231, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.svaip = QtWidgets.QPushButton(task)
        self.svaip.setGeometry(QtCore.QRect(490, 210, 141, 41))
        self.svaip.setObjectName("svaip")
        self.label = QtWidgets.QLabel(task)
        self.label.setGeometry(QtCore.QRect(200, 210, 231, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.svaip = QtWidgets.QPushButton(task)
        self.svaip.setGeometry(QtCore.QRect(490, 210, 141, 41))
        self.svaip.setObjectName("svaip")
        self.green = QtWidgets.QLabel(task)
        self.green.setGeometry(QtCore.QRect(150, 210, 41, 41))
        self.green.setText("")
        self.green.setPixmap(QtGui.QPixmap("Ресурс/green_reb.png"))
        self.green.setObjectName("green")
        self.red1 = QtWidgets.QLabel(task)
        self.red1.setGeometry(QtCore.QRect(150, 210, 41, 41))
        self.red1.setText("")
        self.red1.setPixmap(QtGui.QPixmap("Ресурс/red_reb.jpg"))
        self.red1.setObjectName("red1")
        self.red = QtWidgets.QLabel(task)
        self.red.setGeometry(QtCore.QRect(440, 210, 41, 41))
        self.red.setText("")
        self.red.setPixmap(QtGui.QPixmap("Ресурс/red_reb.jpg"))
        self.red.setObjectName("red")
        self.green1 = QtWidgets.QLabel(task)
        self.green1.setGeometry(QtCore.QRect(440, 210, 41, 41))
        self.green1.setText("")
        self.green1.setPixmap(QtGui.QPixmap("Ресурс/green_reb.png"))
        self.green1.setObjectName("green1")
        self.green.setVisible(False)
        self.red.setVisible(False)
        self.green1.setVisible(False)
        self.red1.setVisible(False)
        self.task = QtWidgets.QLabel(task)
        self.task.setGeometry(QtCore.QRect(150, 80, 331, 121))
        self.task.setText("")
        self.task.setObjectName("task")

        self.retranslateUi(task)
        QtCore.QMetaObject.connectSlotsByName(task)

    def retranslateUi(self, task):
        _translate = QtCore.QCoreApplication.translate
        task.setWindowTitle(_translate("task", "Form"))
        self.bals.setText(_translate(
            "task", "<html><head/><body><p>0</p></body></html>"))
        self.home.setText(_translate("task", "назад"))
        self.ask.setText(_translate("task", "ОТВЕТИТЬ!"))
        self.lol.setText(_translate("task", "Показать ответ"))
        self.label.setText(_translate("task", "↓ Напиши ответ ↓"))
        self.svaip.setText(_translate("task", "Пропустить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    task = QtWidgets.QWidget()
    ui = Ui_tasks()
    ui.setupUi(task)
    task.show()
    sys.exit(app.exec_())
