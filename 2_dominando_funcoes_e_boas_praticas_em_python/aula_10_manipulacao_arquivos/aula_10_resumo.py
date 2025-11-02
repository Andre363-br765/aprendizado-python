# aula_10_resumo.py
# --------------------------
# Aula 10 – Manipulação de Arquivos em Python (TXT, CSV e JSON)
# --------------------------
# Resumo completo das aulas:
# 10.1 – Leitura e Escrita em Arquivos de Texto
# 10.2 – Manipulação de Arquivos CSV
# 10.3 – Manipulação de Arquivos JSON + Desafio

# --------------------------------------------------
# 📘 AULA 10.1 – Arquivos de Texto (TXT)
# --------------------------------------------------

# Escrever em um arquivo de texto
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Olá, mundo!\n")
    arquivo.write("Linha 2: Aprendendo manipulação de arquivos em Python.\n")

# Ler o conteúdo do arquivo
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print("📄 Conteúdo do arquivo de texto:")
print(conteudo)

# --------------------------------------------------
# 📘 AULA 10.2 – Arquivos CSV (Planilhas)
# --------------------------------------------------
import csv

# Criar um arquivo CSV
with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["Ana", 25, "São Paulo"])
    escritor.writerow(["Bruno", 30, "Rio de Janeiro"])
    escritor.writerow(["Clara", 22, "Belo Horizonte"])

print("\n✅ Arquivo 'dados.csv' criado com sucesso!\n")

# Ler o arquivo CSV
with open("dados.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    print("📊 Dados do arquivo CSV:")
    for linha in leitor:
        print(linha)

# --------------------------------------------------
# 📘 AULA 10.3 – Arquivos JSON
# --------------------------------------------------
import json

# Criar um dicionário de exemplo
dados = {
    "nome": "Alice",
    "idade": 28,
    "cidades": ["São Paulo", "Curitiba", "Florianópolis"]
}

# Gravar no formato JSON
with open("dados.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)

print("\n✅ Arquivo 'dados.json' criado com sucesso!\n")

# Ler o arquivo JSON
with open("dados.json", "r", encoding="utf-8") as arquivo_json:
    conteudo_json = json.load(arquivo_json)

print("📘 Conteúdo do JSON:")
print(conteudo_json)

# --------------------------------------------------
# 💪 DESAFIO FINAL – Manipulação Completa (CSV + JSON)
# --------------------------------------------------
# Desafio: Ler dados de um arquivo CSV de produtos, salvar como JSON e mostrar resumo do estoque.

# Criar arquivo CSV de produtos
with open("produtos.csv", "w", newline="", encoding="utf-8") as arq_csv:
    escritor = csv.writer(arq_csv)
    escritor.writerow(["Nome", "Preco", "Quantidade"])
    escritor.writerow(["Caneta", 2.5, 100])
    escritor.writerow(["Lápis", 1.2, 200])
    escritor.writerow(["Caderno", 15.0, 50])
    escritor.writerow(["Borracha", 0.8, 80])

print("\n✅ Arquivo 'produtos.csv' criado para o desafio!\n")

# Ler o CSV e converter em lista de dicionários
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

# Gravar os dados no formato JSON
with open("produtos.json", "w", encoding="utf-8") as arq_json:
    json.dump(produtos, arq_json, ensure_ascii=False, indent=4)

print("✅ Arquivo 'produtos.json' criado a partir do CSV!\n")

# Ler o JSON e exibir resumo
with open("produtos.json", "r", encoding="utf-8") as arq_json:
    dados = json.load(arq_json)

total_itens = sum(p["Quantidade"] for p in dados)
valor_total = sum(p["Preco"] * p["Quantidade"] for p in dados)

print("📦 RESUMO DO ESTOQUE:")
print(f"Total de produtos cadastrados: {len(dados)}")
print(f"Total de itens no estoque: {total_itens}")
print(f"Valor total em estoque: R$ {valor_total:.2f}\n")

print("📋 PRODUTOS CADASTRADOS:")
for p in dados:
    print(f"- {p['Nome']}: {p['Quantidade']} unidades a R$ {p['Preco']:.2f} cada")

# --------------------------------------------------
# 🧠 RESUMO GERAL DA AULA 10
# --------------------------------------------------
# - 'open()' abre arquivos (modo 'r' = leitura, 'w' = escrita, 'a' = adicionar)
# - CSV usa vírgulas para separar dados → ideal para planilhas.
# - JSON armazena dados estruturados → ideal para APIs e configurações.
# - Bibliotecas: csv e json são padrão no Python (não precisa instalar).
# - Sempre use 'with open()' para abrir arquivos → fecha automaticamente.
# - Convertendo formatos: CSV ↔ JSON é comum em projetos reais.
