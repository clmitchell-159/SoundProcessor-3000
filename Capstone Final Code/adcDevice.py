'''
    Authors: Chandler Mitchell, Evan Mele
    Date Last Modified: 4/18/19

    CSCI250 Capstone

    adcDevice.py---Holds adc class and sampling functions
'''

from spiUtils import readADC as readMic
import delay
import numpy as np
import gpiozero as gpz
import spidev

class adcDevice:
    def __init__(self, adcNum=0, button=None, sec=0):
        self.ADC = adcNum
        self.buttonObj = button
        self.time = sec
        self.ch1 = None
        self.ch2 = None
        
    #read adc once
    def readAdcOnce(self):
        data = [((readMic(adc=self.ADC)/1023)*3.3),(readMic(channel=1, adc=self.ADC)/1023)*3.3]
        return data

    #set button
    def setButton(self, button):
        self.buttonObj = button

    #set time
    def setTime(self, sec):
        self.time = sec

    #set ADC num
    def setAdc(self, adcNum):
        self.ADC = adcNum

    #set time
    def getTime(self):
        return self.time

    #return ch1
    def getCh1(self):
        return self.ch1

    #return ch2
    def getCh2(self):
        return self.ch2

    def returnFunch(self):
        return (self.ch1, self.ch2, self.time)
    
    #read adc for a number of seconds
    def readAdcSec(self):
        #setup
        spi = spidev.SpiDev()
        spi.open(0,self.ADC)
        spi.max_speed_hz = int(1e5)
        audio = np.zeros(1000000)
        envelope = np.zeros(1000000)
        i = 0

        #run
        end = delay.getEnd(self.time)
        while (end > delay.getNow()):
            #read ch0
            config = [0b01101000, 0]
            myBytes = spi.xfer2(config)
            myData0 = (myBytes[0] << 8) | myBytes[1]
            #read ch1
            config = [0b01111000, 0]
            myBytes = spi.xfer2(config)
            myData1 = (myBytes[0] << 8) | myBytes[1]
            #append to array
            audio[i] = myData0
            envelope[i] = myData1
            i = i+1

        #convert to voltage
        audio = np.trim_zeros(audio, trim='b')
        envelope = np.trim_zeros(envelope, trim='b')
        audio = audio/1023*3.3
        envelope = envelope/1023*3.3
        spi.close()
        self.ch1 = audio
        self.ch2 = envelope
        return (audio, envelope, self.time)

    #read adc while button is pressed
    def readAdcButtonContinuous(self):
        #setup
        spi = spidev.SpiDev()
        spi.open(0,self.ADC)
        spi.max_speed_hz = int(1e5)
        audio = np.array([])
        envelope = np.array([])

        #run
        self.buttonObj.wait_for_press()
        start = delay.getNow()
        while (self.buttonObj.is_pressed):
            #read ch0
            config = [0b01101000, 0]
            myBytes = spi.xfer2(config)
            myData0 = (myBytes[0] << 8) | myBytes[1]
            #read ch1
            config = [0b01111000, 0]
            myBytes = spi.xfer2(config)
            myData1 = (myBytes[0] << 8) | myBytes[1]
            #append to array
            audio = np.append(audio, myData0)
            envelope = np.append(envelope, myData1)

        #end
        end = delay.getNow()
        delta = end - start
        #convert to voltage
        audio = audio/1023*3.3
        envelope = envelope/1023*3.3
        spi.close()
        self.time = delta.total_seconds()
        self.ch1 = audio
        self.ch2 = envelope
        return (audio, envelope, delta.total_seconds())

    #read adc from button press to button press
    def readAdcButtonStartStop(self):
        #setup
        spi = spidev.SpiDev()
        spi.open(0,self.ADC)
        spi.max_speed_hz = int(1e5)
        audio = np.zeros(100)
        envelope = np.array([])

        self.buttonObj.wait_for_press()
        self.buttonObj.wait_for_release()
        start = delay.getNow()
        while (not (self.buttonObj.is_pressed)):
            #read ch0
            config = [0b01101000, 0]
            myBytes = spi.xfer2(config)
            myData0 = (myBytes[0] << 8) | myBytes[1]
            #read ch1
            config = [0b01111000, 0]
            myBytes = spi.xfer2(config)
            myData1 = (myBytes[0] << 8) | myBytes[1]
            #append to array
            audio = np.append(audio, myData0)
            envelope = np.append(envelope, myData1)

        #end
        end = delay.getNow()
        delta = end - start
        #convert to voltage
        audio = audio/1023*3.3
        envelope = envelope/1023*3.3
        spi.close()
        self.time = delta.total_seconds()
        self.ch1 = audio
        self.ch2 = envelope
        return (audio, envelope, delta.total_seconds())
