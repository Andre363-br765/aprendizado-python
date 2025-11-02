# Aula 3.5 – Resumo de Estrutura de Código em Python
# ---------------------------------------------------
# Objetivo: Resumir conceitos de indentação, blocos, condicionais e loops

# -----------------------
# 1 Indentação básica
print("Início do programa")   # nível 0
# Observação: código fora de qualquer bloco → nível 0

def funcao_exemplo():        # nível 0 → início do bloco da função
    print("Dentro da função") # nível 1 (4 espaços)
    # Observação: todo código dentro do def pertence ao bloco da função

# -----------------------
# 2 Blocos e sub-blocos
def blocos_aninhados():
    if True:                  # nível 1 → bloco do if
        print("Bloco if")     # nível 2 → sub-bloco
        for i in range(2):   # nível 2 → sub-bloco do if
            print(i)         # nível 3 → sub-sub-bloco
        print("Fim do for")  # nível 2 → volta ao bloco do if
    print("Fim do if")        # nível 1 → volta ao bloco da função

# -----------------------
# 3 Estruturas condicionais
x = 15
if x < 10:                    # bloco if
    print("Menor que 10")     # nível 1
elif x < 20:                  # bloco elif
    print("Entre 10 e 19")    # nível 1
else:                         # bloco else
    print("20 ou mais")       # nível 1
# Observação: if, elif e else devem alinhar horizontalmente, cada bloco com +4 espaços

# -----------------------
# 4 Estruturas de repetição
for i in range(3):            # bloco for
    print(f"Loop principal: {i}")  # nível 1
    for j in range(2):        # sub-bloco do for
        print(f"  Sub-loop: {j}")  # nível 2
# Observação: loops aninhados aumentam 4 espaços por nível

contador = 0
while contador < 3:            # bloco while
    if contador % 2 == 0:      # sub-bloco if
        print(f"{contador} é par")  # nível 2
    contador += 1               # nível 1 → bloco while
# Observação: while continua repetindo enquanto a condição for verdadeira

# -----------------------
# Checklist geral de estruturas:
# 1. Cada bloco iniciado com ":" precisa de indentação
# 2. Cada sub-bloco adiciona +4 espaços por nível
# 3. Comandos do mesmo bloco devem alinhar horizontalmente
# 4. Voltar ao nível anterior ao terminar sub-bloco
# 5. Misturar tabs e espaços causa erro (IndentationError)
