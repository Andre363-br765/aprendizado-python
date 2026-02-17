# Aula 10: Desafio e Desafio Resolvido – Manipulação de Arquivos (CSV e JSON)
# --------------------------

# --------------------------
# Aula 10.3 – Desafio
# --------------------------
# Crie um programa que:
# 1. Leia um arquivo CSV com informações de produtos (nome, preço, quantidade).
# 2. Converta esses dados em um dicionário e grave em um arquivo JSON.
# 3. Leia o JSON gerado e exiba um resumo com o total de produtos e o valor total em estoque.

# Arquivo CSV exemplo:
# Nome,Preco,Quantidade
# Caneta,2.5,100
# Lápis,1.2,200
# Caderno,15.0,50
# Borracha,0.8,80

# --------------------------
# Aula 10.3 – Desafio Resolvido
# --------------------------

import csv
import json

# --------------------------
# 1. Criar arquivo CSV com dados de exemplo
# --------------------------
with open("produtos.csv", "w", newline="", encoding="utf-8") as arq_csv:
    escritor = csv.writer(arq_csv)
    escritor.writerow(["Nome", "Preco", "Quantidade"])
    escritor.writerow(["Caneta", 2.5, 100])
    escritor.writerow(["Lápis", 1.2, 200])
    escritor.writerow(["Caderno", 15.0, 50])
    escritor.writerow(["Borracha", 0.8, 80])

print("Arquivo 'produtos.csv' criado com sucesso!\n")

# --------------------------
# 2. Ler o arquivo CSV e converter para lista de dicionários
# --------------------------
produtos = []

with open("produtos.csv", "r", encoding="utf-8") as arq_csv:
    leitor = csv.DictReader(arq_csv)
    for linha in leitor:
        produto = {
            "Nome": linha["Nome"],
            "Preco": float(linha["Preco"]),
            "Quantidade": int(linha["Quantidade"])
        }
        produtos.append(produto)

# --------------------------
# 3. Gravar os dados no formato JSON
# --------------------------
with open("produtos.json", "w", encoding="utf-8") as arq_json:
    json.dump(produtos, arq_json, ensure_ascii=False, indent=4)

print("Arquivo 'produtos.json' criado com sucesso!\n")

# --------------------------
# 4. Ler o arquivo JSON e exibir resumo
# --------------------------
with open("produtos.json", "r", encoding="utf-8") as arq_json:
    dados = json.load(arq_json)

total_itens = sum(p["Quantidade"] for p in dados)
valor_total = sum(p["Preco"] * p["Quantidade"] for p in dados)

print("Resumo do estoque:")
print(f"Total de produtos cadastrados: {len(dados)}")
print(f"Total de itens no estoque: {total_itens}")
print(f"Valor total em estoque: R$ {valor_total:.2f}")

print("\nProdutos cadastrados:")
for p in dados:
    print(f"- {p['Nome']}: {p['Quantidade']} unidades a R$ {p['Preco']:.2f} cada")
