import pyautogui
import time

pyautogui.PAUSE = 3

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(1)