# Aula 3.1 – Conceitos básicos de indentação em Python
# ----------------------------------------------------
# Objetivo: Entender o que é indentação e como ela define blocos de código em Python.

# -----------------------
# Exemplo 1: indentação simples
print("Início do programa")  # nível 0 (sem espaços)
# Observação: Código fora de qualquer bloco está no nível 0

# -----------------------
# Exemplo 2: indentação dentro de função
def minha_funcao():           # nível 0 (def inicia um bloco)
    print("Dentro da função")  # nível 1 (4 espaços)
    # Observação: todo código dentro da função deve ter a mesma indentação

# Chamando a função
minha_funcao()  # nível 0

# -----------------------
# Exemplo 3: indentação em if
if True:                      # nível 0
    print("Dentro do if")      # nível 1 (4 espaços)
    # Observação: bloco do if começa após ":" e tudo que estiver indentado pertence a ele

print("Fora do if")            # nível 0
# Observação: volta ao nível anterior após terminar o bloco

# -----------------------
# Checklist básico de indentação
# 1. Cada nível de bloco adiciona 4 espaços
# 2. Todos os comandos do mesmo bloco devem ter a mesma indentação
# 3. Todo bloco iniciado com ":" precisa de indentação
# 4. Voltar ao nível do bloco anterior ao terminar sub-bloco
# 5. Não misturar tabs e espaços

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 3.2 – Indentação e Blocos em Python
# -----------------------------------------
# Objetivo: Entender como os blocos de código funcionam, níveis de indentação e sub-blocos.

# -----------------------
# Exemplo 1: função com bloco simples
def funcao_exemplo():        # nível 0 (sem espaços)  -> início do bloco da função
    print("Início")           # nível 1 (4 espaços)   -> corpo da função
    # Observação: tudo que está dentro do def pertence ao bloco da função

# -----------------------
# Exemplo 2: if dentro da função (sub-bloco)
def funcao_condicional(x):
    if x > 0:                 # nível 1 (4 espaços)  -> bloco do if
        print("x é positivo") # nível 2 (8 espaços) -> sub-bloco do if
    else:
        print("x não é positivo") # nível 2 (8 espaços)
    print("Fim do if")        # nível 1 (4 espaços)  -> volta ao nível da função

# -----------------------
# Exemplo 3: for dentro do if (sub-sub-bloco)
def funcao_loops():
    for i in range(3):        # nível 1 (4 espaços) -> bloco do for
        print(f"Loop principal: {i}")
        for j in range(2):    # nível 2 (8 espaços) -> sub-bloco do for
            print(f"  Sub-loop: {j}")  # nível 3 (12 espaços)

# -----------------------
# Observações gerais sobre blocos:
# 1. Cada bloco inicia após ":" e precisa de indentação
# 2. Sub-blocos adicionam 4 espaços por nível
# 3. Todos os comandos do mesmo bloco devem alinhar horizontalmente
# 4. Ao terminar um bloco, voltar ao nível anterior
# 5. Misturar tabs e espaços causa erro (IndentationError)

# -----------------------
# Exercício rápido:
# Crie uma função com um if dentro de um for, e coloque um print fora do if.
# Verifique se os níveis de indentação estão corretos.

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 3.3 – Estrutura Condicional em Python
# -----------------------------------------
# Objetivo: Entender como funcionam if, elif e else, e como organizar blocos aninhados.

# -----------------------
# Exemplo 1: if simples
x = 10
if x > 0:                   # bloco if (nível 0 ou 1 dentro de função)
    print("x é positivo")    # nível 1 (4 espaços)
# Observação: tudo dentro do if precisa de indentação

# -----------------------
# Exemplo 2: if com else
x = -5
if x > 0:                   
    print("x é positivo")    # nível 1
else:
    print("x não é positivo") # nível 1
# Observação: else sempre acompanha o if, mesmo nível

# -----------------------
# Exemplo 3: if com elif
idade = 20
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
# Observação: elif permite testar várias condições adicionais, todos os blocos alinhados

# -----------------------
# Exemplo 4: blocos aninhados
nota = 85
if nota >= 60:               # nível 0
    print("Aprovado")        # nível 1
    if nota >= 90:           # sub-bloco do if (nível 2)
        print("Aprovado com excelência") # nível 2
else:
    print("Reprovado")       # nível 1
# Observação: blocos aninhados adicionam 4 espaços a cada nível

# -----------------------
# Exemplo 5: if ternário
idade = 18
status = "maior de idade" if idade >= 18 else "menor de idade"
print(status)
# Observação: if ternário é uma forma compacta de if-else, usada apenas para escolher entre dois valores.
# Estrutura: valor_se_verdadeiro if condição else valor_se_falso
# Use apenas em expressões simples — para blocos maiores, prefira o if tradicional.

# -----------------------
# Checklist rápido de condicionais:
# 1. Cada bloco iniciado com ":" precisa de indentação
# 2. Sub-blocos aumentam +4 espaços por nível
# 3. Comandos do mesmo bloco devem alinhar horizontalmente
# 4. Voltar ao nível anterior ao terminar sub-bloco
# 5. Misturar tabs e espaços gera erro

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 3.4 – Estrutura de Repetição em Python
# -----------------------------------------
# Objetivo: Entender como funcionam loops for e while, incluindo blocos aninhados e sub-blocos.

# -----------------------
# Exemplo 1: for simples
for i in range(5):           # bloco for (nível 0 ou 1 dentro de função)
    print(i)                  # nível 1 (4 espaços)
# Observação: tudo que estiver indentado pertence ao bloco do for

# -----------------------
# Exemplo 2: while simples
contador = 0
while contador < 5:           # bloco while
    print(contador)           # nível 1
    contador += 1             # ainda nível 1
# Observação: o loop continua enquanto a condição for verdadeira

# -----------------------
# Exemplo 3: for com sub-bloco (loop dentro de loop)
for i in range(3):            # nível 0
    print(f"Loop principal: {i}") # nível 1
    
    for j in range(2):        # sub-bloco do for (nível 2)
        print(f"  Sub-loop: {j}")  # nível 2
    
    print("Fim do sub-loop")  # volta ao nível 1

# -----------------------
# Exemplo 4: while com sub-bloco e condicional
contador = 0
while contador < 3:            # nível 0
    if contador % 2 == 0:      # sub-bloco if (nível 1)
        print(f"{contador} é par")  # nível 2
    contador += 1               # volta ao nível 1
# Observação: blocos aninhados aumentam 4 espaços a cada nível

# -----------------------
# Checklist rápido de loops:
# 1. Cada bloco iniciado com ":" precisa de indentação
# 2. Sub-blocos adicionam +4 espaços por nível
# 3. Comandos do mesmo bloco devem alinhar horizontalmente
# 4. Voltar ao nível anterior ao terminar sub-bloco
# 5. Misturar tabs e espaços gera erro

# =================================================================================
# =================================================================================
# =================================================================================
