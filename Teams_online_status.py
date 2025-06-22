"""
Hi user this script will kepp your teams status online for the time you like, by moving and clicking your mouse dynamically which will trick Teams in thinking you are online. 
Keep in mind to keep your system running and screen turned on.
You wount be able to do anything on your system while script is running since it moves and click your mouse to keep your status active.

Your system should have python installed to run this script.
You would need to install pyautogui in your system/virtual environment. command 'pip install pyautogui'

To run the script, 
1. go to your terminal/command prompt
2. change to the directory where you have saved this file.
3. give command 'python Teams_online_status.py'. If you changed the filename, give the same to this commmand.
4. enter the number of minutes you want to stay online.
To stop the script execution in middle, do a 'ctrl+c' or 'ctrl+alt+delete' if former didnt work.
"""

import time
import pyautogui

start_time = time.time()
user_time = int(input("How log do you want to stay online (enter value in minuits): "))
sec = user_time * 60

while time.time() - start_time < sec:
    pyautogui.moveTo(1500,150)
    pyautogui.click(1000,150)
    pyautogui.moveTo(1500,150)

print(f"Done for {user_time} minutes.")
