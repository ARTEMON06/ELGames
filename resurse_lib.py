"""
Модуль создан для хранения и перезаписи данных в виде файла txt.
Может создавать внутрефайловые переменные и присваивать им значение.

Объект класса принимает атрибуты: name, file и max_name.

Name - имя перменной, которая будет считываться или записываться
(создаст новую переменную в файле, если не найдет существующею с такием именем.

File - имя файла(по умолчанию file = "resurse").

Max_name - ьаксимальное кол-во символов в имени переменной(по умолчанию 40)

Модуль создаст фаил с расширением .txt в директории, где находится программа.
Пример файла можно посмотреть по ссылке: https://wampi.ru/image/6I6MHnZ

Примечание: внимание, каждый метод вызывать отдельно!
"""
import os
class Resurse():

	__version__ = '2.0'

	def __init__(self, name, file = "resurse", max_name = 40):
		
		self.max_name = max_name
		name = str(name)
		self.name = name + "-"*(self.max_name - len(name))
		self.file = file + ".txt"
		file = open(self.file, "a", encoding="utf-8")
		file.close()
		with open(self.file, "r", encoding="utf-8") as file:
			txt = [i[:self.max_name] for i in file.readlines()]
			self.have = 0
			self.position = 0
			for i in range(len(txt)):
				self.position = i
				if self.name == txt[i]:
					self.have = 1
					break

	def write(self, value):
		"""
		Метод записывает или перезаписывает значение переменной.

		Метод принимает аргумент value.

		Value - значение переменной в файле, принимает числа и строки.

		Примечание: возращает тип данных str!
		"""
		value = str(value)
		if self.have:
			with open(self.file, "r", encoding="utf-8") as file:
				txt = file.readlines()
				txt.pop(self.position)
				txt.append(f"{self.name+value}\n")
			with open(self.file, "w", encoding="utf-8") as file:
				file.writelines(txt)

		else:
			with open(self.file, "a", encoding="utf-8") as file:
				file.write(f"{self.name+value}\n")
				self.have = True
		self.read()

	def read(self):
		"""
		Метод считывает и возращает значение переменной в файле.

		Метод не принимает никаких аргументов

		Примечание: возращает тип данных str!
		"""
		if self.have:
			with open(self.file, "r", encoding="utf-8") as file:
				text = file.readlines()
				txt = [i[self.max_name:-1] for i in text]
				return txt[self.position]
		else:
			self.write(0)

if __name__ == "__main__":
	'''
	Объявляем обект number 1 c именем переменной - номер 1,
	именем файла - "Тест", 
	и максимальным кол-вом символов в названии - 20.
	'''
	number_1 = Resurse("номер 1", "Тест", 20)
	'''
	Применяем метод write(12)
	и присваиваем переменной значение 12.
	'''
	number_1.write(12)
	'''
	Принтуем метод read() и получаем значение переменной - 12
	'''
	print(number_1.read())