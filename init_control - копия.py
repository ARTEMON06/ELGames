# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_control.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from resurse_lib import Resurse

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_control(object):
    def setupUi(self, control):
        control.setObjectName("control")
        control.resize(671, 248)
        with open(Resurse("theme").read(), "r") as file:
            text = file.read()
            control.setStyleSheet(text)
        self.label = QtWidgets.QLabel(control)
        self.label.setGeometry(QtCore.QRect(0, 20, 671, 61))
        self.label.setStyleSheet("background-color: none;\n"
"font: 75 22pt \"Calibri\";\nborder: none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(control)
        self.label_2.setGeometry(QtCore.QRect(340, 110, 311, 71))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.home = QtWidgets.QPushButton(control)
        self.home.setGeometry(QtCore.QRect(560, 210, 101, 31))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    control = QtWidgets.QWidget()
    ui = Ui_control()
    ui.setupUi(control)
    control.show()
    sys.exit(app.exec_())
