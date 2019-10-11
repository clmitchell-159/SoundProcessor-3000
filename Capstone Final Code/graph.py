'''
    Authors: Chandler Mitchell, Evan Mele
    Date Last Modified: 4/18/19

    CSCI250 Capstone

    graph.py---Holds functionality for graphing numpy arrays
'''

import numpy as np
import matplotlib.pyplot as plt

# Plots the two numpy arrays on separate figures and saves to a file
def plotGeneric(audio, envelope, time, filename, titles, x, y):
    linethick = .2
    audioX = np.linspace(0, time, audio.size)
    envelopeX = np.linspace(0, time, envelope.size)

    plt.figure(0).subplots_adjust(hspace=.5)
    plt.figure(0).set_size_inches(11, 8.5)
    
    plt.subplot(2, 1, 1)
    plt.plot(audioX, audio, 'b', linewidth=linethick)
    plt.grid(True)
    plt.title(titles[0])
    plt.xlabel(x[0])
    plt.ylabel(y[0])
    
    plt.subplot(2, 1, 2)
    plt.plot(envelopeX, envelope, 'g', linewidth=linethick)
    plt.grid(True)
    plt.title(titles[1])
    plt.xlabel(x[1])
    plt.ylabel(y[1])
    plt.subplot(2, 1, 2)
    plt.savefig(filename, dpi=300)
    plt.clf()

# Creates labels and titles for mic graph and calls plotting function
def plotMic(audio, envelope, time, filename):
    titles = ["Audio", "Envelope"]
    xLabels = ["Time (s)", "Time (s)"]
    yLabels = ["Microphone (V)", "Envelope (V)"]
    plotGeneric(audio, envelope, time, filename, titles, xLabels, yLabels)

# Creates labels and titles for jack graph and calls plotting function
def plotJack(left, right, time, filename):
    titles = ["Left Channel", "Right Channel"]
    xLabels = ["Time (s)", "Time (s)"]
    yLabels = ["Left Channel (V)", "Right Channel (V)"]
    plotGeneric(left, right, time, filename, titles, xLabels, yLabels)
