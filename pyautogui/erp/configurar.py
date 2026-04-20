import pyautogui
import time

def obter_posicao_cursor():     
    time.sleep(6)
    x, y = pyautogui.position()
    print(f'valor de x {x} e valor de y {y}')
    return x, y

def descobrir_resolucao_tela():
    largura, altura = pyautogui.size()
    print(f'Resolução da tela: {largura}x{altura}')
    return largura, altura


if __name__ == "__main__":
    pyautogui.PAUSE = 1.0    
    obter_posicao_cursor()
