'''
    Authors: Chandler Mitchell, Evan Mele
    Date Last Modified: 4/18/19

    CSCI250 Capstone

    delay.py---Defines helper methods used for time delay
'''

import datetime

def getDelay(sec):
    return datetime.timedelta(0, sec)

def getEnd(sec):
    now = getNow()
    delay = getDelay(sec)
    end = now + delay
    return end

def getNow():
    return datetime.datetime.now()
