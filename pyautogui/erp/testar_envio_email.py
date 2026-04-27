import pyautogui
import time
from datetime import datetime
import pyperclip

historico_execucao = []

def abrirAplicativo(app):
    pyautogui.press('win')    
    pyautogui.write(app)
    pyautogui.press('enter')    
    time.sleep(10)

def informarUrl(url):
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(10)


def registrar_relatorio(nome, job, ref_erp):
    from datetime import datetime
    
    dados = {
        "nome": nome,
        "job": job,
        "referencia": ref_erp,
        "timestamp": datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    }
    historico_execucao.append(dados)

def enviarEmail(destinatarios):
    # Clicar no botão "Novo Email"
    pyautogui.moveTo(113, 177) 
    pyautogui.click()
    time.sleep(5)

    # Clicar no campo "Para"
    pyautogui.write(destinatarios)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)

    # Preencher o campo "Assunto"
    data_atual = datetime.now()
    data_atual_str = data_atual.strftime("%d/%m/%Y")
    assunto = "Relatório Automatizado ERP - " + data_atual_str
    time.sleep(1)
    pyperclip.copy(assunto)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(2)

    # Preencher o corpo do email
    corpo = "Prezados,\n\nSegue em anexo o relatório automatizado do ERP."
    corpo += "\n\n"    

    pyperclip.copy(corpo)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)   

    corpo = ""
    item = 1

    for relatorio in historico_execucao:
        corpo += f"{item}. {relatorio['nome']}, Job: {relatorio['job']}, Referência: {relatorio['referencia']} \n"
        item += 1

    pyperclip.copy(corpo)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)   
    
    corpo = "\n\n"    
    corpo += "\n\nAtenciosamente."
    pyperclip.copy(corpo)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)   
    

    # Definir Confidencialidade como "Público"
    pyautogui.moveTo(1239, 245) # posição do menu de opções
    time.sleep(1)
    pyautogui.click() # abrir menu
    time.sleep(1)   
    pyautogui.press('enter')   


    # Clicar no botão "Enviar"
    time.sleep(1)   
    pyautogui.hotkey('ctrl', 'enter')

    # Fechar Browser
    time.sleep(5)
    pyautogui.hotkey('alt', 'f4')
    

if __name__ == "__main__":
    pyautogui.PAUSE = 1.0        
    abrirAplicativo('edge')    
    informarUrl('https://outlook.cloud.microsoft/mail/')
    #destinarios = "fabioac@correios.com.br;THIAGOCUNHA@correios.com.br;tamiressilvamonteiro@correios.com.br;"
    destinarios = "fabioac@correios.com.br;"
    registrar_relatorio('Repost ', '3343483', 'R5542E002_EST72M0001')
    registrar_relatorio('Checar pedidos em aberto com status próximo menor que 598','3343483', 'R5542E002_EST72M0002')
    enviarEmail(destinarios)