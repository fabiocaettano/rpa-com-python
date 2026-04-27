import pyautogui
import time

historico_execucao = []

def abrirAplicativo(app):
    pyautogui.press('win')    
    pyautogui.write(app)
    pyautogui.press('enter')    
    time.sleep(15)

def informarUrl(url):
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(15)

def autenticarUsuario(usuario, senha):    
    posicionarCursor(929,488) # campo usuario
    pyautogui.write(usuario)
    pyautogui.press('tab')
    time.sleep(1)
    posicionarCursor(988,526) # campo senha
    pyautogui.write(senha)        
    posicionarCursor(1059,599) # campo senha      
    pyautogui.click()    
    time.sleep(15)

def posicionarCursor(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(3)

def copiar():
    pyautogui.hotkey('ctrl', 'c')

def colar():
    pyautogui.hotkey('ctrl', 'v')


def navegarMenu(relatorio):
    posicoes_relatorios = {
        "relatorio_a": [
            (439, 117),
            (675, 195),
            (940, 940),
            (749, 1010),
            (1040, 971),
            (1333, 744)    
        ],
        "relatorio_b": [
            (439, 117), # Icone
            (675, 195), # Correios    
            (940,940),  # Barra de Rolagem  
            (916,954),  # Suprimento
            (1020,920), # Consultas e Relatórios
            (1177,956), # Relatório
            (1313,952), # Fechamento Mensal
            (1479,853), # Pedido Em Aberto
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
         

def exibirStatusJob(job_name):
    time.sleep(5)
    pyautogui.moveTo(530,115) # icone para Exiber Status do Job
    pyautogui.click()    
    time.sleep(3)
    pyautogui.moveTo(551,154) # Exibir Status do Job
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(1055,350) # Infomrar o número do JOB
    pyautogui.click()
    pyautogui.write(job_name)
    time.sleep(2)
    pyautogui.moveTo(299,223) # Clicar em Procurar
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1375,418) # Selecionar o número do JOB
    pyautogui.click()
    time.sleep(2)
    copiar() # copia número do JOB
    job_number = pyautogui.paste() # armazena número do JOB
    return job_number

def registrar_relatorio(nome, job, ref_erp):
    from datetime import datetime
    
    dados = {
        "nome": nome,
        "job": job,
        "referencia": ref_erp,
        "timestamp": datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    }
    historico_execucao.append(dados)


def executarRelatorioA():
    # tela 1
    time.sleep(3)
    pyautogui.moveTo(301, 291) # marcar seleção
    pyautogui.click()    
    time.sleep(2)
    pyautogui.moveTo(329, 217) # submeter
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(268, 383) # marcar linha
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(375, 245) # botão excluir
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(265,248) # botão ok
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(265,248) # botão ok
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(263,218) # botão ok , SUBMETE O JOB
    pyautogui.click()    
   
def executarRelatorioB():
    # tela 1
    time.sleep(3)
    pyautogui.moveTo(286, 289) # marcar seleção
    pyautogui.click()    
    time.sleep(2)
    pyautogui.moveTo(329, 217) # submeter
    pyautogui.click()  


    # tela 2
    time.sleep(3)
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
    abrirAplicativo('firefox')    
    informarUrl('')
    autenticarUsuario('', '')  
    # executar Repost
    navegarMenu('relatorio_a')    
    executarRelatorioA()
    job_number = exibirStatusJob('R5542E002_EST72M0001')
    registrar_relatorio('Relatório A', job_number, 'R5542E002_EST72M0001')
   
    navegarMenu('relatorio_b')
    executarRelatorioB()
    #exibirStatusJob('R5542E002_EST72M0001')
    #registrar_relatorio('Relatório A', job_number, 'R5542E002_EST72M0001')

    
