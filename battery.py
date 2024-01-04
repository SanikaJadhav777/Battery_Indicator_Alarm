import psutil
from playsound import playsound
import time
import sys

def convertTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return "%d:%02d:%02d" % (hours, minutes, seconds)

while(True):
	battery = psutil.sensors_battery()
	#print("Battery percentage : ", battery.percent)
	#print("Power plugged in : ", battery.power_plugged)
	if battery.percent==100 and battery.power_plugged :
		while battery.power_plugged :
			battery = psutil.sensors_battery()
			playsound('remove_plug.mp3')
			time.sleep(2)
			print("Please remove the charger...!")
		else: 
			print("Plug removed ! ")
			#sys.exit(0)
	if battery.percent==100 :
		playsound('battery_full.mp3')
		sys.exit(0)
	if battery.percent<=20 :
		playsound('battery_low.mp3')
		sys.exit(0)
	else :
		sys.exit(0)
	
print("Battery left : ", convertTime(battery.secsleft))
