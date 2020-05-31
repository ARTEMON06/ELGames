from PyQt5 import QtWidgets, QtGui
from init_tasks import Ui_tasks
from PyQt5.QtCore import QRect, QTimer
from resurse_lib import Resurse
import random as rand
import subprocess as sub
import os
import sys
import inspect


class tasks(QtWidgets.QMainWindow):

	def __init__(self):
		super(tasks, self).__init__()
		self.ui = Ui_tasks()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.option)
		self.ui.home.clicked.connect(self.home)
		self.ui.svaip.clicked.connect(self.task)
		self.ui.lol.clicked.connect(self.lol)
		self.ui.ask.clicked.connect(self.proverka)
		self.ui.task.setWordWrap(True)
		self.ui.otvet.setFocus()
		self.ui.otvet.returnPressed.connect(self.proverka)
		self.lolch = True
		self.s = 0
		self.last = "Вася"
		self.last_ob = "Журнала"
		self.maxnum = int(Resurse("слайдер").read())
		self.heart()
		self.task()

	def lol(self):
		self.ui.otvet.setText(str(self.rez))
		self.lolch = False

	def proverka(self):
		text = self.ui.otvet.text().lower()
		if str(self.rez) == text:
			if self.lolch:
				Resurse("баллы").write(
					str(int(self.bal) + int(Resurse("bal-task").read())))
			else:
				self.lolch = True
			self.rezult_color(0)
			QTimer.singleShot(1000, lambda: self.rezult_color(2))
			self.heart()
			self.task()
		else:
			self.rezult_color(1)
			QTimer.singleShot(1000, lambda: self.rezult_color(2))
		self.ui.otvet.clear()

	def task(self):
    	print("help")
		self.col1 = "0"
		self.col2 = "0"
		self.col3 = "0"
		self.ui.task.clear()
		level = int(Resurse("leveltask").read())

		def item(s, *index):
			index = rand.choice(index)

			if index == "food":
				self.ob1 = ["конфеты", "банана", "мороженых", "леденца", "яблока",
					   "йогурта", "эклера", "пироженых", "печенки", "конфетки", "жвачки"]
				self.ob2 = ["конфет", "бананов", "мороженых", "леденцов", "яблок",
					   "йогуртов", "эклеров", "пироженых", "печенек", "конфеток", "жвачек"]
				self.ob3 = ["конфета", "банан", "мороженое", "леденец", "яблоко",
					   "йогурт", "эклер", "пироженое", "печенье", "конфетка", "жвачка"]
			if index == "furn":
				pass
			if index == "small":
				self.ob1 = ["монеты", "карточки", "карандаша", "ручки", "ластика",
					   "листочка", "гайки", "болтика", "пуговицы", "журнала", "газеты", "книги"]
				self.ob2 = ["монет", "карточек", "карандашей", "ручек", "ластиков",
					   "листочков", "гаек", "болтиков", "пуговиц", "журналов", "газет", "книг"]
				self.ob3 = ["монета", "карточка", "карандаш", "ручка", "ластик",
					   "листочек", "гайка", "болтик", "пуговица", "журнал", "газета", "книга"]

				while True:
					self.poz = rand.randint(0, len(self.ob1) - 1)
					if self.ob1[self.poz] != self.last_ob:
						self.last_ob = self.poz
						break		

		def chelik():
			mans = ["Вася", "Роман", "Олег", "Виктор", "Дядя Петя", "Фёдор Семёнович",
					"Игнат", "Анна", "Жанна Петровна", "Маша", "Вера", "Света"]
			mans2 = ["Васи", "Ромы", "Олега", "Виктора", "Дяди Пети", "Фёдора Семёновича",
					"Игната", "Анны", "Жанны Петровны", "Машы", "Веры", "Светы"]

			while True:
				d = rand.randint(0, len(mans) - 1)
				self.chel = mans[d]
				self.chel2 = mans2[d]
				if self.chel != self.last:
					self.last = self.chel
					break
			self.gen = 0 if self.chel[-1] == "а" else 1
			self.gen2 = 0 if self.chel2[-1] == "а" else 1
 
		def ret(num):
			if int(str(num)[-1]) < 5 and int(str(num)[-1]) != 0:
				if num > 20:
					if int(str(num)[-1]) == 1:
						v = self.ob3[self.poz]
					else:
						v = self.ob1[self.poz]
				else:
					v = self.ob2[self.poz]
			else:
				v = self.ob2[self.poz]
			return v

		def in1():
			self.col1 = ret(self.num)
			self.col2 = ret(self.num2)
			self.col3 = self.ob2[self.poz]

		def one():
			chelik()
			sign = rand.choice(["+", "-"])
			while True:
				self.num = rand.randint(2, self.maxnum)
				self.num2 = rand.randint(2, self.maxnum)
				if sign == "+":
					if self.num + self.num2 <= self.maxnum:
						self.rez = self.num + self.num2
						break
				if sign == "-":
					if self.num - self.num2 > 0:
						self.rez = self.num - self.num2
						break

			if sign == "+":
				item(1, "small", "food")
				in1()
				if rand.randint(0, 1) == 1:
					dei1 = "купил" if self.gen else "купила"
					dei2 = "него" if self.gen else "неё"

					self.ui.task.setText(f"{self.chel} {dei1} в магазине {self.num} {self.col1}, а дома у {dei2} есть ещё {self.num2} {self.col2}.\nСколько всего {self.col3} имеет {self.chel}?")
				else:
					dei1 = "принёс" if self.gen else "принесла"
					dei2 = "его" if self.gen else "её"

					self.ui.task.setText(f"{self.chel} {dei1} {self.num} {self.col1}, а {dei2} друг принёс ещё {self.num2} {self.col2}.\nСколько всего {self.col3} они принесли?")
			if sign == "-":
				item(1, "small", "food")
				in1()
				if rand.randint(0, 1) == 1:
					dei1 = "он" if self.gen else "она"
					dei2 = "отдал" if self.gen else "отдала"
					self.ui.task.setText(f"У {self.chel} есть {self.num} {self.col1}, {self.num2} {self.col2} {dei1} {dei2} другу. Сколько теперь {self.col3} у {self.chel2}?")
				else:
					item(1, "food")
					in1()
					dei1 = "купил" if self.gen else "купила"
					dei2 = "он" if self.gen else "она"
					dei3 = "съел" if self.gen else "съела"
					self.ui.task.setText(f"{self.chel} {dei1} в магазине {self.num} {self.col1}, {self.num2} {self.col2} {dei2} {dei3}. Сколько теперь у него {self.col3}")

		def two():
			var = rand.randint(1, 8)
			while True:
				self.num1 = rand.randint(1, self.maxnum)
				self.num2 = rand.randint(1, self.maxnum)
				self.num3 = rand.randint(1, self.maxnum)
				if var == 1 or var == 5:
					if self.num1 + self.num2 + self.num3 <= self.maxnum:
						self.rez = self.num1 + self.num2 + self.num3
						break
				if var == 2 or var == 6:
					if self.num1 + self.num2 - self.num3 <= self.maxnum:
						self.rez = self.num1 + self.num2 - self.num3
						break
				if var == 3 or var == 7:
					if self.num1 - self.num2 + self.num3 <= self.maxnum:
						self.rez = self.num1 - self.num2 + self.num3
						break
				if var == 4 or var == 8:
					if self.num1 - self.num2 - self.num3 <= self.maxnum:
						self.rez = self.num1 - self.num2 - self.num3
						break

			if var == 1:
				dei1 = "положил" if self.gen else "положила"
				self.ui.task.setText(
					"На столе было {self.num1} {self.col1}, {self.chel} {dei1} ещё {self.num2} {self.col2}, а потом ещё {self.num1}.\nСколько всего {self.ob2[self.poz]} теперь на столе?")
			if var == 2:
				dei = "" if self.gen else ""
				self.ui.task.setText("")

		def three():
			pass

		if level < 10:
			one()
		elif level < 20:
			if rand.random():
				one()
			else:
				two()
		else:
			n = rand.ranint(0, 2)
			if n == 0:
				one()
			if n == 1:
				two()
			if n == 2:
				three()
		print(self.s)

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

	def home(self):
		sub.Popen(["python.exe", "logic_Menu.py"])
		sys.exit()

	def heart(self):
		self.bal = Resurse("баллы").read()
		self.ui.bals.setText(self.bal)

	def option(self):
		opt = Resurse("настройки")
		opt.write("logic_tasks")
		sub.Popen(["python.exe", "logic_options.py"])
		sys.exit()

app = QtWidgets.QApplication([])
application = tasks()
application.show()
sys.exit(app.exec())
