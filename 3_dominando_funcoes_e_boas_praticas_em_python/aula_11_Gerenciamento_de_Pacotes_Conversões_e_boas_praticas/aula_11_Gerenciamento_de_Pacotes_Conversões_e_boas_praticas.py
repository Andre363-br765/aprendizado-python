# Aula 11: Gerenciamento de Pacotes, Conversões e Boas Práticas
# --------------------------

# --------------------------
# 11.1 Gerenciamento de Pacotes
# --------------------------
# Python utiliza pacotes para reutilização de código. Pacotes podem ser bibliotecas externas instaladas via pip.

# Exemplos de comandos pip (executar no terminal):
# pip install requests        → instala o pacote requests
# pip install --upgrade requests → atualiza o pacote
# pip uninstall requests      → desinstala o pacote
# pip list                    → lista pacotes instalados

# Exemplo prático com requests (necessário instalar via pip)
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

# --------------------------
# 11.2 Conversões de tipos
# --------------------------
# Python é dinamicamente tipado, mas conversões são necessárias em várias situações.

# Conversão de string para inteiro
s = "123"
i = int(s)
print(f"String '{s}' para inteiro: {i}")

# Conversão de string para float
f = float("3.14")
print("String '3.14' para float:", f)

# Conversão de inteiro para string
num = 42
s_num = str(num)
print("Inteiro 42 para string:", s_num)

# Conversão para booleano
valores = ["", "texto", 0, 1]
for v in valores:
    print(f"Valor: {v} → Booleano: {bool(v)}")

# Conversão entre listas, tuplas e conjuntos
lista = [1, 2, 3]
tupla = tuple(lista)
conjunto = set(lista)
print("Lista:", lista)
print("Tupla:", tupla)
print("Conjunto:", conjunto)

# --------------------------
# 11.3 Boas práticas de programação
# --------------------------

# 1. Nomeação clara
nome_aluno = "Ana"
def calcular_media(notas):
    """Retorna a média de uma lista de notas"""
    return sum(notas) / len(notas)

# 2. Comentários explicativos e docstrings
notas = [7, 8, 9]
media = calcular_media(notas)
print(f"Média das notas: {media}")

# 3. Estrutura de código organizada
def saudacao(nome):
    """Exibe saudação personalizada"""
    print(f"Olá, {nome}!")

saudacao("Bruno")

# 4. Evitar repetição de código (DRY)
def imprimir_lista(lista):
    for item in lista:
        print(item)

itens = ["caneta", "caderno", "lapis"]
imprimir_lista(itens)

# 5. Tratamento de erros
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero!")

# 6. Usar 'with open' para arquivos
with open("exemplo.txt", "w", encoding="utf-8") as arq:
    arq.write("Exemplo de boas práticas com arquivos.")

# 7. Seguir PEP8
# nomes de funções em snake_case
# nomes de classes em CamelCase
# 4 espaços por indentação

# --------------------------
# 11.4 Dicas adicionais
# --------------------------
# - Modularize seu código em arquivos e pastas
# - Documente funções com docstrings
# - Teste seu código com entradas diferentes
# - Use ambientes virtuais (venv) para gerenciar dependências

# Criando e ativando ambiente virtual (terminal):
# python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
# Depois instale pacotes apenas nesse ambiente

# --------------------------
# 11.5 Exemplo prático combinando conceitos
# --------------------------
# Usando pacotes, conversões e boas práticas juntos

# Função que calcula imposto sobre produtos
def calcular_imposto(produtos, taxa):
    """
    Calcula o valor total de produtos com imposto.
    produtos: lista de dicionários com 'nome' e 'preco'
    taxa: percentual de imposto (0-100)
    """
    total = 0
    for p in produtos:
        preco = float(p["preco"])  # conversão para float
        total += preco + (preco * taxa / 100)
    return total

produtos = [
    {"nome": "Caneta", "preco": "2.5"},
    {"nome": "Caderno", "preco": "15.0"},
    {"nome": "Borracha", "preco": "0.8"}
]

total_imposto = calcular_imposto(produtos, 10)
print(f"Total com imposto: R$ {total_imposto:.2f}")

# --------------------------
# 11.6 Resumo detalhado
# --------------------------
# - pip gerencia pacotes: instalar, atualizar e remover bibliotecas
# - Conversões: int(), float(), str(), bool(), list(), tuple(), set()
# - Boas práticas:
#    * Nomeação clara
#    * Comentários e docstrings
#    * Estrutura organizada e modular
#    * DRY (não repetir código)
#    * Tratamento de erros
#    * Seguir PEP8
#    * Usar 'with open()' para arquivos
# - Ambientes virtuais isolam pacotes por projeto
