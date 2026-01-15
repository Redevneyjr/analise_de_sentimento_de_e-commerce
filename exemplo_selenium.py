from selenium import webdriver
from selenium.webdriver.common.by import By


navegador = webdriver.Chrome()
navegador.get('https://www.mercadolivre.com.br/')

barra_pesquisar = navegador.find_element(By.XPATH,'//input[@class="nav-search-input"]')
barra_pesquisar.clear()
barra_pesquisar.send_keys('CIVIC 2011')
barra_pesquisar.submit()

descritos_carros = navegador.find_elements(By.XPATH,'//a[@class="poly-component__title"]')

contador = 1
for descritivo in descritos_carros:
    print(f'Carro numero {contador} : descritivo {descritivo.text}')
    contador = contador + 1
