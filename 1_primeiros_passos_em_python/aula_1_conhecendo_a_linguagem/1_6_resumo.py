# resumo_aulas_1_5.py
# Resumo final das aulas 1 a 5 – Python Básico

# --------------------------
# Aula 1: Tipos de dados básicos
# --------------------------

# Tipos numéricos
inteiro = 10         # int
decimal = 3.14       # float
complexo = 2 + 3j    # complex

# Booleanos
verdadeiro = True
falso = False

# Strings
texto = "Olá, mundo!"

# Exemplo de saída
print(inteiro, decimal, complexo)
print(verdadeiro, falso)
print(texto)

# --------------------------
# Aula 2: Modo interativo
# --------------------------
# Tipos de modo interativo:
# 1. Terminal / Prompt Python (>>>)
# 2. IDLE (interface gráfica)
# Também pode usar python -i para rodar scripts e depois continuar interativo
# Permite testar código, fazer contas e experimentar funções rapidamente

# Exemplo com dir()
texto_exemplo = "Python"
print(dir(texto_exemplo))  # mostra todos os métodos disponíveis para a string

# --------------------------
# Aula 3: Variáveis e Constantes
# --------------------------

# Variáveis de diferentes tipos
nome = "Ana"       # string
idade = 20         # int
altura = 1.65      # float
ligado = True      # bool
saldo = 1500.50    # float
ativo = False      # bool

# Alterando valores
idade = 21
nome = "Leo"

print(nome, idade)

# Variáveis de limites e listas
limite_saque = 1000
BRAZILIAN_STATES = ["RS", "SP", "RJ", "SC"]
print(BRAZILIAN_STATES)

# Variáveis podem armazenar resultados de cálculos
total = saldo + limite_saque
print("Total disponível:", total)

# Constantes (convencionalmente maiúsculas)
PI = 3.14159
TAXA = 0.05
MAX_USUARIOS = 1000
DIAS_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

print("PI:", PI)
print("Taxa:", TAXA)
print("Máximo de usuários:", MAX_USUARIOS)
print("Dias da semana:", DIAS_SEMANA)

# --------------------------
# Aula 4: Conversão de tipos
# --------------------------

# Convertendo para inteiro
x = int(3.14)
y = int("10")
print(x, y)

# Convertendo para float
a = float(10)
b = float("10.10")
print(a, b)

# Convertendo para string
valor = 10
valor_str = str(valor)
preco = 3.14
preco_str = str(preco)
print(type(valor), type(valor_str))
print(preco_str)

# Convertendo para booleano
v1 = bool(1)
v2 = bool(0)
v3 = bool("")
v4 = bool("Python")
print(v1, v2, v3, v4)

# Operações que mostram diferenças de conversão
print(100 / 2)   # divisão normal -> float
print(100 // 2)  # divisão inteira -> int

# --------------------------
# Aula 5: Funções de entrada e saída
# --------------------------

# Saída de dados
print("Olá, mundo!")
print(10 + 5)
nome = "Ana"
idade = 20
print("Nome:", nome, "Idade:", idade)
print(f"Nome: {nome}, Idade: {idade}")

# Entrada de dados
usuario = input("Digite seu nome: ")
print("Olá,", usuario)

idade_usuario = int(input("Digite sua idade: "))
altura_usuario = float(input("Digite sua altura: "))
print(f"Idade: {idade_usuario}, Altura: {altura_usuario}")

# Exemplos com diferentes parâmetros do print()
nome = input('Informe seu nome: ')
idade = input("Informe sua idade: ")

print(nome, idade)                   # saída padrão
print(nome, idade, end="...\n")      # mudando final da linha
print(nome, idade, sep="#", end="...\n")  # separador customizado + final de linha
print(nome, idade, sep="#")          # apenas separador customizado

# Observações:
# - 'sep' altera o separador entre os valores do print (padrão: espaço)
# - 'end' altera o que aparece no final do print (padrão: \n)

# --------------------------
# Observações de boas práticas
# --------------------------
# 1. Nomes de variáveis claros e descritivos (ex: nome_aluno, idade_usuario)
# 2. Constantes em letras maiúsculas (PI, TAXA, MAX_USUARIOS)
# 3. Conversão de tipos quando necessário (int(), float(), str(), bool())
# 4. Usar f-strings para formatação de saída, evita concatenação complicada
# 5. Evitar nomes de variáveis iguais a palavras reservadas (if, for, print)
# 6. Testar código pequeno no modo interativo antes de criar scripts maiores
