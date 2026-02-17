# =================================================================================
# =================================================================================
# =================================================================================

# Aula 10: Manipulação de Arquivos em Python
# --------------------------

# --------------------------
# 10.1 Introdução
# --------------------------
# Python permite criar, ler e escrever arquivos facilmente usando a função open().
# A função open() retorna um objeto do tipo arquivo.
# Sintaxe: open("nome_arquivo", "modo")

# Modos comuns:
# "r" → leitura (read)
# "w" → escrita (write) – apaga o conteúdo anterior
# "a" → acrescentar (append) – adiciona sem apagar
# "r+" → leitura e escrita

# --------------------------
# 10.2 Criando e escrevendo em um arquivo
# --------------------------
arquivo = open("exemplo.txt", "w")  # cria ou substitui
arquivo.write("Olá, mundo!\n")
arquivo.write("Esta é a primeira linha gravada com Python.\n")
arquivo.close()  # sempre feche o arquivo

# --------------------------
# 10.3 Lendo o conteúdo de um arquivo
# --------------------------
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print("Conteúdo do arquivo:")
print(conteudo)
arquivo.close()

# --------------------------
# 10.4 Lendo linha por linha
# --------------------------
arquivo = open("exemplo.txt", "r")
for linha in arquivo:
    print("Linha:", linha.strip())  # strip remove quebras de linha extras
arquivo.close()

# --------------------------
# 10.5 Acrescentando (sem apagar o conteúdo)
# --------------------------
arquivo = open("exemplo.txt", "a")
arquivo.write("Nova linha adicionada!\n")
arquivo.close()

# --------------------------
# 10.6 Usando 'with open' (método recomendado)
# --------------------------
# O 'with' fecha o arquivo automaticamente, mesmo se ocorrer erro.
with open("exemplo.txt", "r") as arq:
    for linha in arq:
        print("->", linha.strip())

# --------------------------
# 10.7 Lendo arquivos grandes com eficiência
# --------------------------
# Em vez de ler tudo de uma vez, leia linha por linha:
with open("exemplo.txt", "r") as arq:
    linha = arq.readline()
    while linha:
        print(linha.strip())
        linha = arq.readline()

# --------------------------
# 10.8 Resumo
# --------------------------
# - open("arquivo", "modo") → abre o arquivo
# - write() → escreve
# - read() → lê tudo
# - readline() / readlines() → lê linha(s)
# - "w" substitui, "a" acrescenta
# - with open() é a forma mais segura e moderna

# =================================================================================
# =================================================================================
# =================================================================================

# aula_10_2_csv_json.py
# Aula 10.2: Leitura e Escrita de Arquivos CSV e JSON
# --------------------------

# --------------------------
# 10.2.1 Trabalhando com arquivos CSV
# --------------------------
# CSV (Comma-Separated Values) é um formato muito usado para tabelas (como planilhas Excel).
# Python possui o módulo csv para ler e escrever arquivos nesse formato.

import csv

# --------------------------
# Escrevendo em um arquivo CSV
# --------------------------
with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["Ana", 25, "São Paulo"])
    escritor.writerow(["Bruno", 30, "Rio de Janeiro"])
    escritor.writerow(["Carla", 22, "Curitiba"])

print("Arquivo CSV criado com sucesso!")

# --------------------------
# Lendo um arquivo CSV
# --------------------------
with open("dados.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)

# --------------------------
# Lendo CSV com cabeçalhos (usando DictReader)
# --------------------------
with open("dados.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        print(f"{linha['Nome']} tem {linha['Idade']} anos e mora em {linha['Cidade']}.")

# --------------------------
# 10.2.2 Trabalhando com arquivos JSON
# --------------------------
# JSON (JavaScript Object Notation) é muito usado para armazenar dados estruturados.
# O Python tem o módulo 'json' para manipular facilmente esse formato.

import json

# --------------------------
# Criando um dicionário em Python
# --------------------------
dados = {
    "nome": "Alice",
    "idade": 28,
    "cidades": ["São Paulo", "Campinas", "Santos"],
    "ativo": True
}

# --------------------------
# Gravando em um arquivo JSON
# --------------------------
with open("dados.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)

print("Arquivo JSON criado com sucesso!")

# --------------------------
# Lendo um arquivo JSON
# --------------------------
with open("dados.json", "r", encoding="utf-8") as arquivo_json:
    conteudo = json.load(arquivo_json)
    print(conteudo)
    print("Nome:", conteudo["nome"])
    print("Cidades:", conteudo["cidades"])

# --------------------------
# Convertendo entre Python e JSON
# --------------------------
# dump()  → grava em arquivo JSON
# dumps() → converte para string JSON
# load()  → lê arquivo JSON
# loads() → lê string JSON

json_str = json.dumps(dados, ensure_ascii=False, indent=4)
print("JSON em formato de string:")
print(json_str)

# --------------------------
# Resumo
# --------------------------
# - Módulo csv → usado para dados tabulares (como planilhas)
# - Módulo json → usado para dados estruturados
# - csv.writer / csv.reader → grava e lê linhas
# - json.dump() / json.load() → grava e lê arquivos JSON
# - with open() → sempre recomendável para lidar com arquivos

# =================================================================================
# =================================================================================
# =================================================================================