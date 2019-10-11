'''
    Authors: Chandler Mitchell, Evan Mele
    Date Last Modified: 4/18/19

    CSCI250 Capstone

    analytics.py---Defines methods used for data analytics
'''
import numpy as np
import graph

# Takes in a np array and smooths the values
def smoothData(arr, smoothFactor = 100):
    smooth = np.array(arr)
    for i in range(arr.size):
        if i > smoothFactor - 1 and i < arr.size - smoothFactor:
            valSum = 0
            for j in range(-smoothFactor, smoothFactor):
                valSum = valSum + arr.item(j + i)
            smooth[i] = valSum / (2 * smoothFactor + 1)
        elif i < smoothFactor:
            valSum = 0
            for j in range(0, i + smoothFactor):
                valSum = valSum + arr.item(j)
            smooth[i] = valSum / (smoothFactor + i + 1)
        else:
            valSum = 0
            for j in range(i - smoothFactor, arr.size):
                valSum = valSum + arr.item(j)
            smooth[i] = valSum / (smoothFactor + arr.size - i + 1)
    return smooth

#Prints basic statistics for data from the mic
def generalMicData(audio, envelope):
    print("Audio General Statistics---------")
    print("mean: ", np.mean(audio))
    print("sd: ", np.std(audio))
    print("max: ", np.amax(audio))
    print("min: ", np.amin(audio))
    print("Envelope General Statistics---------")
    print("mean: ", np.mean(envelope))
    print("sd: ", np.std(envelope))
    print("max: ", np.amax(envelope))
    print("min: ", np.amin(envelope))

#Prints basic statistics for data from the jack
def generalJackData(left, right):
    print("Left General Statistics---------")
    print("mean: ", np.mean(left))
    print("sd: ", np.std(left))
    print("max: ", np.amax(left))
    print("min: ", np.amin(left))
    print("Right General Statistics---------")
    print("mean: ", np.mean(right))
    print("sd: ", np.std(right))
    print("max: ", np.amax(right))
    print("min: ", np.amin(right))
    
#returns % of time left is louder
def leftLouder(left, right):
    smaller = min(left.size, right.size)
    leftLoud = 0
    for i in range(smaller):
        if left[i] > right[i]:
            leftLoud = leftLoud + 1
    return (leftLoud / smaller * 100)

#returns % time right is louder
def rightLouder(left, right):
    return(100 - leftLouder(left, right))

#returns % time left is louder
def leftMinusRight(left, right):
    difference = np.absolute(left - right)
    return difference

def abs(arr):
    return (np.absolute(arr))
''' TESTING--------------------------------
arr = np.load("arr.txt.npy")
print(arr.size)
smooth = np.array(smoothData(arr, 100))
time = arr.size
print(arr)
print()
print(smooth)
smoothTest = "smoothTest.png"
graph.plotJack(arr, smooth, time, smoothTest)
'''

