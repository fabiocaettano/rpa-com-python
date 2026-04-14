import pyautogui
import time

pyautogui.PAUSE = 5

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=448, y=361)  # clicar no campo de email
pyautogui.write("pythonimpressionador@gmail.com") #preenche o campo email
pyautogui.press("tab") # passando pro próximo campo

time.sleep(3)
pyautogui.write("sua senha muito muito muito dificilima")

time.sleep(3)
pyautogui.click(x=672, y=527) # clique no botao de login
