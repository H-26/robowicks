import random
import time
from playsound import playsound
excersise = ''
excersise1 = ''
excersise2 = ''
excersise3 = ''
excersise4 = ''
excersise5 = ''
excersises = int(0)
excersiseTypes = []
validExcersiseTypes = ["1", "2", "3", "4", "5"]
validExcersiseType = False
excersiseAmount = int(input("How many excersisies do you want to do?  "))
Breaks = int(input("How long do you want your breaks (seconds)?  "))
Work = int(input("How long do you want your work (seconds)?  "))

while validExcersiseType == False:
    excersiseType = str(input("Which parts of the body do you want to excersise? (type the numbers you want, you can select multiple)\nFull body: 1\nLegs: 2\nChest and back: 3\nSholders and arms: 4\nCore: 5\n"))
    if '1' in excersiseType:
        excersiseTypes.append(0)
    if '2' in excersiseType:
        excersiseTypes.append(1)
    if '3' in excersiseType:
        excersiseTypes.append(2)
    if '4' in excersiseType:
        excersiseTypes.append(3)
    if '5' in excersiseType:
        excersiseTypes.append(4)
    for item in validExcersiseTypes:
        if item in excersiseType:
            validExcersiseType = True       

#FullBody
exersiseFullBody = ["Inchworm", "Bear crawl", "Mountain climbers", "Burpee","Tuck jump", "Star jumps", "Squat jumps","Plank", "Progressive/up-down Plank", "Side plank"]
#Legs
exersiseLegs = ["Wall sit", "Step-up", "Lunge", "Lunge jump", "Reverse Lunge", "Curtsy lunge", "Squats", "Squat Hold", "Squat Pulse"]
#Chest and back
excersiseChestBack = ["Superman", "Push-up", "Clap push-up", "Tight push-up", "Rotational push-up"]
#Sholders and arms
excersiseSholderArm = ["Boxing", "Arm circles"]
#Core
excersiseCore = ["Bycicle crunch", "Crunch/sit-up", "Single leg crunch","Double leg raises", "Single leg raises"]

ExcersiseTypeConverter = [exersiseFullBody, exersiseLegs, excersiseChestBack, excersiseSholderArm, excersiseCore]


while excersiseAmount != 0:
    
    #Saves and updates past excersises to check that there are no repeats
    excersise5 = excersise4
    excersise4 = excersise3
    excersise3 = excersise2
    excersise2 = excersise1
    excersise1 = excersise

    #chooses the excersise 
    excersiseTypeNumber = random.choice(excersiseTypes)

    excersiseType = ExcersiseTypeConverter[excersiseTypeNumber]

    excersise = excersiseType[random.randint(0,(len(excersiseType)-1))]
    
    #Checks if there are any repeats and re-chooses the excersise if there are
    while excersise in {excersise1, excersise2, excersise3, excersise4, excersise5}:
        excersise = excersiseType[random.randint(0,(len(excersiseType)-1))]

    #Prints the next excerise
    if excersises == 0:
        #Special first excerise message
        print("Let's start! The first one is the " + excersise +"!")
    elif excersiseAmount == excersises:
        print("You're halfway there! Next up is the " + excersise +"!")
    else:
        #Normal message
        print("Next up is the " + excersise + "!")
    
    time.sleep(Breaks)
    print("Go Go Go!")
    playsound('beep-01a.mp3')
    
    excersiseAmount = excersiseAmount - 1
    excersises = excersises + 1

    time.sleep(Work)

    if excersiseAmount != 0:
        print("Break!")
        playsound('beep-01a.mp3')
    else:
        print("And you are Done!")
        playsound('beep-01a.mp3')
        time.sleep(0.2)
        playsound('beep-01a.mp3')
        time.sleep(0.2)
        playsound('beep-01a.mp3')
