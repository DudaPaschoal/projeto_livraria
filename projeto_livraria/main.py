
# FASE 2 & 5 (Importações - Exercícios 5 e 15)

import requests
from bs4 import BeautifulSoup
import csv
import sys

# FASE 2 Conectando com a Internet

# Exercício 6
url = "http://books.toscrape.com/"
resposta = requests.get(url)

# Exercício 7
if resposta.status_code == 200:
    print("Conexão bem-sucedida!")
else:
    print(f"Erro ao conectar: Status Code {resposta.status_code}")
    sys.exit() 


# FASE 3

# Exercício 8
soup = BeautifulSoup(resposta.text, "html.parser")
print(f"Título da página: {soup.title.text.strip()}")

# Exercício 9
livros_html = soup.find_all("article", class_="product_pod")

# Exercício 10
print(f"Quantidade de livros encontrados: {len(livros_html)}")


# FASE 4 Extração de Dados

# Exercício 11
dados_extraidos = []

for livro in livros_html:
    # Exercício 12 Encontrar o título
  
    titulo = livro.h3.a["title"]
    
    # Exercício 13 Encontrar o preço
   
    preco = livro.find("p", class_="price_color").text
    
    # Exercício 14 Criar dicionário e adicionar à lista
    dados_extraidos.append({
        "titulo": titulo,
        "preco": preco
    })

print("\nLista de livros extraídos:")
for item in dados_extraidos:
    print(item)

# FASE 5Salvando o Relatório (CSV)

# Exercício 15
with open("relatorio_livros.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    
    # Exercício 16
    cabecalhos = ["titulo", "preco"]
    gravador = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)
    
    gravador.writeheader()
    gravador.writerows(dados_extraidos)

print("\nRelatório CSV gerado com sucesso!")
