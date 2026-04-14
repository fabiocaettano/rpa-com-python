# Neste exemplo, abrimos o navegador, acessamos um site, maximizamos a janela,
# localizamos todos os elementos com a classe "header__titulo" e clicamos naquele
# cujo texto é "Assinatura".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
navegador = webdriver.Chrome()
navegador.get("https://www.hashtagtreinamentos.com/")
navegador.maximize_window()
lista_botoes = navegador.find_elements(By.CLASS_NAME, "header__titulo")
for botao in lista_botoes:
    if botao.text == "Assinatura":
        botao.click()
        break
time.sleep(10)