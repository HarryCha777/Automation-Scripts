#! python3
import pyautogui, time, random

print('Started to randomly move the mouse a bit once per 10 seconds.')

while True:
    pyautogui.moveRel(random.randint(-30, 30), random.randint(-30, 30), duration=0.25)
    time.sleep(10)    

print('Mouse moving stopped!')