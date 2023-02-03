import pyautogui as py
import pyperclip
import time


time.sleep(10)


py.click(960, 540) 

py.hotkey('ctrl','a')
py.hotkey('ctrl','c')
text = pyperclip.paste()

print(text)
