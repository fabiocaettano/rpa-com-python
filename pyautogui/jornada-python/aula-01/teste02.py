import pyautogui
import time

pyautogui.PAUSE = 5

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(3)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)