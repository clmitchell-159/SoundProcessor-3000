'''
    Authors: Chandler Mitchell, Evan Mele
    Date Last Modified: 4/18/19

    CSCI250 Capstone

    menus.py---Holds functionality for printing menus
'''

# Prints main menu options for user
def printMainMenu():
    print("Please Select an Option\n")
    print("1: Collect Data")
    print("2: Read Data From File")
    print("3: Save/Display Data")
    print("4: View Statistics")

# Prints Sensor menu options for user
def printSensorMenu():
    print("Please Select a Sensor\n")
    print("1: Microphone")
    print("2: Audio Jack")
    print("3: Previous Menu")

# Prints Save/Display Data menu options for user
def printSaveDisplayMenu():
    print("Please Select an Option\n")
    print("1: Display Data")
    print("2: Save Data to File")
    print("3: Previous Menu")

# Prints Sampling menu options for user
def printSamplingMenu():
    print("Please Select an Option\n")
    print("1: Time")
    print("2: While Button Pressed")
    print("3: Button Start/Stop")
    print("4: Previous Menu")

# Prints Save Data menu options for user
def printSaveMenu():
    print("Please Select Data to Save\n")
    print("1: Microphone Data")
    print("2: Audio Jack Data")
    print("3: Previous Menu")

# Prints Analytics Data menu options for user
def printAnalyticsMenu():
    print("Please Select an Option\n")
    print("1: General Statistics")
    print("2: Dominating Signal Percentages (Audio Jack Only)")
    print("3: Previous Menu")

# Prints Graph Data menu options for user
def printGraphMenu():
    print("Please Select Data to Graph\n")
    print("1: Graph Microphone Data")
    print("2: Graph Audio Jack Data")
    print("3: Graph Smoothed Microphone Data")
    print("4: Graph Smoothed Audio Jack Data")
    print("5: Graph Left Channel Minus Right Channel")
    print("6: Previous Menu")
