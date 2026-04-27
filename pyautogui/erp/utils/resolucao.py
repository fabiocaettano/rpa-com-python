import pyautogui

def descobrir_resolucao_tela():
    largura, altura = pyautogui.size()
    print(f'Resolução da tela: {largura}x{altura}')
    return largura, altura


if __name__ == "__main__":
    pyautogui.PAUSE = 1.0    
    largura, altura = descobrir_resolucao_tela()
    print(f'largura: {largura} e altura: {altura}')
