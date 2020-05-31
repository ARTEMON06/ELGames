# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_options.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from resurse_lib import Resurse


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_options(object):
    def setupUi(self, options):
        options.setObjectName("options")
        options.resize(793, 389)
        with open(Resurse("theme").read(), "r") as file:
            text = file.read()
            options.setStyleSheet(text)
        self.checkBox = QtWidgets.QCheckBox(options)
        self.checkBox.setGeometry(QtCore.QRect(430, 160, 341, 31))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(options)
        self.label.setGeometry(QtCore.QRect(30, 230, 400, 31))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        if Resurse("theme").read() == "css_dark.txt":
            self.label.setStyleSheet("background-color: none;\nborder: none;")
        self.horizontalSlider = QtWidgets.QSlider(options)
        self.horizontalSlider.setGeometry(QtCore.QRect(430, 230, 341, 31))
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.svaip = QtWidgets.QPushButton(options)
        self.svaip.setGeometry(QtCore.QRect(30, 300, 341, 31))
        self.svaip.setObjectName("svaip")
        self.home = QtWidgets.QPushButton(options)
        self.home.setGeometry(QtCore.QRect(690, 350, 91, 31))
        self.home.setObjectName("home")
        self.svaip_2 = QtWidgets.QPushButton(options)
        self.svaip_2.setGeometry(QtCore.QRect(30, 160, 341, 31))
        self.svaip_2.setObjectName("svaip_2")
        self.control = QtWidgets.QPushButton(options)
        self.control.setGeometry(QtCore.QRect(430, 300, 341, 31))
        self.control.setObjectName("control")
        self.comboBox = QtWidgets.QComboBox(options)
        self.comboBox.setGeometry(QtCore.QRect(30, 90, 341, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Синяя тема", "Темная тема", "Розовая тема", "Коричневая тема", "Стильная тема"])
        

        self.retranslateUi(options)
        QtCore.QMetaObject.connectSlotsByName(options)

    def retranslateUi(self, options):
        _translate = QtCore.QCoreApplication.translate
        options.setWindowTitle(_translate("options", "Form"))
        self.checkBox.setText(_translate("options", "Ты умеешь делить и умножать?"))
        self.label.setText(_translate("options", "  Выбери до скольки ты умеешь считать: "))
        self.svaip.setText(_translate("options", "Сброс достижений и баллов"))
        self.home.setText(_translate("options", "назад"))
        self.svaip_2.setText(_translate("options", "Мои достижения!"))
        self.control.setText(_translate("options", "Родительский контроль"))
        
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    options = QtWidgets.QWidget()
    ui = Ui_options()
    ui.setupUi(options)
    options.show()
    sys.exit(app.exec_())
