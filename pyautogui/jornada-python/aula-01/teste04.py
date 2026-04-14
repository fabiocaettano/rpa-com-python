import pyautogui
import time

pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=448, y=361)  # clicar no campo de email
pyautogui.write("pythonimpressionador@gmail.com") #preenche o campo email
pyautogui.press("tab") # passando pro próximo campo

time.sleep(5)
pyautogui.write("sua senha muito muito muito dificilima")

time.sleep(5)
pyautogui.click(x=672, y=527) # clique no botao de login

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:  
    # clicar no campo de código
    pyautogui.click(x=406, y=256)
    
    codigo = tabela.loc[linha, "codigo"]    
    pyautogui.write(str(codigo))    
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))        
    pyautogui.press("tab")
    
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim