# aula_9_resumo.py
# Resumo completo da Aula 9: Decoradores, Iteradores e Geradores
# --------------------------

# --------------------------
# Parte 1 e 2: Decoradores
# --------------------------

# Decoradores são funções que "decoram" outras funções, adicionando comportamento extra.

# Decorador simples
def meu_decorador(funcao):
    def wrapper():
        print("Antes da função ser executada.")
        funcao()
        print("Depois da função ser executada.")
    return wrapper

@meu_decorador
def saudacao():
    print("Olá!")

saudacao()

# Decorador com argumentos
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

# Decoradores aninhados
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

print(mensagem())  # PYTHON É LEGAL!!!

# --------------------------
# Parte 3: Iteradores
# --------------------------

# Iteradores permitem percorrer elementos um a um usando __iter__() e __next__()

numeros = [1, 2, 3, 4, 5]
iterador = iter(numeros)

print(next(iterador))  # 1
print(next(iterador))  # 2

# Loop for usa iteradores automaticamente
for n in numeros:
    print(n)

# Iterador personalizado
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
# Parte 4: Geradores
# --------------------------

# Geradores retornam valores sob demanda usando yield
def gerador_numeros(n):
    for i in range(n):
        yield i

gen = gerador_numeros(5)
print(next(gen))
print(next(gen))

for numero in gerador_numeros(5):
    print(numero)

# Gerador infinito
def contador_infinito():
    i = 0
    while True:
        yield i
        i += 1

cont = contador_infinito()
print(next(cont))
print(next(cont))

# Gerador filtrando pares
def pares_ate(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

for p in pares_ate(10):
    print(p)

# Expressão geradora
numeros_quad = (x ** 2 for x in range(5))
for n in numeros_quad:
    print(n)

# --------------------------
# Parte 5: Desafio Resolvido
# --------------------------

# Decorador mostrando execução
def mostrar_execucao(funcao):
    def wrapper(*args, **kwargs):
        print(f"Iniciando '{funcao.__name__}'...")
        resultado = funcao(*args, **kwargs)
        print(f"'{funcao.__name__}' finalizada.")
        return resultado
    return wrapper

# Iterador personalizado contando chamadas
class ContadorChamadas:
    def __init__(self):
        self.contador = 0
    def incrementar(self):
        self.contador += 1
        return self.contador

contador = ContadorChamadas()

# Gerador de números pares
def gerar_pares(limite):
    for i in range(limite + 1):
        if i % 2 == 0:
            yield i

# Função combinando tudo
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
