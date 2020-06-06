from PyQt5 import QtWidgets, QtGui
from init_calc import Ui_calc
from PyQt5.QtCore import QRect, QTimer
from resurse_lib import Resurse
import subprocess as sub
import sys
import random as r
import time 

# this good code
class mywindow(QtWidgets.QMainWindow):
    """Класс запускающий окно с примерами."""
    def __init__(self):
        """
        Родители класса - QMainWindow.
        self.ui.svaip.clicked.connect(self.primer)--------------------|Кнопка пропуска привязаннна к методу primer()
        self.ui.ask.clicked.connect(self.proverka)--------------------|Кнопка ОТВЕТИТЬ! привязаннна к методу proverka()
        self.ui.horizontalSlider.setValue(self.maxnum)----------------|Начальное положение Slider = muxnum(по умол. 10)
        self.ui.horizontalSlider.valueChanged[int].connect(self.val)--|Значения слайдера привязанны к методу val()
        self.ui.otvet.returnPressed.connect(self.proverka)------------|Кнопка на клавиатуре Enter привязанна к методу proverka()
        self.ui.checkBox.stateChanged.connect(self.cb)----------------|Значения с CheckBox  привязанны к методу cb()
        self.ui.otvet.setFocus()--------------------------------------|По умолчанию каретка стотит на поле ответа
        """
        super(mywindow, self).__init__()
        self.bal = int(Resurse("баллы").read())
        self.maxnum = int(Resurse("слайдер").read()) if int(Resurse("слайдер").read()) > 1 else 2
        self.zn = int(Resurse("умножение").read())
        self.ui = Ui_calc()
        self.ui.setupUi(self)
        self.ui.home.clicked.connect(self.home)
        self.ui.svaip.clicked.connect(self.svaip)
        self.ui.pushButton.clicked.connect(self.option)
        self.ui.lol.clicked.connect(self.lol)
        self.ui.ask.clicked.connect(self.proverka)
        self.ui.otvet.returnPressed.connect(self.proverka)
        self.ui.otvet.setFocus()
        self.lolch = False
        self.save = 0
        self.hert()
        self.primer() # первый запуск primer()

    def svaip(self):
        if self.save < 30 and self.save != -5:
            self.save = self.save + 1
            self.primer()
        else:
            if Resurse("пасхалка").read() == "0":
                Resurse("пасхалка").write(1)
                self.save_fun()       
            else:
                print("none")
                self.save = 0
                self.primer()
            
        print(self.save)


    def home(self):
        sub.Popen(["python.exe", "logic_Menu.py"])
        sys.exit()

    def option(self):
        opt = Resurse("настройки")
        opt.write("logic_calc")
        sub.Popen(["python.exe", "logic_options.py"])
        sys.exit()

    def lol(self):
        self.lolch = True
        self.ui.otvet.setText(self.rez)

    def rand(self):
        self.num1 = r.randint(1,self.maxnum)
        self.num2 = r.randint(1,self.maxnum)

    def primer(self):
        """
        Метод создания примера.
        self.ui.quest.setText(txt) печатает пример в строчку с примером.
        Создает переменную self.rez = результат выражения.
        """
        self.lolch = False
        self.ui.otvet.clear()
        self.rand()
        znak = 0
        if self.zn:
            znak = r.randint(1,4)
        else:
            znak = r.randint(1,2) 

        #print(znak)

        if znak == 1:
            while True:
                if self.num1+self.num2 <= self.maxnum:
                    break
                else:
                    self.rand()     
            #print(f"{num1} + {num2}")
            self.rez = str(self.num1+self.num2)
            self.txt = f"    {self.num1} + {self.num2}"

        if znak == 2:
            while True:
                if self.num1 >= self.num2:
                    break
                else:
                    self.rand()
            #print(f"{num1} - {num2}")
            self.rez = str(self.num1-self.num2)
            self.txt = f"    {self.num1} - {self.num2}"

        if znak == 3:
            while True:
                if self.num1*self.num2 <= self.maxnum:
                    break
                else:
                    self.rand()
            self.rez = str(self.num1*self.num2)
            self.txt = f"    {self.num1} * {self.num2}"
            #print(f"{num1} * {num2}")

        if znak == 4:
            while True:
                if (self.num1/self.num2).is_integer() and self.num1>self.num2 and self.num2 != 0:
                    break
                else:
                    self.rand()
            #print(f"{num1} / {num2}")
            self.rez = str(self.num1//self.num2)
            self.txt = f"    {self.num1} / {self.num2}"

        self.ui.quest.setText(self.txt)

    def hert(self):
        """
        Метод вывод кол-во сердечек(аргумент self.bal).
        """
        #print(self.bal)
        
        # move_bal = len(str(self.bal))
        
        # self.ui.heart.setGeometry(QtCore.QRect(511, 10, 81, 81))
        self.ui.bals.setText(str(self.bal))

    def save_fun(self):
        self.rez = "нет"
        self.ui.quest.setText("Напиши \"да\" и ответь")
        self.save = -5
    
    def proverka(self):
        text = self.ui.otvet.text()
        """
        Метод отвечает за проверку данных введенных пользователем.
        Если результаты совпали меняется иконка на зеленый цвет, прибавляется 1 к self.bal, вызываются методы hert() и primer().
        Иначе иконка меняется на красный цвет и стераются данные, введенные пользователем.
        """
        

        if text == self.rez:
            if self.save == -5:
                self.save = 0
                print("tu t")
                self.ui.quest.setText("  Лови бонус - 50 ❤")
                self.bal = self.bal + 50
                self.resurse_init()
                self.hert()
                QTimer.singleShot(3000, lambda: self.primer())
            else:
                self.rezult_color(0)
                QTimer.singleShot(1000, lambda: self.rezult_color(2))
                self.bal = self.bal if self.lolch else self.bal + 1
                self.resurse_init()
                self.hert()
                self.primer()
        else:
            if self.save == -5:
                self.save = 0
                self.ui.otvet.clear()
                self.primer()
            else:
                self.rezult_color(1)
                QTimer.singleShot(1000, lambda: self.rezult_color(2))
                self.ui.otvet.clear()

    def rezult_color(self, rezult):
        css_colors = ["Ресурс/logo_fin_green.png","Ресурс/logo_fin_red.png"]
        if rezult == 0:
            self.ui.icon.setPixmap(QtGui.QPixmap(css_colors[0]))
            self.ui.label_3.setVisible(0)
            self.ui.true_l.setVisible(1)
        if rezult == 1:
            self.ui.icon.setPixmap(QtGui.QPixmap(css_colors[1]))
            self.ui.true_l.setVisible(0)
            self.ui.label_3.setVisible(1)
        if rezult == 2:
            self.ui.icon.setPixmap(QtGui.QPixmap(Resurse("logo").read()))
            self.ui.true_l.setVisible(0)
            self.ui.label_3.setVisible(0)

    def resurse_init(self):
        bal = Resurse("баллы")
        bal.write(self.bal)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())