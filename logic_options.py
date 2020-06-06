from PyQt5 import QtWidgets, QtGui
from init_options import Ui_options
from resurse_lib import Resurse
import subprocess as sub
import sys

class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow,self).__init__()
		self.ui = Ui_options()
		self.ui.setupUi(self)
		self.bal = int(Resurse("баллы").read())
		self.maxnum = int(Resurse("слайдер").read()) if int(Resurse("слайдер").read()) > 1 else 2
		self.zn = int(Resurse("умножение").read())
		self.ui.horizontalSlider.setValue(self.maxnum)
		self.ui.label.setText(f"  Выбери до скольки ты умеешь считать: {self.maxnum}")
		self.ui.home.clicked.connect(self.home)
		self.ui.horizontalSlider.valueChanged[int].connect(self.val)
		self.ui.svaip.clicked.connect(self.svaip)
		self.ui.checkBox.stateChanged.connect(self.cb)
		self.ui.checkBox.setChecked(self.zn)
		self.ui.control.clicked.connect(self.control)
		self.ui.comboBox.activated.connect(self.theme)
		if Resurse("theme").read() == "css.txt":
			self.ui.comboBox.setCurrentIndex(0)
		if Resurse("theme").read() == "css_dark.txt":
			self.ui.comboBox.setCurrentIndex(1)
		if Resurse("theme").read() == "css_pink.txt":
			self.ui.comboBox.setCurrentIndex(2)
		if Resurse("theme").read() == "css_brow.txt":
			self.ui.comboBox.setCurrentIndex(3)
		if Resurse("theme").read() == "css_style.txt":
			self.ui.comboBox.setCurrentIndex(4)
		# if Resurse("обнулить").read() == "1":
		# 	self.obnul()

		self.ui.svaip_2.setToolTip("Нажимая на эту кнопку, ты можешь посмотреть все свои <b>достижения!</b>")
		self.ui.checkBox.setToolTip("Поставь здесь галочку, если ты умеешь <b>делить и умножать!</b>")
		self.ui.svaip.setToolTip("Нажимая на эту кнопку, ты обнуляешь все свои <b>достижения и баллы!</b>")
		self.ui.control.setToolTip("Настройка <b>родительского контроля!</b>")

	def theme(self, text): 
		if text == 1:
			Resurse("theme").write("css_dark.txt")
			Resurse("logo").write("Ресурс/logo_fin_black.png")
			Resurse("heart").write("Ресурс/heart_black.png")
			Resurse("option").write("Ресурс/opt_ic_black.png")
			sub.Popen(["python.exe", "logic_options.py"])
			sys.exit()
			

		if text == 2:
			Resurse("theme").write("css_pink.txt")
			Resurse("logo").write("Ресурс/logo_pink.png")
			Resurse("heart").write("Ресурс/heart_pink")
			Resurse("option").write("Ресурс/opt_pink.png")
			sub.Popen(["python.exe", "logic_options.py"])
			sys.exit()

		if text == 4:
			Resurse("theme").write("css_style.txt")
			Resurse("logo").write("Ресурс/logo_fin.png")
			Resurse("heart").write("Ресурс/heart_style.png")
			Resurse("option").write("Ресурс/opt_ic.png")
			sub.Popen(["python.exe", "logic_options.py"])
			sys.exit()

		if text == 3:
			Resurse("theme").write("css_brow.txt")
			Resurse("logo").write("Ресурс/logo_fin_brow.png")
			Resurse("heart").write("Ресурс/heart_brow.png")
			Resurse("option").write("Ресурс/opt_ic_brow.png")
			sub.Popen(["python.exe", "logic_options.py"])
			sys.exit()

		if text == 0:
			Resurse("theme").write("css.txt")
			Resurse("logo").write("Ресурс/logo_fin.png")
			Resurse("heart").write("Ресурс/Serdtse-s-chernoj-okantovkoj-narisovannoe.png")
			Resurse("option").write("Ресурс/opt_ic.png")
			sub.Popen(["python.exe", "logic_options.py"])
			sys.exit()
			
	def control(self):
		password = int(Resurse("password").read())
		if password:
			sub.Popen(["python.exe", "logic_control_pass_give.py"])
			sys.exit()
		else:
			sub.Popen(["python.exe", "logic_control_pass_take.py"])
			sys.exit()

	# def obnul(self):
    # 		Resurse("баллы").write(0)
	# 	self.ui.bals.setText(str(Resurse("баллы").read()))
	# 	Resurse("обнулить").write(0)

	def svaip(self):
		sub.Popen(["python.exe", "logic_check.py"])
		sys.exit()

	def home(self):
		home = Resurse("настройки")
		path = home.read()
		sub.Popen(["python.exe", path + ".py"])
		sys.exit()

	def val(self, value):
		"""
		Переменная self.maxnum = slider.
		Значения от 2 до 100.
		"""
		#print(value)
		self.maxnum = value
		self.ui.label.setText(f"  Выбери до скольки ты умеешь считать: {self.maxnum}")
		self.resurse_init()

	def cb(self, state):
		"""
		Переменная self.zn = checkbox.
		Значения 0 - не нажата, 1 - нажата.
		"""
		if state == 0:
		    self.zn = 0
		else:
		    self.zn = 1
		self.resurse_init()

	def resurse_init(self):
		bal = Resurse("баллы")
		bal.write(self.bal)
		maxnum = Resurse("слайдер")
		maxnum.write(self.maxnum)
		zn = Resurse("умножение")
		zn.write(self.zn)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
