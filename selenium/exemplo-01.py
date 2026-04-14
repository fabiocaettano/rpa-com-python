#Neste exemplo, abrimos o navegador Chrome e acessamos a página do Google.
from selenium import webdriver
import time
navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")
time.sleep(10)