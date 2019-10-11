'''
    Authors: Chandler Mitchell, Evan Mele
    Date Last Modified: 4/2/19

    CSCI250 Capstone

    fileIO.py---Implements fileIO functions
'''

import numpy as np

# Prompt user for a file name to pull data from
def readData():
    print("Please Enter a .npz File Name: ", end = "")
    userFile = str(input())
    return np.load(userFile)
    # TODO add file I/O code with exception handling

# Prompt user for a file name to save data to
def saveData(arrData1, arrData2, arrTime):
    print("Please Enter a Save File Name: ", end = "")
    userFileName = str(input())
    np.savez(userFileName, a = arrData1, b = arrData2, c = arrTime)
