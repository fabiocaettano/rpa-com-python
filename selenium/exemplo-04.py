from selenium import webdriver
import time
navegador = webdriver.Chrome()
navegador.get("https://www.hashtagtreinamentos.com/")
navegador.maximize_window()
botao_verde = navegador.find_element("class name", "botao-verde")
time.sleep(10)
botao_verde.click()
time.sleep(10)