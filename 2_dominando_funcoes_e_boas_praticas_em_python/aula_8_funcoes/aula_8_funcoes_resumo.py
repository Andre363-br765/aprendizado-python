# aula_8_resumo.py
# Resumo completo da Aula 8: Funções em Python (Partes 1, 2 e 3)
# --------------------------

# --------------------------
# 8.1 O que são funções
# --------------------------
def saudacao():
    print("Olá! Seja bem-vindo ao curso de Python!")

saudacao()

# --------------------------
# 8.2 Funções com parâmetros
# --------------------------
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

saudacao_personalizada("Ana")
saudacao_personalizada("Bruno")

# --------------------------
# 8.3 Funções com múltiplos parâmetros
# --------------------------
def soma(a, b):
    resultado = a + b
    print(f"A soma de {a} + {b} é {resultado}")

soma(5, 3)
soma(10, 20)

# --------------------------
# 8.4 Funções com retorno de valor
# --------------------------
def quadrado(numero):
    return numero ** 2

resultado = quadrado(4)
print("O quadrado de 4 é:", resultado)

# --------------------------
# 8.5 Retornando múltiplos valores
# --------------------------
def operacoes(a, b):
    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return soma, sub, mult, div

res = operacoes(10, 2)
print("Resultados:", res)

soma_r, sub_r, mult_r, div_r = operacoes(6, 3)
print(f"Soma: {soma_r}, Sub: {sub_r}, Mult: {mult_r}, Div: {div_r}")

# --------------------------
# 8.6 Funções com valor padrão
# --------------------------
def apresentar(nome="Visitante"):
    print(f"Olá, {nome}!")

apresentar("Carla")
apresentar()  # usa o valor padrão

# --------------------------
# 8.7 Escopo de variáveis
# --------------------------
x = 10  # variável global

def mostrar_valores():
    x = 5  # variável local
    print("Valor dentro da função:", x)

mostrar_valores()
print("Valor fora da função:", x)

# --------------------------
# 8.8 Argumentos dinâmicos (*args e **kwargs)
# --------------------------
def somar_todos(*numeros):
    soma = sum(numeros)
    print("Soma total:", soma)

somar_todos(1, 2, 3)
somar_todos(5, 10, 15, 20)

def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Ana", idade=20, curso="Python")

# --------------------------
# 8.9 Misturando argumentos normais, *args e **kwargs
# --------------------------
def exemplo(a, b=0, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print("args:", args)
    print("kwargs:", kwargs)

exemplo(1, 2, 3, 4, x=10, y=20)

# --------------------------
# 8.10 Funções aninhadas
# --------------------------
def externa():
    print("Função externa chamada.")

    def interna():
        print("Função interna chamada.")

    interna()

externa()

# --------------------------
# 8.11 Funções Lambda (anônimas)
# --------------------------
quadrado = lambda x: x ** 2
print("Quadrado de 5:", quadrado(5))

soma = lambda a, b: a + b
print("Soma 10 + 20:", soma(10, 20))

# --------------------------
# 8.12 Uso de lambda com map(), filter() e sorted()
# --------------------------
numeros = [1, 2, 3, 4, 5]

dobrados = list(map(lambda x: x * 2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
ordenados = sorted(["ana", "Carlos", "bruno", "daniela"], key=lambda n: n.lower())

print("Dobro:", dobrados)
print("Pares:", pares)
print("Nomes ordenados:", ordenados)

# --------------------------
# 8.13 Documentação de funções (docstrings)
# --------------------------
def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b

print(multiplicar.__doc__)
print("Resultado:", multiplicar(4, 5))

# --------------------------
# 8.14 Funções como objetos
# --------------------------
def dobro(x):
    return x * 2

def triplo(x):
    return x * 3

operacoes = [dobro, triplo]
for func in operacoes:
    print(func(5))

# --------------------------
# 8.15 Funções que recebem funções
# --------------------------
def aplicar_operacao(funcao, valor):
    return funcao(valor)

print(aplicar_operacao(dobro, 10))
print(aplicar_operacao(triplo, 10))

# --------------------------
# 8.16 Funções internas com retorno (closures)
# --------------------------
def saudacao_personalizada(prefixo):
    def mensagem(nome):
        return f"{prefixo}, {nome}!"
    return mensagem

ola = saudacao_personalizada("Olá")
print(ola("Carlos"))
print(ola("Maria"))

# --------------------------
# 8.17 Funções recursivas
# --------------------------
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))

# --------------------------
# 8.18 Decoradores
# --------------------------
def decorador(funcao):
    def nova_funcao():
        print("Antes da função...")
        funcao()
        print("Depois da função...")
    return nova_funcao

@decorador
def saudacao_decorada():
    print("Olá, mundo!")

saudacao_decorada()

# --------------------------
# 8.19 Decoradores com parâmetros
# --------------------------
def repetir_vezes(vezes):
    def decorador(funcao):
        def nova_funcao():
            for _ in range(vezes):
                funcao()
        return nova_funcao
    return decorador

@repetir_vezes(3)
def mensagem_repetida():
    print("Executando...")

mensagem_repetida()

# --------------------------
# 8.20 Funções internas úteis (built-ins)
# --------------------------
from functools import reduce

numeros = [1, 2, 3, 4, 5]

soma_total = reduce(lambda a, b: a + b, numeros)
print("Soma com reduce:", soma_total)
print("Todos são positivos?", all(n > 0 for n in numeros))
print("Algum é par?", any(n % 2 == 0 for n in numeros))