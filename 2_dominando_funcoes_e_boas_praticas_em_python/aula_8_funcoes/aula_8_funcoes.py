# =================================================================================
# =================================================================================
# =================================================================================

# Aula 8: Funções em Python – Parte 1
# --------------------------

# --------------------------
# 8.1 O que são funções
# --------------------------
# Funções servem para organizar e reutilizar código.
# São definidas com a palavra-chave 'def'.

def saudacao():
    print("Olá! Seja bem-vindo ao curso de Python!")

# Chamando a função
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

# Desempacotando retornos
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
# Variáveis criadas dentro da função são locais.

x = 10  # variável global

def mostrar_valores():
    x = 5  # variável local (diferente da global)
    print("Valor dentro da função:", x)

mostrar_valores()
print("Valor fora da função:", x)

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 8: Funções em Python – Parte 2
# --------------------------

# --------------------------
# 8.8 Argumentos dinâmicos (*args e **kwargs)
# --------------------------

# *args permite passar vários argumentos posicionais
def somar_todos(*numeros):
    soma = sum(numeros)
    print("Soma total:", soma)

somar_todos(1, 2, 3)
somar_todos(5, 10, 15, 20)

# **kwargs permite passar argumentos nomeados (chave=valor)
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

    interna()  # só pode ser chamada dentro da externa

externa()

# --------------------------
# 8.11 Funções Lambda (anônimas)
# --------------------------
# São funções curtas, definidas em uma linha

quadrado = lambda x: x ** 2
print("Quadrado de 5:", quadrado(5))

soma = lambda a, b: a + b
print("Soma 10 + 20:", soma(10, 20))

# --------------------------
# 8.12 Uso de lambda com map(), filter() e sorted()
# --------------------------
numeros = [1, 2, 3, 4, 5]

# map() aplica uma função a todos os elementos
dobrados = list(map(lambda x: x * 2, numeros))
print("Dobro:", dobrados)

# filter() filtra elementos com base em uma condição
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

# sorted() com chave lambda
nomes = ["ana", "Carlos", "bruno", "daniela"]
ordenados = sorted(nomes, key=lambda n: n.lower())
print("Nomes ordenados:", ordenados)

# --------------------------
# 8.13 Documentação de funções (docstrings)
# --------------------------
def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b

print(multiplicar.__doc__)
print("Resultado:", multiplicar(4, 5))

# =================================================================================
# =================================================================================
# =================================================================================

# aula_8_funcoes_parte3.py
# Aula 8: Funções em Python – Parte 3 (Avançado)
# --------------------------

# --------------------------
# 8.14 Funções como objetos
# --------------------------
# Em Python, funções são "cidadãs de primeira classe".
# Isso significa que podemos armazená-las em variáveis,
# passá-las como argumentos e retorná-las de outras funções.

def dobro(x):
    return x * 2

def triplo(x):
    return x * 3

# Armazenando funções em uma lista
operacoes = [dobro, triplo]

for func in operacoes:
    print(func(5))  # chama cada função passando 5


# --------------------------
# 8.15 Funções que recebem funções
# --------------------------
def aplicar_operacao(funcao, valor):
    return funcao(valor)

print(aplicar_operacao(dobro, 10))   # 20
print(aplicar_operacao(triplo, 10))  # 30


# --------------------------
# 8.16 Funções internas com retorno (closures)
# --------------------------
# Uma closure é quando uma função interna "lembra" o contexto
# da função externa, mesmo após ela ter sido executada.

def saudacao_personalizada(prefixo):
    def mensagem(nome):
        return f"{prefixo}, {nome}!"
    return mensagem  # retorna a função interna

ola = saudacao_personalizada("Olá")
print(ola("Carlos"))   # "Olá, Carlos!"
print(ola("Maria"))    # "Olá, Maria!"


# --------------------------
# 8.17 Funções recursivas
# --------------------------
# São funções que chamam a si mesmas.
# Precisam de uma condição de parada para evitar loop infinito.

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))


# --------------------------
# 8.18 Decoradores
# --------------------------
# Decoradores são funções que "envolvem" outras funções,
# adicionando funcionalidades sem alterar o código original.

def decorador(funcao):
    def nova_funcao():
        print("Antes da função...")
        funcao()
        print("Depois da função...")
    return nova_funcao

@decorador
def saudacao():
    print("Olá, mundo!")

saudacao()


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
def mensagem():
    print("Executando...")

mensagem()

# =================================================================================
# =================================================================================
# =================================================================================

# --------------------------
# 8.20 Funções internas úteis (built-ins)
# --------------------------
# Algumas funções úteis que podem receber outras funções:
# - map(), filter(), sorted(), reduce(), all(), any()

from functools import reduce

numeros = [1, 2, 3, 4, 5]

soma = reduce(lambda a, b: a + b, numeros)
print("Soma com reduce:", soma)

print("Todos são positivos?", all(n > 0 for n in numeros))
print("Algum é par?", any(n % 2 == 0 for n in numeros))

# =================================================================================
# =================================================================================
# =================================================================================
