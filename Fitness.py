import random
import time
from playsound import playsound

excersises = int(0)
excersiseAmount = int(input("How many excersisies do you want to do?  "))
Breaks = int(input("How long do you want your breaks (seconds)?  "))
Work = int(input("How long do you want your work (seconds)?  "))

#FullBody
exerciseFullBody = ["Inchworm", "Bear crawl", "Mountain climbers", "Burpee","Tuck jump", "Star jumps", "Squat jumps","Plank", "Progressive/up-down Plank", "Side plank"]
#Legs
exerciseLegs = ["Wall sit", "Step-up", "Lunge", "Lunge jump", "Reverse Lunge", "Curtsy lunge", "Squats", "Squat Hold", "Squat Pulse"]
#Chest and back
excersiseChestBack = ["Superman", "Push-up", "Clap push-up", "Tight push-up", "Rotational push-up"]
#Sholders and arms
excersiseSholderArm = ["Boxing", "Arm circles"]
#Core
excersiseCore = ["Bycicle crunch", "Crunch/sit-up", "Single leg crunch","Double leg raises", "Single leg raises"]

ExcersiseTypeConverter = [exerciseFullBody, exerciseLegs, excersiseChestBack, excersiseSholderArm, excersiseCore]


while excersiseAmount != 0:
    
    excersiseTypeNumber = random.randint(0,4)

    excersiseType = ExcersiseTypeConverter[excersiseTypeNumber]

    excersise = excersiseType[random.randint(0,(len(excersiseType)-1))]
    if excersises == 0:
        print("Let's start! The first one is the " + excersise +"!")
    else:
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
