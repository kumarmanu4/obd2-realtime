import obd
import csv
import random
import time
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')



timeNow = time.time()
print('------OBD VEHICLE DATA LOGGER------')

count = 0

connection = obd.OBD()

while not connection.is_connected():
	print('...waiting for Connection...')
	time.sleep(1)

print('------CONNECTED TO OBD-II DEVICE')

timeNow = time.time()


fieldnames = ["instance", "speed", "rpm", "engine_load", "coolant_temp","throttle"]


with open('/home/kumarmanu4/obd_bluetooth_beat/data.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()


while True:
	time.sleep(1)
	count += 1
	rRPM = connection.query(obd.commands.RPM)
	rSPEED = connection.query(obd.commands.SPEED)
	rELOAD = connection.query(obd.commands.ENGINE_LOAD)
	rCoolantTemp = connection.query(obd.commands.COOLANT_TEMP)
	rThrottlePos = connection.query(obd.commands.THROTTLE_POS)
	
	with open('/home/kumarmanu4/obd_bluetooth_beat/data.csv', 'a') as csv_file:
	  csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			
	  info = {
			"instance": count,	
			"speed": rSPEED.value.magnitude,
			"rpm": rRPM.value.magnitude,
			"engine_load": rELOAD.value.magnitude,
			"coolant_temp": rCoolantTemp.value.magnitude,
			"throttle": rThrottlePos.value.magnitude
			}

	  csv_writer.writerow(info)
	print(count, str(rSPEED), str(rRPM), str(rELOAD),str(rCoolantTemp),str(rThrottlePos))

        


print("------DATA LOGGING ABORTED------")
				
