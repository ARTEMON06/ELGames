# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_control_pass_take.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from resurse_lib import Resurse

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_control_pass_take(object):
    def setupUi(self, control_pass_take):
        control_pass_take.setObjectName("control_pass_take")
        control_pass_take.resize(531, 240)
        with open(Resurse("theme").read(), "r") as file:
            text = file.read()
            control_pass_take.setStyleSheet(text)
        self.porol = QtWidgets.QLineEdit(control_pass_take)
        self.porol.setGeometry(QtCore.QRect(280, 110, 241, 41))
        self.porol.setObjectName("porol")
        self.label = QtWidgets.QLabel(control_pass_take)
        self.label.setGeometry(QtCore.QRect(10, 110, 241, 41))
        self.label.setObjectName("label")
        self.error = QtWidgets.QLabel(control_pass_take)
        self.error.setGeometry(QtCore.QRect(280, 40, 241, 61))
        self.error.setStyleSheet("background-color: none;\n"
"color: red;\nborder: none;")
        self.error.setScaledContents(False)
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setWordWrap(True)
        self.error.setObjectName("error")
        self.home = QtWidgets.QPushButton(control_pass_take)
        self.home.setGeometry(QtCore.QRect(10, 200, 91, 31))
        self.home.setObjectName("home")
        self.go = QtWidgets.QPushButton(control_pass_take)
        self.go.setGeometry(QtCore.QRect(280, 200, 231, 31))
        self.go.setObjectName("go")

        self.retranslateUi(control_pass_take)
        QtCore.QMetaObject.connectSlotsByName(control_pass_take)
        self.error.setVisible(False)

    def retranslateUi(self, control_pass_take):
        _translate = QtCore.QCoreApplication.translate
        control_pass_take.setWindowTitle(_translate("control_pass_take", "Form"))
        self.label.setText(_translate("control_pass_take", "Придумайте пароль:"))
        self.error.setText(_translate("control_pass_take", "Строка не должена быть пустой!"))
        self.home.setText(_translate("control_pass_take", "назад"))
        self.go.setText(_translate("control_pass_take", "Продолжить →"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    control_pass_take = QtWidgets.QWidget()
    ui = Ui_control_pass_take()
    ui.setupUi(control_pass_take)
    control_pass_take.show()
    sys.exit(app.exec_())
