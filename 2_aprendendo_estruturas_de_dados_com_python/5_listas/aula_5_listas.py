# aula_5_listas.py
# Aula 5: Trabalhando com Listas em Python
# --------------------------

# --------------------------
# 5.1 Criando listas
# --------------------------
lista_vazia = []
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "uva"]
misturado = [1, "Python", True, 3.14]

print(lista_vazia, numeros, frutas, misturado)

# --------------------------
# 5.2 Acessando elementos
# --------------------------
print("Primeiro número:", numeros[0])
print("Última fruta:", frutas[-1])

# --------------------------
# 5.3 Fatiamento de listas
# --------------------------
print(numeros[1:4])    # [2,3,4]
print(frutas[:2])      # ['maçã','banana']
print(numeros[::2])    # [1,3,5]
print(numeros[::-1])   # [5,4,3,2,1]

# --------------------------
# 5.4 Modificando listas
# --------------------------
numeros[0] = 10
frutas.append("laranja")     # adiciona no final
frutas.insert(1, "morango") # adiciona na posição 1
print(numeros, frutas)

# --------------------------
# 5.5 Removendo elementos
# --------------------------
frutas.remove("banana")   # remove pelo valor
ultimo = frutas.pop()     # remove e retorna o último
print(frutas, "Removido:", ultimo)
del numeros[1]            # remove pelo índice
print(numeros)

# --------------------------
# 5.6 Métodos úteis de listas
# --------------------------
numeros = [1, 2, 3, 4, 5]
print(len(numeros))      # tamanho da lista
print(max(numeros))      # maior valor
print(min(numeros))      # menor valor
print(sum(numeros))      # soma dos elementos
numeros.sort(reverse=True) # ordena decrescente
print(numeros)

# --------------------------
# 5.7 Verificação de presença
# --------------------------
print(3 in numeros)   # True
print(10 in numeros)  # False

# --------------------------
# 5.8 Iterando sobre listas
# --------------------------
for fruta in frutas:
    print("Fruta:", fruta)

for i, numero in enumerate(numeros):
    print(f"Índice {i}: {numero}")

# --------------------------
# 5.9 Listas aninhadas (listas dentro de listas)
# --------------------------
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Índices positivos:
# linha→   0      1      2
# col ↓
# 0       [1]    [2]    [3]
# 1       [4]    [5]    [6]
# 2       [7]    [8]    [9]

# Índices negativos:
# linha→  -3     -2     -1
# col ↓
# -3      [1]    [2]    [3]
# -2      [4]    [5]    [6]
# -1      [7]    [8]    [9]

print("Elemento central:", matriz[1][1])  # 5

# Iterando sobre matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()