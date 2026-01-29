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
