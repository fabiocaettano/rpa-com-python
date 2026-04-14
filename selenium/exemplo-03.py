# Neste exemplo, abrimos o navegador, acessamos um site, maximizamos a janela,
# localizamos um elemento pelo nome da classe e clicamos nele após uma pausa.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
navegador = webdriver.Chrome()
navegador.get("https://www.hashtagtreinamentos.com/")
navegador.maximize_window()
botao_header_titulo = navegador.find_element(By.CLASS_NAME, "header__titulo")
botao_header_titulo.click()
time.sleep(10)