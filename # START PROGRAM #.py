# START PROGRAM #
import subprocess as sub
from resurse_lib import Resurse
import datetime
import os

now = datetime.datetime.now()

now_hour = int(now.hour)
now_minutes = int(now.minute)

minutes = Resurse("min").read()
hour = Resurse("hour").read()

hour_over = now_hour + int(hour)
minutes_over = now_minutes + int(minutes)

# sub.Popen(["python.exe", "logic_Menu.py"])


while True:
	now = datetime.datetime.now()

	if minutes_over > 59:
		minutes_over = minutes_over - 60
		hour_over = hour_over + 1

	if hour_over > 24:
		hour_over = 0

	print(f"{str(hour_over)}   {str(minutes_over)}      {now.hour}  {now.minute}")

	if hour_over == int(now.hour) and minutes_over == int(now.minute):
		break

os.system("TASKKILL /F /FI \"WINDOWTITLE eq Form*\"")