#!/usr/bin/python
from os import system as cmd
from os import listdir
from os import name
from time import sleep, time
from platform import system
import zipfile

#Variables
PATH_TO_FRAMES = "bad_apple.asv"
TARGET_FRAMERATE = 30
SYSTEM_TYPE = system()

#Delta
last_time = time()
frametime = 1/TARGET_FRAMERATE

#get Frames
frames_file = zipfile.ZipFile(PATH_TO_FRAMES, 'r')
List_Of_Files = frames_file.namelist()

for x in reversed(List_Of_Files):
    #calculate delta
    delta = time() - last_time
    last_time = time()

    #clear screen
    if SYSTEM_TYPE == "Windows":
        cmd("cls")
    else:
        cmd(f"clear ; cat {PATH_TO_FRAMES}{x}") #clear for Linux (bash)

    #print file content
    file_content = frames_file.read(x).decode()
    print(file_content)

    #wait (to get stable framerate)
    waittime = float(frametime - delta)
    if waittime < 0:
        waittime = float(frametime)
    sleep(waittime)