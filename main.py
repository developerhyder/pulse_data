import serial
import subprocess
import os
import matplotlib.pyplot as plt
import time

plt.ion()
# cmd = "python -m serial.tools.list_ports"
# stream = os.popen(cmd)
# output = stream.read()
# type python -m serial.tools.list_ports in the terminal to get the number of ports locate the port
# which is being used by the arduino

#print(output)

# this is the port number and the baudrate that you have initialised in the arduino code
var = "/dev/ttyACM2"

ser = serial.Serial(var, 115200)
ser.close()

lis1 = []
lis2 = []

ser.open()

#here we calculate the time since the plot has started
start_time = time.time()
while True:
    data = ser.readline()
    dat = data.decode().splitlines()
    print(dat[0].encode())
    if len(lis1) > 150:
        # we take 150 data points and then we refresh it
        lis1.clear()
        lis1.append(0)
        lis2.clear()
        lis2.append(0)
    lis1.append(int(dat[0]))
    stop_time = time.time()
    lis2.append(int(stop_time - start_time ))
    plt.title('Heart beat versus time')
    plt.style.use('ggplot')
    plt.xlabel('time')
    plt.ylabel('BPM')
    plt.plot(lis2,lis1)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()
