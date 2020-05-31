

import subprocess as sub

from resurse_lib import Resurse

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_check(object):
	def setupUi(self, check):
		check.setObjectName("check")
		check.resize(402, 228)
		with open(Resurse("theme").read(), "r") as file:
			text = file.read()
			check.setStyleSheet(text)
		self.verticalLayoutWidget = QtWidgets.QWidget(check)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 381, 201))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setWordWrap(True)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.yes = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.yes.setObjectName("yes")
		self.horizontalLayout.addWidget(self.yes)
		self.no = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.no.setObjectName("no")
		self.horizontalLayout.addWidget(self.no)
		self.verticalLayout.addLayout(self.horizontalLayout)

		self.retranslateUi(check)
		QtCore.QMetaObject.connectSlotsByName(check)

	def retranslateUi(self, check):
		_translate = QtCore.QCoreApplication.translate
		check.setWindowTitle(_translate("check", "Form"))
		self.label.setText(_translate("check", "Твои баллы и достижения исчезнут. Ты уверен?"))
		self.yes.setText(_translate("check", "Да"))
		self.no.setText(_translate("check", "Нет"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    check_ = QtWidgets.QWidget()
    ui = Ui_check()
    ui.setupUi(check_)
    check_.show()
    sys.exit(app.exec_())

