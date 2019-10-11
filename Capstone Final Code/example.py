import numpy as np
import graph
import adcDevice
import gpiozero as gpz

button = gpz.Button(21)

data = adcDevice.readAdcButtonStartStop(button)

graph.plotMic(data[0], data[1], data[2], "mic.png")
graph.plotJack(data[0], data[1], data[2], "jack.png")
