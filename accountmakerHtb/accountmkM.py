import pyautogui 
import time

#capture coded
time.sleep(2)
pyautogui.click(x=106, y=84)
time.sleep(2)
pyautogui.click(x=722, y=391)
time.sleep(2)
pyautogui.doubleClick(x=1078, y=598)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

#decoding
pyautogui.click(x=328, y=84)
time.sleep(1)
pyautogui.doubleClick(x=328, y=263)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.click(x=252, y=575) #For config
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)



#register in invite
pyautogui.click(x=512, y=79)
time.sleep(1)
pyautogui.click(x=261, y=239)
time.sleep(2)
pyautogui.click(x=594, y=446)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.click(x=556, y=493)
time.sleep(3)

pyautogui.click(x=252, y=575)



time.sleep(10)
#register in invite
pyautogui.doubleClick(x=424, y=120)
pyautogui.write("localhost")
pyautogui.press('enter')
pyautogui.click(x=652, y=443)
