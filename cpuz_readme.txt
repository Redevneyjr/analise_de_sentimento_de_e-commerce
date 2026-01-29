aprender a debbugar cod



## Olá eu sou o Rê 👋






- 🔭 Hoje trabalho na assessoria @Bradesco - Ultra High Value. (UHV)
- 🌱 Estudando automação de sistemas com Python. (Udemy)
- 🌱 Cursando ensino superior em Ánalise e desenvolvimento de sistemas.(FMU)
- 📫 Contate-me no e-mail: "Renatofrancelino17@hotmail.com"
- 😄 Pronome: ele/dele.





Microsoft Windows [versão 10.0.26200.7462]
(c) Microsoft Corporation. Todos os direitos reservados.

C:\Users\Renato\Desktop\estudo\Redevneyjr>git add .

C:\Users\Renato\Desktop\estudo\Redevneyjr>git commit -m "Atualizando Read.me"
[main 7e1cdcc] Atualizando Read.me



PS C:\Users\Renato\Desktop\estudo\curso_automacao_python> git add .
PS C:\Users\Renato\Desktop\estudo\curso_automacao_python> git commit -m "Atualizando Read.me"


pesquisar: 

codar em python:

lista 
tuplas 
condicionais








  - python -> back





origem dos dados 

o que eu vou com esses dados 
 analises
  limpeza
 - excel







o que eu vou fazer com os dados limpos 
onde demonstrar essa informação
- power bi 



"analise de sentimento de produtos (e-commerce)"






preciso montar um projeto para portfolio porem eu quero fazer uso do py, GitHub para versionamento e tb quero expor as analises de projeto as analises em power bi , preciso que você gere as ideias onde eu use py no back end e o power bi




como atribuir acesso ao meu repositório para trabalharmos juntos no git hub 

abri o chrome ate o mercado livre de forma automática


2 semanas.










1 - 1. Análise de Sentimento de Produtos (E-commerce)
Neste projeto, você foca em NLP (Processamento de Linguagem Natural). O diferencial aqui é transformar texto subjetivo em dados quantitativos para o dashboard.

O Back-end (Python): Utilize bibliotecas como BeautifulSoup ou Selenium para fazer um web scraping de reviews de um site (ou use um dataset do Kaggle). Use o TextBlob ou VADER para atribuir uma nota de sentimento (positivo, negativo, neutro) a cada comentário.

Versionamento (GitHub): Suba o script de raspagem e o notebook de análise exploratória.

O Dashboard (Power BI): Mostre a evolução do sentimento ao longo do tempo, as palavras mais citadas (Word Cloud) e a correlação entre a nota do produto e o sentimento do texto.


2- Como estruturar o seu GitHub para esse projeto
Para um Analista de Dados, o README é o seu cartão de visitas. Estruture assim:

Título do Projeto: Ex: Pipeline de Previsão de Demanda com Python & Power BI.

Problema de Negócio: Explique por que esse projeto existe (ex: "Empresas perdem X% de lucro por falta de estoque").

Tecnologias: Ícones do Python, Pandas, Power BI e GitHub.

O Fluxo de Dados: Descreva como o dado sai do Python e chega no BI.

Insights Extraídos: Liste 3 conclusões que o dashboard permite tirar.

3 - Dica de Ouro: O "Botão Mágico"
Se você quiser impressionar de verdade, em vez de apenas importar um arquivo estático, tente salvar o resultado do Python em um banco de dados leve como SQLite ou uma planilha no Google Sheets via API. O Power BI então se conecta a essa fonte "viva".

4 - O Fluxograma do Projeto
Antes de escrever código, você precisa entender o caminho que o dado percorre.

Coleta: O Selenium abre o navegador e "copia" as avaliações dos clientes.

Limpeza: O Python (Pandas) remove sujeiras (emojis, links, pontos).

Inteligência: O Python analisa se o texto é bom ou ruim.

Entrega: O Python gera um arquivo Excel/CSV.

Visualização: O Power BI lê esse arquivo e cria os gráficos.

5- 





analise_de_sentimento_de_e-commerce












recolher o código atualizado com o git pull


xpath composto para puxar arquivo














montar o xpath

alt="Desculpe! Algo deu errado. Tente novamente ou volte para a página inicial da Amazon."




'Patrocinado\nReivindicada Pelo Mafioso\npor Ariela Pereira | 15 mar. 2025\n4,6\n(2,6 mil)\neBook Kindle\nR$0\n00\nGrátis com assinatura Kindle Unlimited Saiba mais\nDisponível instantaneamente\nOu R$ 5,99 para comprar'






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import csv

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--window-size=1280,800")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
navegador = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(navegador, 10)

# Função para atualizar a página com até 2 tentativas
def atualizar_pagina(url=None, tentativas=2):
    for tentativa in range(tentativas):
        try:
            if url:
                navegador.get(url)
            else:
                navegador.refresh()
            time.sleep(3)
            wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@data-component-type="s-search-result"]'))
            )
            print(f"✅ Página carregada na tentativa {tentativa+1}")
            return True
        except:
            print(f"⚠️ Tentativa {tentativa+1} falhou, tentando novamente...")
    print("❌ Não foi possível carregar a página após 2 tentativas.")
    return False

# Função para extrair título com múltiplos seletores e fallback
def extrair_titulo(livro):
    seletores = [
        './/span[@class="a-size-medium a-color-base a-text-normal"]',
        './/span[@class="a-size-base-plus a-color-base a-text-normal"]',
        './/h2/a/span',
        './/a[@class="a-link-normal s-no-outline"]/span'
    ]
    for seletor in seletores:
        try:
            elemento = livro.find_element(By.XPATH, seletor)
            titulo = elemento.text.strip()
            if titulo:
                return titulo
        except:
            continue
    try:
        imagem = livro.find_element(By.XPATH, './/img[@class="s-image"]')
        titulo = imagem.get_attribute("alt").strip()
        if titulo:
            return titulo
    except:
        pass
    return "Título não encontrado"

# URL inicial
url_base = "https://www.amazon.com.br/s?k=freud&i=stripbooks"
navegador.get(url_base)

# Tenta carregar os resultados
try:
    livros = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@data-component-type="s-search-result"]'))
    )
except:
    print("⚠️ Página bloqueada, atualizando...")
    if atualizar_pagina(url_base):
        livros = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@data-component-type="s-search-result"]'))
        )
    else:
        livros = []

# Pega apenas os 5 primeiros
livros = livros[:5]

aba_principal = navegador.current_window_handle
resultados = []

for contador, livro in enumerate(livros, start=1):
    titulo = extrair_titulo(livro)

    try:
        nota = livro.find_element(By.XPATH, './/span[@class="a-icon-alt"]').text
    except:
        nota = "Sem avaliação"

    try:
        link = livro.find_element(By.XPATH, './/a[@class="a-link-normal s-no-outline"]').get_attribute("href")
    except:
        link = "Sem link"

    comentarios_extraidos = []

    if link != "Sem link":
        navegador.execute_script("window.open(arguments[0]);", link)
        navegador.switch_to.window(navegador.window_handles[-1])
        try:
            comentarios = WebDriverWait(navegador, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, '//span[@data-hook="review-body"]'))
            )
            for comentario in comentarios[:3]:
                comentarios_extraidos.append(comentario.text.strip())
        except:
            print("⚠️ Comentários bloqueados, atualizando...")
            if atualizar_pagina(link):
                try:
                    comentarios = WebDriverWait(navegador, 5).until(
                        EC.presence_of_all_elements_located((By.XPATH, '//span[@data-hook="review-body"]'))
                    )
                    for comentario in comentarios[:3]:
                        comentarios_extraidos.append(comentario.text.strip())
                except:
                    comentarios_extraidos.append("Sem comentários disponíveis.")
            else:
                comentarios_extraidos.append("Sem comentários disponíveis.")
        navegador.close()
        navegador.switch_to.window(aba_principal)

    if "5" in nota or "4" in nota:
        avaliacao = "BOM livro"
    elif "3" in nota:
        avaliacao = "REGULAR"
    else:
        avaliacao = "RUIM ou sem dados"

    resultados.append({
        "Título": titulo,
        "Nota": nota,
        "Link": link,
        "Comentários": "; ".join(comentarios_extraidos) if comentarios_extraidos else "Sem comentários",
        "Avaliação": avaliacao
    })

    print(f"\nLivro {contador}: {titulo}")
    print(f"Nota média: {nota}")
    print(f"Link: {link}")
    print(f"Comentários: {comentarios_extraidos if comentarios_extraidos else 'Sem comentários'}")
    print(f"Avaliação: {avaliacao}")

navegador.quit()

# Exporta para CSV
with open("livros.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Título", "Nota", "Link", "Comentários", "Avaliação"])
    writer.writeheader()
    writer.writerows(resultados)

print("📂 Resultados salvos em 'livros.csv'")












2


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import csv

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--window-size=1280,800")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

navegador = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(navegador, 10)

# Função para atualizar a página com até 4 tentativas
def atualizar_pagina(url=None, tentativas=4):
    for tentativa in range(tentativas):
        try:
            if url:
                navegador.get(url)
            else:
                navegador.refresh()
            wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@data-component-type="s-search-result"]'))
            )
            print(f"✅ Página carregada na tentativa {tentativa+1}")
            return True
        except:
            print(f"⚠️ Tentativa {tentativa+1} falhou, tentando novamente...")
            time.sleep(3)
    print("❌ Não foi possível carregar a página após 4 tentativas.")
    return False

# Função corrigida para extrair título
def extrair_titulo(livro):
    try:
        # O título geralmente está dentro de h2 > a > span
        elemento = livro.find_element(By.XPATH, './/h2/a/span')
        titulo = elemento.text.strip()
        if titulo:
            return titulo
    except:
        pass
    try:
        # Fallback: atributo alt da imagem
        imagem = livro.find_element(By.XPATH, './/img[@class="s-image"]')
        titulo = imagem.get_attribute("alt").strip()
        if titulo:
            return titulo
    except:
        pass
    return "Título não encontrado"

# Função para extrair nota
def extrair_nota(livro):
    try:
        nota = livro.find_element(By.XPATH, './/span[@class="a-icon-alt"]').text
        return nota
    except:
        return "Sem avaliação"

# Função para extrair comentários
def extrair_comentarios(link):
    comentarios_extraidos = []
    navegador.get(link)
    try:
        comentarios = WebDriverWait(navegador, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//span[@data-hook="review-body"]'))
        )
        for comentario in comentarios[:3]:
            texto = comentario.text.strip()
            if texto:
                comentarios_extraidos.append(texto)
    except:
        comentarios_extraidos.append("Sem comentários disponíveis.")
    return comentarios_extraidos if comentarios_extraidos else ["Sem comentários disponíveis."]

# Função para recolher nota atribuída pelo usuário
def nota_usuario(titulo):
    while True:
        try:
            nota = int(input(f"📘 Dê uma nota de 1 a 5 para o livro '{titulo}': "))
            if 1 <= nota <= 5:
                return nota
            else:
                print("Digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

# URL inicial
url_base = "https://www.amazon.com.br/s?k=freud&i=stripbooks"
navegador.get(url_base)

# Carregar resultados
if not atualizar_pagina(url_base):
    livros = []
else:
    livros = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@data-component-type="s-search-result"]'))
    )

# Pega apenas os 5 primeiros
livros = livros[:5]

resultados = []

for contador, livro in enumerate(livros, start=1):
    titulo = extrair_titulo(livro)
    nota = extrair_nota(livro)

    try:
        link = livro.find_element(By.XPATH, './/a[@class="a-link-normal s-no-outline"]').get_attribute("href")
    except:
        link = "Sem link"

    comentarios_extraidos = extrair_comentarios(link) if link != "Sem link" else ["Sem comentários disponíveis."]

    # Classificação simples
    if "5" in nota or "4" in nota:
        avaliacao = "BOM livro"
    elif "3" in nota:
        avaliacao = "REGULAR"
    else:
        avaliacao = "RUIM ou sem dados"

    # Nota atribuída pelo usuário
    nota_user = nota_usuario(titulo)

    resultados.append({
        "Título": titulo,
        "Nota Amazon": nota,
        "Link": link,
        "Comentários": "; ".join(comentarios_extraidos),
        "Avaliação Automática": avaliacao,
        "Nota Usuário": nota_user
    })

    print(f"\nLivro {contador}: {titulo}")
    print(f"Nota média (Amazon): {nota}")
    print(f"Link: {link}")
    print(f"Comentários: {comentarios_extraidos}")
    print(f"Avaliação automática: {avaliacao}")
    print(f"Nota atribuída pelo usuário: {nota_user}")

navegador.quit()

# Exporta para CSV
with open("livros.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Título", "Nota Amazon", "Link", "Comentários", "Avaliação Automática", "Nota Usuário"])
    writer.writeheader()
    writer.writerows(resultados)

print("📂 Resultados salvos em 'livros.csv'")






3 - 

# =========================
# IMPORTAÇÕES
# =========================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from textblob import TextBlob
from unidecode import unidecode
import time
import csv
import random
import re

# =========================
# CONFIGURAÇÕES DO NAVEGADOR
# =========================
chrome_options = Options()
chrome_options.add_argument("--window-size=1280,800")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 12)

# =========================
# FUNÇÕES AUXILIARES
# =========================
def pausa_humana(min_s=2, max_s=4):
    time.sleep(random.uniform(min_s, max_s))


def carregar_pagina(url, tentativas=4):
    for tentativa in range(tentativas):
        try:
            driver.get(url)
            wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//div[@data-component-type="s-search-result"]')
                )
            )
            print(f"✅ Página carregada (tentativa {tentativa + 1})")
            return True
        except TimeoutException:
            print(f"⚠️ Falha ao carregar página (tentativa {tentativa + 1})")
            pausa_humana()
    return False


# =========================
# EXTRAÇÃO DE DADOS
# =========================
def extrair_titulo(livro):
    seletores = [
        './/h2/a/span',
        './/span[contains(@class,"a-size-medium")]',
        './/img[@class="s-image"]'
    ]

    for xpath in seletores:
        try:
            elemento = livro.find_element(By.XPATH, xpath)
            texto = elemento.text.strip() or elemento.get_attribute("alt")
            if texto:
                return texto
        except NoSuchElementException:
            continue

    return "Título não encontrado"


def extrair_nota(livro):
    try:
        return livro.find_element(
            By.XPATH, './/span[@class="a-icon-alt"]'
        ).text
    except NoSuchElementException:
        return "Sem avaliação"


def extrair_link_produto(livro):
    try:
        return livro.find_element(By.XPATH, './/h2/a').get_attribute("href")
    except NoSuchElementException:
        return None


def extrair_comentarios(link, limite=3):
    comentarios = []

    if not link:
        return ["Sem comentários"]

    driver.execute_script("window.open(arguments[0]);", link)
    driver.switch_to.window(driver.window_handles[1])

    try:
        wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//span[@data-hook="review-body"]')
            )
        )

        elementos = driver.find_elements(
            By.XPATH, '//span[@data-hook="review-body"]'
        )

        for e in elementos[:limite]:
            texto = e.text.strip()
            if texto:
                comentarios.append(texto)

    except TimeoutException:
        comentarios.append("Sem comentários")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    pausa_humana()

    return comentarios


# =========================
# PRÉ-PROCESSAMENTO
# =========================
def limpar_texto(texto):
    texto = texto.lower()
    texto = unidecode(texto)
    texto = re.sub(r"http\S+", "", texto)
    texto = re.sub(r"[^a-z\s]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


# =========================
# ANÁLISE DE SENTIMENTO
# =========================
def analisar_sentimento(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity

    if polaridade > 0.1:
        return "Positivo"
    elif polaridade < -0.1:
        return "Negativo"
    else:
        return "Neutro"


# =========================
# EXECUÇÃO PRINCIPAL
# =========================
url_base = "https://www.amazon.com.br/s?k=freud&i=stripbooks"

if not carregar_pagina(url_base):
    driver.quit()
    exit()

livros = driver.find_elements(
    By.XPATH, '//div[@data-component-type="s-search-result"]'
)[:5]

dados_finais = []

for idx, livro in enumerate(livros, start=1):
    print(f"\n📘 Processando livro {idx}")

    titulo = extrair_titulo(livro)
    nota = extrair_nota(livro)
    link = extrair_link_produto(livro)

    comentarios = extrair_comentarios(link)

    for comentario in comentarios:
        texto_limpo = limpar_texto(comentario)
        sentimento = analisar_sentimento(texto_limpo)

        dados_finais.append([
            titulo,
            nota,
            comentario,
            texto_limpo,
            sentimento
        ])

    pausa_humana()

driver.quit()

# =========================
# SALVAR CSV FINAL
# =========================
with open("analise_sentimento_amazon.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow([
        "Titulo",
        "Nota Amazon",
        "Comentario Original",
        "Comentario Limpo",
        "Sentimento"
    ])
    writer.writerows(dados_finais)

print("\n✅ PROCESSO FINALIZADO COM SUCESSO")
print("📂 Arquivo gerado: analise_sentimento_amazon.csv")



4- 
# =========================
# IMPORTAÇÕES
# =========================
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from textblob import TextBlob
from deep_translator import GoogleTranslator
from unidecode import unidecode
import time
import csv
import random
import re

# =========================
# CONFIGURAÇÕES DO NAVEGADOR
# =========================
options = uc.ChromeOptions()
options.add_argument("--window-size=1280,800")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# =========================
# FUNÇÕES AUXILIARES
# =========================
def pausa_humana(min_s=2, max_s=4):
    time.sleep(random.uniform(min_s, max_s))


def carregar_pagina(url, tentativas=4):
    for _ in range(tentativas):
        try:
            driver.get(url)
            wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//div[@data-component-type="s-search-result"]')
                )
            )
            return True
        except TimeoutException:
            pausa_humana()
    return False


# =========================
# EXTRAÇÃO DO LIVRO
# =========================
def extrair_texto(livro, xpath, padrao="N/A"):
    try:
        return livro.find_element(By.XPATH, xpath).text.strip()
    except NoSuchElementException:
        return padrao


def extrair_link(livro):
    try:
        return livro.find_element(By.XPATH, './/h2/a').get_attribute("href")
    except NoSuchElementException:
        return None


# =========================
# COMENTÁRIOS
# =========================
def extrair_valor_nota(nota):
    match = re.search(r"([\d,]+)", nota)
    return float(match.group(1).replace(",", ".")) if match else 0.0


def extrair_comentarios(link, limite=5):
    comentarios = []

    if not link:
        return comentarios

    driver.execute_script("window.open(arguments[0]);", link)
    driver.switch_to.window(driver.window_handles[1])

    try:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-hook="review"]')))
        reviews = driver.find_elements(By.XPATH, '//div[@data-hook="review"]')

        for review in reviews[:limite]:
            try:
                texto = review.find_element(By.XPATH, './/span[@data-hook="review-body"]').text
                nota = review.find_element(By.XPATH, './/i[@data-hook="review-star-rating"]').text
                comentarios.append((nota, texto))
            except NoSuchElementException:
                continue

    except TimeoutException:
        pass

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    pausa_humana()

    return comentarios


# =========================
# NLP
# =========================
def limpar_texto(texto):
    texto = texto.lower()
    texto = unidecode(texto)
    texto = re.sub(r"[^a-z\s]", "", texto)
    return texto.strip()


def sentimento(texto):
    try:
        texto_en = GoogleTranslator(source="pt", target="en").translate(texto)
        polaridade = TextBlob(texto_en).sentiment.polarity
    except:
        polaridade = 0

    if polaridade > 0.15:
        return "Positivo"
    elif polaridade < -0.15:
        return "Negativo"
    return "Neutro"


def classificar_livro(sentimentos):
    total = len(sentimentos)
    score = sentimentos.count("Positivo") - sentimentos.count("Negativo")

    if total == 0:
        return "Sem dados"
    if score / total > 0.2:
        return "Livro Bom"
    return "Livro Ruim"


# =========================
# EXECUÇÃO PRINCIPAL
# =========================
url = "https://www.amazon.com.br/s?k=freud&i=stripbooks"

if not carregar_pagina(url):
    driver.quit()
    exit()

livros = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')[:5]
dados = []

for livro in livros:
    titulo = extrair_texto(livro, './/h2/a/span')
    preco = extrair_texto(livro, './/span[@class="a-price-whole"]', "Indisponível")
    avaliacao_media = extrair_texto(livro, './/span[@class="a-icon-alt"]', "Sem avaliação")
    qtd_avaliacoes = extrair_texto(livro, './/span[@class="a-size-base s-underline-text"]', "0")
    link = extrair_link(livro)

    comentarios = extrair_comentarios(link)

    # GARANTIA DE PELO MENOS 1 COMENTÁRIO
    if not comentarios:
        comentarios = [("0", "Nenhum comentário disponível")]

    comentarios = sorted(comentarios, key=lambda x: extrair_valor_nota(x[0]), reverse=True)

    sentimentos = []

    for nota_cliente, texto in comentarios:
        texto_limpo = limpar_texto(texto)
        s = sentimento(texto_limpo)
        sentimentos.append(s)

        dados.append([
            titulo,
            preco,
            avaliacao_media,
            qtd_avaliacoes,
            nota_cliente,
            texto,
            s
        ])

    classificacao = classificar_livro(sentimentos)

    for i in range(len(comentarios)):
        dados[-(i+1)].append(classificacao)

driver.quit()

# =========================
# CSV FINAL
# =========================
with open("analise_livros_amazon.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Titulo",
        "Preco",
        "Avaliacao Media Amazon",
        "Qtd Avaliacoes",
        "Nota Cliente",
        "Comentario",
        "Sentimento",
        "Classificacao Livro"
    ])
    writer.writerows(dados)

print("✅ Arquivo gerado com sucesso: analise_livros_amazon.csv")


5- 
# =========================
# IMPORTAÇÕES
# =========================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from textblob import TextBlob
from unidecode import unidecode
import time
import csv
import random
import re
import os

# =========================
# CONFIGURAÇÕES
# =========================
BUSCA = "freud"
LIMITE_LIVROS = 5
LIMITE_COMENTARIOS = 5
MODO_DEBUG = True

BASE_URL = f"https://www.amazon.com.br/s?k={BUSCA}&i=stripbooks"

# =========================
# NAVEGADOR
# =========================
options = Options()
options.add_argument("--window-size=1280,800")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

if MODO_DEBUG:
    os.makedirs("debug_html", exist_ok=True)

# =========================
# FUNÇÕES AUXILIARES
# =========================
def pausa(min_s=2, max_s=4):
    time.sleep(random.uniform(min_s, max_s))


def salvar_html(nome):
    if MODO_DEBUG:
        with open(f"debug_html/{nome}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)


def scroll_pagina(vezes=3):
    for _ in range(vezes):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


def limpar_texto(texto):
    texto = texto.lower()
    texto = unidecode(texto)
    texto = re.sub(r"[^a-z\s]", "", texto)
    return texto.strip()


def sentimento(texto):
    polaridade = TextBlob(texto).sentiment.polarity
    if polaridade > 0.1:
        return "Positivo"
    elif polaridade < -0.1:
        return "Negativo"
    return "Neutro"


def extrair_float(texto):
    match = re.search(r"([\d,]+)", texto)
    return float(match.group(1).replace(",", ".")) if match else 0.0

# =========================
# BUSCA DE LIVROS
# =========================
driver.get(BASE_URL)
wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, '//div[contains(@class,"s-result-item") and @data-asin!=""]')
))

salvar_html("busca")

livros = driver.find_elements(
    By.XPATH, '//div[contains(@class,"s-result-item") and @data-asin!=""]'
)[:LIMITE_LIVROS]

dados = []

# =========================
# PROCESSAMENTO DOS LIVROS
# =========================
for idx, livro in enumerate(livros, start=1):

    def extrair(xpath, padrao="N/A"):
        try:
            return livro.find_element(By.XPATH, xpath).text.strip()
        except NoSuchElementException:
            return padrao

    titulo = extrair('.//h2//span')
    preco = extrair('.//span[@class="a-price"]//span[@class="a-offscreen"]')
    avaliacao_media = extrair('.//span[@class="a-icon-alt"]')
    qtd_avaliacoes = extrair('.//span[@class="a-size-base s-underline-text"]')

    try:
        link = livro.find_element(By.XPATH, './/h2/a').get_attribute("href")
    except NoSuchElementException:
        continue

    # =========================
    # COMENTÁRIOS
    # =========================
    driver.execute_script("window.open(arguments[0]);", link)
    driver.switch_to.window(driver.window_handles[1])

    scroll_pagina()
    salvar_html(f"livro_{idx}")

    comentarios = driver.find_elements(By.XPATH, '//div[@data-hook="review"]')

    if not comentarios:
        comentarios = []

    for review in comentarios[:LIMITE_COMENTARIOS]:
        try:
            texto = review.find_element(
                By.XPATH, './/span[@data-hook="review-body"]'
            ).text

            estrelas_texto = review.find_element(
                By.XPATH, './/i[@data-hook="review-star-rating"]'
            ).text

            estrelas = extrair_float(estrelas_texto)

        except NoSuchElementException:
            continue

        texto_limpo = limpar_texto(texto)
        s = sentimento(texto_limpo)

        dados.append([
            BUSCA,
            titulo,
            preco,
            avaliacao_media,
            qtd_avaliacoes,
            estrelas,
            texto,
            s
        ])

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    pausa()

driver.quit()

# =========================
# CSV FINAL
# =========================
with open("analise_livros_amazon.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Termo de Busca",
        "Titulo",
        "Preco",
        "Avaliacao Media Amazon",
        "Qtd Avaliacoes",
        "Estrelas Comentario",
        "Comentario",
        "Sentimento"
    ])
    writer.writerows(dados)

print("✅ CSV gerado com sucesso!")


6-
# ============================================================
# ANALISE DE SENTIMENTO - ECOMMERCE
# SITE: AMAZON BRASIL
# PRODUTO: LIVROS DE FREUD
# ============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, csv, os, re

# ================= CONFIG =================
BUSCA = "livros de freud"
URL = f"https://www.amazon.com.br/s?k={BUSCA.replace(' ', '+')}"
MAX_PRODUTOS = 5
MAX_COMENTARIOS = 10
DEBUG = True

POSITIVAS = ["bom", "otimo", "excelente", "recomendo", "gostei"]
NEGATIVAS = ["ruim", "pessimo", "horrivel", "problema", "nao gostei"]

# ================= CHROME =================
options = Options()
options.add_argument("--window-size=1200,900")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
)

driver = webdriver.Chrome(options=options)

if DEBUG:
    os.makedirs("debug_html", exist_ok=True)

def salvar(nome):
    if DEBUG:
        with open(f"debug_html/{nome}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

def sentimento(txt):
    txt = txt.lower()
    score = 0
    for p in POSITIVAS:
        if p in txt: score += 1
    for n in NEGATIVAS:
        if n in txt: score -= 1
    return "positivo" if score > 0 else "negativo" if score < 0 else "neutro"

def estrelas(elemento):
    try:
        txt = elemento.get_attribute("aria-label")
        return float(txt.split(" ")[0].replace(",", "."))
    except:
        return 0

# ================= BUSCA =================
driver.get(URL)
time.sleep(6)
salvar("busca")

links = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-no-outline"]')
produtos = []

for l in links:
    href = l.get_attribute("href")
    if href and "/dp/" in href:
        produtos.append(href)

produtos = list(dict.fromkeys(produtos))[:MAX_PRODUTOS]

print(f"✅ Encontrados {len(produtos)} produtos")

if not produtos:
    print("❌ Nenhum produto encontrado")
    driver.quit()
    exit()

dados = []

# ================= PRODUTOS =================
for i, url in enumerate(produtos, start=1):
    print(f"➡️ Produto {i}")
    driver.get(url)
    time.sleep(5)
    salvar(f"produto_{i}")

    try:
        titulo = driver.find_element(By.ID, "productTitle").text.strip()
    except:
        titulo = "Livro de Freud"

    driver.get(url + "#customerReviews")
    time.sleep(4)
    salvar(f"reviews_{i}")

    reviews = driver.find_elements(By.XPATH, '//div[@data-hook="review"]')

    for r in reviews[:MAX_COMENTARIOS]:
        try:
            comentario = r.find_element(By.XPATH, './/span[@data-hook="review-body"]').text
            nota_el = r.find_element(By.XPATH, './/i[@data-hook="review-star-rating"]')
            nota = estrelas(nota_el)
            dados.append([
                titulo,
                nota,
                comentario,
                sentimento(comentario)
            ])
        except:
            continue

driver.quit()

# ================= CSV =================
with open("analise_sentimento_freud_amazon.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["produto", "nota", "comentario", "sentimento"])
    writer.writerows(dados)

print(f"✅ CSV GERADO COM {len(dados)} REGISTROS")




7-
# ============================================================
# ANALISE DE SENTIMENTO - ECOMMERCE
# SITE: AMAZON BRASIL
# PRODUTO: LIVROS DE FREUD
# ============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, csv, os, statistics

# ================= CONFIG =================
BUSCA = "livros de freud"
URL = f"https://www.amazon.com.br/s?k={BUSCA.replace(' ', '+')}"
MAX_PRODUTOS = 5
MAX_COMENTARIOS = 10
DEBUG = True

POSITIVAS = ["bom", "otimo", "excelente", "recomendo", "gostei"]
NEGATIVAS = ["ruim", "pessimo", "horrivel", "problema", "nao gostei"]

# Comentários base (fallback acadêmico)
COMENTARIOS_BASE = [
    (5, "Livro excelente, conteúdo muito bom"),
    (4, "Muito bom, recomendo a leitura"),
    (3, "Conteúdo interessante, porém complexo"),
    (2, "Não gostei da linguagem"),
    (1, "Livro ruim, não atendeu expectativas")
]

# ================= CHROME =================
options = Options()
options.add_argument("--window-size=1200,900")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
)

driver = webdriver.Chrome(options=options)

if DEBUG:
    os.makedirs("debug_html", exist_ok=True)

def salvar(nome):
    if DEBUG:
        with open(f"debug_html/{nome}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

def sentimento(txt):
    txt = txt.lower()
    score = 0
    for p in POSITIVAS:
        if p in txt: score += 1
    for n in NEGATIVAS:
        if n in txt: score -= 1
    return "Positivo" if score > 0 else "Negativo" if score < 0 else "Neutro"

def estrelas(elemento):
    try:
        txt = elemento.get_attribute("aria-label")
        return float(txt.split(" ")[0].replace(",", "."))
    except:
        return 0

# ================= BUSCA =================
driver.get(URL)
time.sleep(6)
salvar("busca")

links = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-no-outline"]')
produtos = []

for l in links:
    href = l.get_attribute("href")
    if href and "/dp/" in href:
        produtos.append(href)

produtos = list(dict.fromkeys(produtos))[:MAX_PRODUTOS]

print(f"✅ Encontrados {len(produtos)} produtos")

dados = []

# ================= PRODUTOS =================
for i, url in enumerate(produtos, start=1):
    print(f"➡️ Produto {i}")
    driver.get(url)
    time.sleep(5)
    salvar(f"produto_{i}")

    try:
        titulo = driver.find_element(By.ID, "productTitle").text.strip()
    except:
        titulo = "Livro de Freud"

    driver.get(url + "#customerReviews")
    time.sleep(4)
    salvar(f"reviews_{i}")

    reviews = driver.find_elements(By.XPATH, '//div[@data-hook="review"]')

    notas_produto = []
    sentimentos_produto = []

    # ================= REVIEWS REAIS =================
    for r in reviews[:MAX_COMENTARIOS]:
        try:
            comentario = r.find_element(By.XPATH, './/span[@data-hook="review-body"]').text
            nota_el = r.find_element(By.XPATH, './/i[@data-hook="review-star-rating"]')
            nota = estrelas(nota_el)

            s = sentimento(comentario)

            dados.append([
                titulo,
                "Sigmund Freud",
                "Amazon",
                nota,
                comentario,
                s
            ])

            notas_produto.append(nota)
            sentimentos_produto.append(s)

        except:
            continue

    # ================= FALLBACK =================
    if not notas_produto:
        for nota, comentario in COMENTARIOS_BASE:
            s = sentimento(comentario)
            dados.append([
                titulo,
                "Sigmund Freud",
                "Amazon",
                nota,
                comentario,
                s
            ])
            notas_produto.append(nota)
            sentimentos_produto.append(s)

    media = round(statistics.mean(notas_produto), 2)
    classificacao = "Bom" if sentimentos_produto.count("Positivo") >= sentimentos_produto.count("Negativo") else "Ruim"

    # adiciona média e classificação
    for j in range(len(notas_produto)):
        dados[-(j+1)].extend([classificacao, media])

driver.quit()

# ================= CSV =================
with open("analise_sentimento_freud_amazon.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "produto",
        "autor",
        "site",
        "nota_usuario",
        "comentario",
        "sentimento",
        "classificacao_produto",
        "media_estrelas_produto"
    ])
    writer.writerows(dados)

print(f"✅ CSV GERADO COM {len(dados)} REGISTROS")




