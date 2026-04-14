import pyautogui
import time

def clicar_em_coordenadas(x, y):
    """
    Move o cursor do mouse para as coordenadas (x, y) e realiza um clique.
    
    Parâmetros:
    x (int): A coordenada x na tela.
    y (int): A coordenada y na tela.
    """
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print(f"Clique realizado em ({x}, {y})")

def mover_para_coordenadas(x, y):
    """
    Move o cursor do mouse para as coordenadas (x, y) sem clicar.
    
    Parâmetros:
    x (int): A coordenada x na tela.
    y (int): A coordenada y na tela.
    """
    pyautogui.moveTo(x, y)
    print(f"Cursor movido para ({x}, {y})")

def descobrir_resolucao_tela():
    """
    Retorna a resolução atual da tela.
    
    Retorna:
    tuple: Uma tupla contendo a largura e altura da tela (largura, altura).
    """
    largura, altura = pyautogui.size()
    return largura, altura

def obter_posicao_cursor(): 
    """
    Retorna a posição atual do cursor do mouse.
    
    Retorna:
    tuple: Uma tupla contendo as coordenadas x e y do cursor (x, y).
    """
    x, y = pyautogui.position()
    return x, y

def teste01():
    #pyautogui.alert("Teste de automação iniciado!")
    pyautogui.press("WIN")  # Abre o menu Iniciar no Windows
    pyautogui.write("chrome")  # Digita "chrome"
    pyautogui.press("ENTER")  # Pressiona Enter para abrir o Chrome
    pyautogui.sleep(2)  # Aguarda 2 segundos para o navegador

def teste02():
    x, y = obter_posicao_cursor()
    time.sleep(15)  # Aguarda 5 segundos para o usuário posicionar o cursor
    print(f"Posição atual do cursor: ({x}, {y})")

def teste03():
    largura, altura = descobrir_resolucao_tela()
    print(f"Resolução da tela: {largura}x{altura}")
    

# Exemplo de uso
if __name__ == "__main__":
    teste02()