import pyautogui
import time

def abirAplicativo(app):
    pyautogui.press('win')
    pyautogui.write(app)
    pyautogui.press('enter')
    time.sleep(5)

def informarUrl(url):
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(7)

def autenticarUsuario(usuario, senha):    
    posicionarCursor(682,390) # campo usuario
    pyautogui.write(usuario)
    posicionarCursor(828,490) # botão continuar
    pyautogui.click()
    posicionarCursor(670,421) # campo senha
    pyautogui.write(senha)    
    posicionarCursor(765,525)
    pyautogui.click()
    #pyautogui.press('tab')
    #pyautogui.write(senha)
    #pyautogui.press('enter')    

def posicionarCursor(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(5)

def navegarMenu(relatorio):
    posicoes_relatorios = {
        "relatorio_a": [
            (293, 121),
            (62, 576),
        ],
        "relatorio_b": [
            (120, 220),
            (170, 270),
            (220, 320),
        ],
        "relatorio_c": [
            (130, 230),
            (180, 280),
            (230, 330),
            (280, 380),
        ],
    }
    if relatorio in posicoes_relatorios:
        for posicao in posicoes_relatorios[relatorio]:
            posicionarCursor(posicao[0], posicao[1])
    else:
        print(f"Relatório '{relatorio}' não encontrado.")
    

def executarRelatorioA():
    pyautogui.moveTo(293, 121)
    pyautogui.click()    
    pyautogui.moveTo(293, 121)
    pyautogui.click()
    pyautogui.moveTo(293, 121)
    pyautogui.click()
    pyautogui.moveTo(293, 121)
    pyautogui.click()


if __name__ == "__main__":
    pyautogui.PAUSE = 1.0    
    abirAplicativo('firefox')
    informarUrl('https://portalhashtag.com/login')
    autenticarUsuario('', '')
    time.sleep(5)
    navegarMenu('relatorio_a')