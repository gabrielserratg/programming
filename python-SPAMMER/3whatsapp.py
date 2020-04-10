import pyautogui
import time

#pyautogui.displayMousePosition()

filepath = 'user.txt'
with open(filepath) as fp:
    line = fp.read()
    print(line)

acg = pyautogui

acg.click(83, 217)

acg.typewrite(line)