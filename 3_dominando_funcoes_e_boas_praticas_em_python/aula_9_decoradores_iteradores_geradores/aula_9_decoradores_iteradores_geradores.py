# =================================================================================
# =================================================================================
# =================================================================================

# Aula 9: Decoradores em Python (Parte 1 e Parte 2)

# --------------------------
# O que são Decoradores
# --------------------------
# Decoradores são funções que "decoram" outras funções,
# ou seja, permitem adicionar comportamentos extras sem alterar o código original.

# Exemplo simples de função normal:
def saudacao():
    print("Olá!")

# Exemplo de decorador:
def meu_decorador(funcao):
    def wrapper():
        print("Antes da função ser executada.")
        funcao()
        print("Depois da função ser executada.")
    return wrapper

# Aplicando o decorador manualmente
funcao_decorada = meu_decorador(saudacao)
funcao_decorada()

# --------------------------
# Usando a sintaxe @decorador
# --------------------------
# Forma mais prática e comum de usar decoradores:
@meu_decorador
def despedida():
    print("Tchau!")

despedida()

# --------------------------
# Decoradores com argumentos
# --------------------------
def decorador_com_args(funcao):
    def wrapper(*args, **kwargs):
        print(f"Executando {funcao.__name__} com argumentos: {args} {kwargs}")
        resultado = funcao(*args, **kwargs)
        print("Execução finalizada.")
        return resultado
    return wrapper

@decorador_com_args
def soma(a, b):
    return a + b

print("Resultado:", soma(5, 3))

# --------------------------
# Decoradores aninhados (vários decoradores)
# --------------------------
def maiusculas(funcao):
    def wrapper():
        texto = funcao()
        return texto.upper()
    return wrapper

def adiciona_exclamacao(funcao):
    def wrapper():
        texto = funcao()
        return texto + "!!!"
    return wrapper

@adiciona_exclamacao
@maiusculas
def mensagem():
    return "python é legal"

print(mensagem())  # Saída: PYTHON É LEGAL!!!

# --------------------------
# Resumo
# --------------------------
# - Decoradores são funções que modificam o comportamento de outras funções.
# - Podem ser aplicados com @nome_do_decorador.
# - Podem receber parâmetros usando *args e **kwargs.
# - Podem ser combinados (decoradores empilhados).

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 9.2: Iteradores em Python

# --------------------------
# O que são Iteradores
# --------------------------
# Iteradores são objetos que permitem percorrer elementos de uma coleção
# um a um, sem precisar acessar índices diretamente.
# Todo iterador implementa os métodos __iter__() e __next__().

# --------------------------
# Criando e usando iteradores
# --------------------------
# Exemplo com lista
numeros = [1, 2, 3, 4, 5]

# Transformando a lista em iterador
iterador = iter(numeros)

# Usando next() para percorrer elementos
print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3
print(next(iterador))  # 4
print(next(iterador))  # 5
# print(next(iterador))  # StopIteration se ultrapassar o final

# --------------------------
# Iterando com loop for
# --------------------------
# O loop for já utiliza iteradores internamente
for n in numeros:
    print(n)

# --------------------------
# Criando um iterador personalizado
# --------------------------
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.limite:
            numero = self.atual
            self.atual += 1
            return numero
        else:
            raise StopIteration

contador = Contador(5)
for n in contador:
    print(n)

# --------------------------
# Resumo
# --------------------------
# - Iterador permite percorrer elementos um a um.
# - Usamos iter() para criar um iterador a partir de um objeto iterável.
# - Usamos next() para acessar o próximo elemento.
# - Loops for usam iteradores automaticamente.
# - Podemos criar iteradores personalizados implementando __iter__() e __next__().

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 9.3: Geradores em Python

# --------------------------
# O que são Geradores
# --------------------------
# Geradores são funções que retornam um iterador de forma preguiçosa (lazy evaluation),
# ou seja, os valores são gerados apenas quando solicitados.
# Usam a palavra-chave `yield` ao invés de `return`.

# --------------------------
# Exemplo simples de gerador
# --------------------------
def gerador_numeros(n):
    for i in range(n):
        yield i  # devolve o valor, mas mantém o estado da função

gen = gerador_numeros(5)

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# Continuar chamando next() até StopIteration

# --------------------------
# Iterando com loop for
# --------------------------
for numero in gerador_numeros(5):
    print(numero)

# --------------------------
# Gerador infinito
# --------------------------
# Pode gerar valores infinitamente sem ocupar muita memória
def contador_infinito():
    i = 0
    while True:
        yield i
        i += 1

cont = contador_infinito()
print(next(cont))  # 0
print(next(cont))  # 1
print(next(cont))  # 2

# --------------------------
# Combinando geradores com funções
# --------------------------
def pares_ate(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

for p in pares_ate(10):
    print(p)

# --------------------------
# Expressões geradoras (Generator Expressions)
# --------------------------
# Semelhante às listas, mas gera os valores sob demanda
numeros = (x ** 2 for x in range(5))

for n in numeros:
    print(n)

# --------------------------
# Vantagens dos Geradores
# --------------------------
# - Economia de memória (não cria toda a lista na memória)
# - Valores gerados sob demanda
# - Úteis para grandes sequências ou streams de dados

# --------------------------
# Resumo
# --------------------------
# - Funções com yield retornam um iterador gerador.
# - Geradores podem ser percorridos com next() ou for.
# - Suportam loops infinitos de forma eficiente.
# - Generator expressions são uma forma compacta de criar geradores.

# =================================================================================
# =================================================================================
# =================================================================================

# aula_9_desafio.py
# Aula 9.4 e 9.5: Desafio e Desafio Resolvido – Decoradores, Iteradores e Geradores

# --------------------------
# Aula 9.4: Desafio
# --------------------------
# Crie um programa que combine:
# 1. Um decorador que mostre a execução de uma função.
# 2. Um gerador que gere números pares até um limite informado.
# 3. Um iterador personalizado que conte quantas vezes a função foi chamada.

# Escreva o código para implementar essas funcionalidades.

# --------------------------
# Aula 9.5: Desafio Resolvido
# --------------------------

# Decorador que mostra execução
def mostrar_execucao(funcao):
    def wrapper(*args, **kwargs):
        print(f"Iniciando '{funcao.__name__}'...")
        resultado = funcao(*args, **kwargs)
        print(f"'{funcao.__name__}' finalizada.")
        return resultado
    return wrapper

# Iterador personalizado para contar chamadas
class ContadorChamadas:
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1
        return self.contador

contador = ContadorChamadas()

# Gerador que produz números pares até um limite
def gerar_pares(limite):
    for i in range(limite + 1):
        if i % 2 == 0:
            yield i

# Função que combina tudo
@mostrar_execucao
def processar_pares(limite):
    print(f"Chamada número: {contador.incrementar()}")
    for n in gerar_pares(limite):
        print(n, end=" ")
    print()  # nova linha

# Chamadas de teste
processar_pares(10)
processar_pares(6)
processar_pares(8)

# --------------------------
# Resumo do desafio
# --------------------------
# - Decoradores: adiciona comportamento extra (mostrar início/fim da função)
# - Iteradores personalizados: contador de chamadas
# - Geradores: números pares gerados sob demanda
# - Combinação de conceitos da Aula 9 para prática
