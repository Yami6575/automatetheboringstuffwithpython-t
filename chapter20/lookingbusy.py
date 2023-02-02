import time
import pyautogui

try:
    while True:
        pyautogui.move(10, 0, 0.5)
        pyautogui.move(-10, 0, 0.5)
        time.sleep(10)
except KeyboardInterrupt:
    print('stopped')