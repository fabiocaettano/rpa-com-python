# Neste exemplo, abrimos o navegador, acessamos um site, maximizamos a janela,
# localizamos todos os elementos com a classe "header__titulo" e clicamos naquele
# cujo texto é "Assinatura".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Abrimos o navegador e acessamos o site
navegador = webdriver.Chrome()
navegador.get("https://www.hashtagtreinamentos.com/")

# Maximizamos a janela do navegador
navegador.maximize_window()

# Localiza todos os elementos com a classe "header__titulo"
lista_botoes = navegador.find_elements(By.CLASS_NAME, "header__titulo")
for botao in lista_botoes:
    if botao.text == "Assinatura":
        botao.click()
        break

# gerenciando múltiplas abas
abas = navegador.window_handles
# direciona para primeira aba
navegador.switch_to.window(abas[0])
navegador.get("https://www.hashtagtreinamentos.com/curso-python")
# Preenche o formulário de inscrição
navegador.find_element(By.ID, "firstname").send_keys("João")
navegador.find_element(By.ID, "email").send_keys("bla@bla.com")
navegador.find_element(By.ID, "phone").send_keys("11-999999999")
# Localiza o botão "Acessar o curso" e rola a página até ele
botao_acessar_curso = navegador.find_element(By.ID, "_form_2475_submit")
# centra o botão na tela evocê pode ver o movimento de rolagem
# aguardando 5 segundos para visualizar a rolagem
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_acessar_curso)
time.sleep(5)
# clica no botão "Acessar o curso"
botao_acessar_curso.click()
time.sleep(10)
