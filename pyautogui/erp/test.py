
import pyautogui
import time

def testeClick():    
    pyautogui.moveTo(331,287)  # Comparação
    pyautogui.click()
    pyautogui.moveTo(320,213)  # Comparação
    pyautogui.click()
    time.sleep(4)
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    pyautogui.press('tab')    
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('tab')    
    time.sleep(1)
    pyautogui.press('down')    
    pyautogui.press('down')    
    pyautogui.press('down')    
    pyautogui.press('down')    
    time.sleep(1)
    pyautogui.write('S9')
    pyautogui.moveTo(248,239)  # Comparação
    pyautogui.click()



if __name__ == "__main__":
    pyautogui.PAUSE = 1.0       
    time.sleep(10)
    testeClick()