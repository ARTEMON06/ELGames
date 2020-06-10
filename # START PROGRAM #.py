# START PROGRAM #
# This program start with logic_Menu
import subprocess as sub
from resurse_lib import Resurse
import datetime
import os

now = datetime.datetime.now()

now_hour = int(now.hour)
now_minutes = int(now.minute)

if int(Resurse("start").read()) == 1:
	hour_2 = int(Resurse("realmin").read())
	min_2 = int(Resurse("realhour").read())
	t_h = hour_2 + int(Resurse("hour_2").read)
	t_m = min_2 + int(Resurse("min_2").read)
	if t_m > 59:
    	t_h + 1
	if t_m < now_minutes:
    		if t_h <= now_hour:
    			minutes = Resurse("min").read()
				hour = Resurse("hour").read()

				hour_over = now_hour + int(hour)
				minutes_over = now_minutes + int(minutes)

				sub.Popen(["python.exe", "logic_Menu.py"])

				while True:
					v = datetime.datetime.now()

					if minutes_over > 59:
						minutes_over = minutes_over - 60
						hour_over = hour_over + 1

					if hour_over > 24:
						hour_over = 0

					if hour_over == int(v.hour) and minutes_over == int(v.minute):
						break

				Resurse("realmin").write(v.minute)
				Resurse("realhour").write(v.hour)

				if int(Resurse("start").read()) == 0:
					Resurse("start").write(1)

				

sub.Popen(["python.exe", "init_end.py"])
os.system("TASKKILL /F /FI \"WINDOWTITLE eq Form*\"")			



