# --------------------------
# Aula 11 – Gerenciamento de Pacotes, Conversões e Boas Práticas
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

# Exemplo prático (requere instalação de requests):
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

# --------------------------
# 11.2 Conversões de tipos
# --------------------------
# Conversões comuns em Python:
x = "10"
print("String para inteiro:", int(x))

y = "3.14"
print("String para float:", float(y))

num = 42
print("Inteiro para string:", str(num))

valores = ["", "texto", 0, 1]
for v in valores:
    print(f"Valor: {v} → Booleano: {bool(v)}")

lista = [1, 2, 3]
tupla = tuple(lista)
conjunto = set(lista)
print("Lista:", lista)
print("Tupla:", tupla)
print("Conjunto:", conjunto)

# --------------------------
# 11.3 Boas práticas de programação
# --------------------------
# - Nomeação clara de variáveis e funções
# - Comentários explicativos e docstrings
# - Estrutura organizada e modular
# - Evitar repetição (DRY)
# - Tratamento de erros com try/except
# - Usar 'with open()' para arquivos
# - Seguir convenções PEP8

def calcular_media(notas):
    """Retorna a média de uma lista de notas"""
    return sum(notas) / len(notas)

notas = [7, 8, 9]
print("Média das notas:", calcular_media(notas))

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero!")

# --------------------------
# 11.4 Exemplo prático
# --------------------------
def calcular_imposto(produtos, taxa):
    """
    Calcula o valor total de produtos com imposto.
    produtos: lista de dicionários com 'nome' e 'preco'
    taxa: percentual de imposto (0-100)
    """
    total = 0
    for p in produtos:
        preco = float(p["preco"])
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
# 11.5 Desafio Resolvido
# --------------------------
import csv
try:
    # Criar CSV de produtos
    with open("produtos_desafio.csv", "w", newline="", encoding="utf-8") as arq_csv:
        escritor = csv.writer(arq_csv)
        escritor.writerow(["Nome", "Preco", "Quantidade"])
        escritor.writerow(["Caneta", 2.5, 100])
        escritor.writerow(["Lápis", 1.2, 200])
        escritor.writerow(["Caderno", 15.0, 50])
        escritor.writerow(["Borracha", 0.8, 80])
    print("\nArquivo 'produtos_desafio.csv' criado com sucesso!\n")

    # Ler CSV e converter tipos
    produtos = []
    with open("produtos_desafio.csv", "r", encoding="utf-8") as arq_csv:
        leitor = csv.DictReader(arq_csv)
        for linha in leitor:
            produto = {
                "Nome": linha["Nome"],
                "Preco": float(linha["Preco"]),
                "Quantidade": int(linha["Quantidade"])
            }
            produtos.append(produto)

    # Função para calcular valor total do estoque
    def calcular_valor_estoque(produtos):
        """
        Recebe uma lista de produtos e calcula o valor total do estoque.
        """
        total = 0
        for p in produtos:
            total += p["Preco"] * p["Quantidade"]
        return total

    # Exibir resumo
    total_estoque = calcular_valor_estoque(produtos)
    print("📦 Resumo do Estoque:")
    print(f"Total de produtos cadastrados: {len(produtos)}")
    print(f"Valor total do estoque: R$ {total_estoque:.2f}\n")

    print("📋 Produtos cadastrados:")
    for p in produtos:
        print(f"- {p['Nome']}: {p['Quantidade']} unidades a R$ {p['Preco']:.2f} cada")

    # Tabela opcional com prettytable
    try:
        from prettytable import PrettyTable
        tabela = PrettyTable()
        tabela.field_names = ["Nome", "Preço (R$)", "Quantidade", "Subtotal (R$)"]
        for p in produtos:
            tabela.add_row([p["Nome"], f"{p['Preco']:.2f}", p["Quantidade"], f"{p['Preco']*p['Quantidade']:.2f}"])
        print("\n📊 Tabela formatada com PrettyTable:")
        print(tabela)
    except ImportError:
        print("\nPrettyTable não instalado. Para instalar: pip install prettytable")

except Exception as e:
    print("Ocorreu um erro:", e)

# --------------------------
# 11.6 Resumo Final
# --------------------------
# - pip gerencia pacotes: instalar, atualizar e remover bibliotecas
# - Conversões de tipos: int(), float(), str(), bool(), list(), tuple(), set()
# - Boas práticas: funções, docstrings, tratamento de erros, código modular e legível
# - Ambientes virtuais (venv) isolam pacotes por projeto
# - CSV + JSON + pacotes externos são ferramentas comuns em projetos reais
