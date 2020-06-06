from PyQt5 import QtWidgets, QtGui
from init_mystery import Ui_mystery
from PyQt5.QtCore import QTimer
from resurse_lib import Resurse
import subprocess as sub
import os
import sys

class mystery(QtWidgets.QMainWindow):

    def __init__(self):
        super(mystery, self).__init__()
        self.ui = Ui_mystery()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.option)
        self.ui.otvet.returnPressed.connect(self.proverka)
        self.ui.ask.clicked.connect(self.proverka)
        self.ui.home.clicked.connect(self.home)
        self.ui.svaip.clicked.connect(self.reb)
        self.ui.lol.clicked.connect(self.lol)
        self.ui.otvet.returnPressed.connect(self.proverka)
        self.ui.otvet.setFocus()
        self.lolch = True
        self.reb()
        self.heart()

    def lol(self):
        self.rez = Resurse(self.num, "keys_mystery").read()
        self.ui.otvet.setText(self.rez)
        self.lolch = False

    #TODO: this code need for fast fixid a very bad bug, you mast check self.rez, why it has type - str with \n, it most not be, what a fuk man!?

    def proverka(self):
        self.rez = Resurse(self.num, "keys_mystery").read()
        print(self.rez)
        text = self.ui.otvet.text().lower()
        if self.rez == text:
            if self.lolch:
                Resurse("баллы").write(str(int(self.bal) + 1))
            else:
                self.lolch = True
            self.rezult_color(0)
            QTimer.singleShot(1000, lambda: self.rezult_color(2))
            self.heart()
            self.reb()
            self.num = int(self.num) + 1
            Resurse("mystery").write(self.num)
        else:
            self.rezult_color(1)
            QTimer.singleShot(1000, lambda: self.rezult_color(2))
        self.ui.otvet.clear()

    def rezult_color(self, color):
        if color == 0:
            self.ui.red.setVisible(0)
            self.ui.green.setVisible(1)
            self.ui.red1.setVisible(0)
            self.ui.green1.setVisible(1)
        if color == 1:
            self.ui.green.setVisible(0)
            self.ui.red.setVisible(1)
            self.ui.green1.setVisible(0)
            self.ui.red1.setVisible(1)
        if color == 2:
            self.ui.green.setVisible(0)
            self.ui.red.setVisible(0)
            self.ui.green1.setVisible(0)
            self.ui.red1.setVisible(0)

    def reb(self):
        self.ui.otvet.clear()
        self.num = Resurse("mystery").read()
        if self.num == "28":
            self.num = "0"
        with open("resurse_mystery.txt", "r", encoding="utf-8") as file:
            text = file.readlines()[int(self.num)]
            self.ui.reb.setText(text)
        

    def home(self):
        sub.Popen(["python.exe", "logic_Menu_mystery.py"])
        sys.exit()

    def heart(self):
        self.bal = Resurse("баллы").read()
        self.ui.bals.setText(self.bal)

    def option(self):
        opt = Resurse("настройки")
        opt.write("logic_mystery")
        sub.Popen(["python.exe", "logic_options.py"])
        sys.exit()

app = QtWidgets.QApplication([])
application = mystery()
application.show()
sys.exit(app.exec())