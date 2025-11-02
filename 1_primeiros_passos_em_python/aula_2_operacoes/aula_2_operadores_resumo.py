# Aula 2: Operadores e Atribuições em Python (Resumo)

# --------------------------
# Operações Aritméticas
# --------------------------
x, y = 10, 5
print("Soma:", x + y)
print("Subtração:", x - y)
print("Multiplicação:", x * y)
print("Divisão:", x / y)
print("Divisão inteira:", x // y)
print("Resto da divisão:", x % y)
print("Potência:", x ** y)

# --------------------------
# Operadores de Comparação
# --------------------------
saldo, saque = 1500, 700
print("Saldo == saque?", saldo == saque)
print("Saldo != saque?", saldo != saque)
print("Saldo > saque?", saldo > saque)
print("Saldo >= saque?", saldo >= saque)
print("Saldo < saque?", saldo < saque)
print("Saldo <= saque?", saldo <= saque)
print("Saldo>1000 e saque<800?", saldo>1000 and saque<800)
print("Saldo<1000 ou saque>500?", saldo<1000 or saque>500)

# --------------------------
# Operadores de Atribuição
# --------------------------
saldo = 1500
saldo += 500
saldo -= 300
saldo *= 2
saldo /= 2
saldo //= 100
saldo %= 7
print("Saldo final:", saldo)

# --------------------------
# Operadores Lógicos
# --------------------------
saldo, saque, limite = 1000, 200, 100
print("Saldo suficiente e saque dentro do limite?", saldo>=saque and saque<=limite)
print("Saldo suficiente ou saque dentro do limite?", saldo>=saque or saque<=limite)
transacao_negada = not (saldo>=saque and saque<=limite)
print("Transação negada?", transacao_negada)

# --------------------------
# Operadores de Identidade
# --------------------------
limite, saque = 500, 500
print("saque é limite?", saque is limite)
print("saque não é limite?", saque is not limite)
x = limite
print("x é limite?", x is limite)
valor = None
print("valor é None?", valor is None)

# --------------------------
# Operadores de Associação
# --------------------------
frutas = ["laranja", "banana", "uva", "abacate", "pera"]
verduras = ["alface", "couve", "espinafre", "brócolis"]
legumes = ["cenoura", "batata", "abobrinha"]

print("banana está em frutas?", "banana" in frutas)
print("maçã está em frutas?", "maçã" in frutas)
item = "batata"
if item in legumes:
    print(f"{item} é um legume.")
else:
    print(f"{item} não é um legume.")
