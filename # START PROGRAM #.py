# START PROGRAM #
# This program start with logic_Menu
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

while True:
	v = datetime.datetime.now()

	if minutes_over > 59:
		minutes_over = minutes_over - 60
		hour_over = hour_over + 1

	if hour_over > 24:
		hour_over = 0

	if hour_over == int(v.hour) and minutes_over == int(v.minute):
		break

sub.Popen(["python.exe", "init_end.py"])
os.system("TASKKILL /F /FI \"WINDOWTITLE eq Form*\"")			



