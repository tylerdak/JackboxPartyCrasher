#JackboxPartyCrasher
#This program is designed to generate random 4 character long codes and enter them into Jackbox.tv in an
#attempt to enter a random game. It depends on the way the website worked as of writing it (4/9/20) but can
#easily be reconfigured if the website changes. The script does not have a way of detecting if a code works.
#The user must manually turn it off. (ctrl-C on most terminals)

#It's also not guaranteed that a game code that works will actually have people ready to play :P

import random
import os
import time

#PyAutoGUI is needed for this! pip install pyautogui
import pyautogui


for h in range(5):
    os.system("say " + str(5 - h))
    time.sleep(1)

#Only designed to go for 100 rounds but this could be changed to a while(true) loop if you want it
#to automatically go for longer than that
for i in range(100):
    code = ""
    for j in range(0,4):
        letter = chr(random.randint(65,90))
        code += (letter)

    print("TEST " + str(i+1) + ": " + code)

    pyautogui.write(code)
    pyautogui.press('enter')
    #This delay should definitely be changed if the script messes up or is even too slow for your liking.
    #It's designed to take account for the delay between hitting PLAY and getting the error message
    #that needs to be dismissed. If the connection is too slow, this may not be enough time.
    time.sleep(0.2)
    pyautogui.press('enter')
    for i in range(9):
        pyautogui.press('tab')


