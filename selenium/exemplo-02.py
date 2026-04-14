#Neste exemplo, abrimos o navegador Chrome, acessamos a página do Google e maximizamos a janela.
from selenium import webdriver
import time
navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")
navegador.maximize_window()
time.sleep(10)