# =================================================================================
# =================================================================================
# =================================================================================

# Aula 2.1: Operações Aritméticas em Python

# --------------------------
# Soma (+)
# --------------------------
x = 10
y = 5
soma = x + y
print("Soma:", soma)  # 15

# --------------------------
# Subtração (-)
# --------------------------
sub = x - y
print("Subtração:", sub)  # 5

# --------------------------
# Multiplicação (*)
# --------------------------
mult = x * y
print("Multiplicação:", mult)  # 50

# --------------------------
# Divisão (/)
# --------------------------
div = x / y
print("Divisão:", div)  # 2.0 (sempre retorna float)

# --------------------------
# Divisão inteira (//)
# --------------------------
div_int = x // y
print("Divisão inteira:", div_int)  # 2

# --------------------------
# Resto da divisão (%)
# --------------------------
resto = x % y
print("Resto da divisão:", resto)  # 0

# --------------------------
# Potência (**)
# --------------------------
pot = x ** y
print("Potência:", pot)  # 100000

# --------------------------
# Observações de boas práticas
# --------------------------
# 1. Use nomes de variáveis claros (ex: total, resultado, quociente)
# 2. Separe cálculos diferentes em variáveis para facilitar leitura
# 3. Sempre comente seu código para ficar fácil de entender

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 2.2: Operadores de comparação

# Exemplo de saldo e saque
saldo = 1500
saque = 700

# --------------------------
# Operadores de igualdade e diferença
# --------------------------
print("Saldo igual ao saque?", saldo == saque)   # False
print("Saldo diferente do saque?", saldo != saque)  # True

# --------------------------
# Operadores maior e maior ou igual
# --------------------------
print("Saldo maior que saque?", saldo > saque)       # True
print("Saldo maior ou igual ao saque?", saldo >= saque)  # True

# --------------------------
# Operadores menor e menor ou igual
# --------------------------
print("Saldo menor que saque?", saldo < saque)       # False
print("Saldo menor ou igual ao saque?", saldo <= saque)  # False

# --------------------------
# Combinações de comparações
# --------------------------
# Podemos combinar operadores usando 'and' e 'or'
print("Saldo maior que 1000 e saque menor que 800?", saldo > 1000 and saque < 800)  # True
print("Saldo menor que 1000 ou saque maior que 500?", saldo < 1000 or saque > 500)   # True

# --------------------------
# Observações de boas práticas
# --------------------------
# 1. Operadores de comparação retornam valores booleanos (True ou False)
# 2. Úteis para decisões em estruturas condicionais (if, while)
# 3. Use nomes de variáveis claros e descritivos
# 4. Combine comparações com 'and', 'or' ou 'not' para condições mais complexas
# 5. Sempre comente seu código para melhorar a legibilidade

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 2.3: Operadores de Atribuição

# --------------------------
# Atribuição simples (=)
# --------------------------
saldo = 1500    # atribui 1500 à variável saldo
print("Saldo inicial:", saldo)

# --------------------------
# Atribuição com adição (+=)
# --------------------------
saldo += 500    # equivalente a saldo = saldo + 500
print("Após depósito de 500:", saldo)

# --------------------------
# Atribuição com subtração (-=)
# --------------------------
saldo -= 300    # equivalente a saldo = saldo - 300
print("Após saque de 300:", saldo)

# --------------------------
# Atribuição com multiplicação (*=)
# --------------------------
bonus = 2
saldo *= bonus   # equivalente a saldo = saldo * bonus
print("Após multiplicar por bônus 2:", saldo)

# --------------------------
# Atribuição com divisão (/=)
# --------------------------
saldo /= 2       # equivalente a saldo = saldo / 2
print("Após dividir por 2:", saldo)

# --------------------------
# Atribuição com divisão inteira (//=)
# --------------------------
saldo //= 100
print("Divisão inteira por 100:", saldo)

# --------------------------
# Atribuição com módulo (%=)
# --------------------------
saldo %= 7
print("Resto da divisão por 7:", saldo)

# --------------------------
# Observações de boas práticas
# --------------------------
# 1. Use operadores de atribuição para simplificar cálculos e deixar o código mais legível
# 2. Mantenha nomes de variáveis claros e descritivos
# 3. Evite misturar operações complexas em uma única linha sem comentários
# 4. Sempre teste os resultados para garantir que as atribuições estão corretas

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 2.4: Operadores Lógicos

# Exemplo de variáveis
saldo = 1000
saque = 200
limite = 100

# --------------------------
# Operador AND
# --------------------------
# Retorna True se todas as condições forem verdadeiras
print("Saldo suficiente e saque dentro do limite?", saldo >= saque and saque <= limite)  # False

# --------------------------
# Operador OR
# --------------------------
# Retorna True se pelo menos uma condição for verdadeira
print("Saldo suficiente ou saque dentro do limite?", saldo >= saque or saque <= limite)   # True

# --------------------------
# Operador NOT
# --------------------------
# Inverte o valor booleano
transacao_negada = not(saldo >= saque and saque <= limite)
print("Transação negada?", transacao_negada)  # True

# --------------------------
# Combinações mais complexas
# --------------------------
# Por exemplo, verificar se o saque é permitido
saque_permitido = (saldo >= saque and saque <= limite)
print("Saque permitido?", saque_permitido)  # False

# Negando a condição
print("Saque não permitido?", not saque_permitido)  # True

# --------------------------
# Observações de boas práticas
# --------------------------
# 1. Use parênteses para deixar condições complexas mais claras
# 2. 'and' retorna True apenas se todas as condições forem verdadeiras
# 3. 'or' retorna True se pelo menos uma condição for verdadeira
# 4. 'not' inverte o valor booleano
# 5. Nomes de variáveis claros ajudam a entender a lógica

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 2.5: Operadores de Identidade

# Exemplo de variáveis
saldo = 1000
limite = 500
saque = 500  # mesmo valor de limite, mas variável diferente

# --------------------------
# Operadores de identidade
# --------------------------
# 'is' verifica se duas variáveis ocupam o mesmo espaço na memória
# 'is not' verifica se ocupam espaços diferentes

print("saque é limite?", saque is limite)          # False (valores iguais, mas objetos diferentes)
print("saque não é limite?", saque is not limite)  # True

# --------------------------
# Exemplo com objetos iguais
# --------------------------
x = limite
print("x é limite?", x is limite)   # True (mesmo objeto na memória)

# --------------------------
# Observações importantes
# --------------------------
# 1. 'is' e 'is not' comparam IDENTIDADE (mesmo objeto), não valor.
# 2. Para comparar VALORES, use == ou !=.
# 3. São mais usados com tipos imutáveis (None, bool, etc.)
# 4. Exemplo prático: verificar se uma variável é None:
valor = None
print("valor é None?", valor is None)  # True
print("valor não é None?", valor is not None)  # False

# =================================================================================
# =================================================================================
# =================================================================================

# Aula 2.6: Operadores de Associação

# --------------------------
# Listas de exemplos
# --------------------------
frutas = ["laranja", "banana", "uva", "abacate", "pera"]
verduras = ["alface", "couve", "espinafre", "brócolis"]
legumes = ["cenoura", "batata", "abobrinha"]

# --------------------------
# Operadores de associação
# --------------------------
# 'in' verifica se um elemento está presente em uma sequência
# 'not in' verifica se NÃO está presente

print("banana está na lista de frutas?", "banana" in frutas)      # True
print("maçã está na lista de frutas?", "maçã" in frutas)          # False

print("couve está na lista de verduras?", "couve" in verduras)    # True
print("batata está nas verduras?", "batata" in verduras)          # False

print("abobrinha não está nas frutas?", "abobrinha" not in frutas)  # True
print("pera não está nas frutas?", "pera" not in frutas)            # False

# --------------------------
# Exemplos práticos
# --------------------------
item = "batata"
if item in legumes:
    print(f"{item} é um legume.")
else:
    print(f"{item} não é um legume.")

# --------------------------
# Observações de boas práticas
# --------------------------
# 1. Use 'in' e 'not in' para verificar presença em listas, tuplas, strings e dicionários.
# 2. Sempre mantenha os nomes de listas e variáveis descritivos (ex: 'frutas', 'legumes').
# 3. Esses operadores são muito usados em loops e condições (ex: if, for).
# 4. São ideais para evitar erros ao tentar acessar algo inexistente em uma coleção.

# =================================================================================
# =================================================================================
# =================================================================================
