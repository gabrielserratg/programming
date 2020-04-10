import pyautogui
import time

#pyautogui.displayMousePosition()

print("iniciando...")
time.sleep(2)

pyautogui.click(374, 191)
time.sleep(0.5)
pyautogui.click(313, 284)
time.sleep(0.5)
pyautogui.click(356, 588)
time.sleep(0.5)
pyautogui.click(200, 588)
time.sleep(0.5)
pyautogui.tripleClick(42, 588)
time.sleep(0.5)
pyautogui.hotkey('backspace')
time.sleep(0.5)

filepath = 'user.txt'
with open(filepath) as fp:
    line = fp.read()
    #print(line)

pyautogui.typewrite(line)
time.sleep(0.5)
pyautogui.click(356, 588)

print("Changed")