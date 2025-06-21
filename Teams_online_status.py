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