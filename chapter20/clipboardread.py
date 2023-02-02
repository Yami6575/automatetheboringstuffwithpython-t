import pyautogui ,pyperclip

pyautogui.moveTo(30,30)
pyautogui.click()
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
data=pyperclip.paste()
print(data)
