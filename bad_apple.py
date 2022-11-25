#!/usr/bin/python
from os import system as cmd
from os import listdir
from os import name
from time import sleep, time
from platform import system

#Variables
PATH_TO_FRAMES = "ascii/"
TARGET_FRAMERATE = 30
SYSTEM_TYPE = system()

#Delta
last_time = time()
frametime = 1/TARGET_FRAMERATE

#get Frames
frames = listdir(PATH_TO_FRAMES)

for x in frames:
    #calculate delta
    delta = time() - last_time
    last_time = time()

    #clear screen
    if SYSTEM_TYPE == "Windows":
        cmd("cls")
    else:
        cmd(f"clear ; cat {PATH_TO_FRAMES}{x}") #clear for Linux (bash)

    #print file content
    file = open(f"{PATH_TO_FRAMES}{x}")
    print(file.read())

    #wait (to get stable framerate)
    waittime = float(frametime - delta)
    if waittime < 0:
        waittime = float(frametime)
    sleep(waittime)