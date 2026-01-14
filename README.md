# 📊 Análise de Sentimento de E-commerce: Python & Power BI

![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Selenium](https://img.shields.io/badge/Ferramenta-Selenium-green)

## 🎯 Objetivo do Projeto
Este projeto foi desenvolvido para demonstrar o ciclo completo de um analista de dados: desde a coleta automatizada de dados na web (**Web Scraping**), o processamento e inteligência com **Python**, até a visualização estratégica em um dashboard no **Power BI**.

O foco é entender a percepção dos clientes sobre um produto específico, classificando as avaliações como positivas, negativas ou neutras.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python**: Linguagem base do projeto.
* **Selenium**: Automação para navegar no e-commerce e coletar as avaliações.
* **Pandas**: Manipulação e estruturação dos dados em tabelas.
* **TextBlob**: Biblioteca de NLP (Processamento de Linguagem Natural) para análise de sentimento.
* **Power BI**: Criação de visualizações interativas.
* **Git/GitHub**: Versionamento e portfólio.

---

## 📉 Fluxo de Dados

1.  **Extração**: O robô `Selenium` acessa o site, percorre as páginas de comentários e extrai o texto bruto.
2.  **Transformação**: O `Pandas` limpa os dados e remove informações irrelevantes.
3.  **Análise**: A `TextBlob` atribui uma nota de polaridade para cada comentário.
4.  **Carga**: Os dados são exportados para um arquivo `.csv`.
5.  **Visualização**: O `Power BI` consome o arquivo para gerar insights de negócio.

---

## 💻 Passo a Passo do Código

### 1. Configuração do Ambiente
Para rodar o projeto, instale as dependências:
```bash
pip install selenium pandas textblob webdriver-manager