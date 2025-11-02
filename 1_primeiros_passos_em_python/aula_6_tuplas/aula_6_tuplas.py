# Aula 6: Conhecendo Tuplas em Python
# --------------------------

# --------------------------
# 6.1 Criando tuplas
# --------------------------
tupla_vazia = ()
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mista = (1, "Python", True, 3.14)

print(tupla_vazia, tupla_numeros, tupla_mista)

# Tupla com um único elemento
tupla_um = (10,)  # precisa da vírgula
print(tupla_um)

# --------------------------
# 6.2 Acessando elementos
# --------------------------
print("Primeiro número:", tupla_numeros[0])
print("Último elemento:", tupla_mista[-1])

# --------------------------
# 6.3 Fatiamento de tuplas
# --------------------------
print(tupla_numeros[1:4])    # (2,3,4)
print(tupla_numeros[:3])     # (1,2,3)
print(tupla_numeros[::2])    # (1,3,5)
print(tupla_numeros[::-1])   # (5,4,3,2,1)

# --------------------------
# 6.4 Tuplas são imutáveis
# --------------------------
# Não é possível modificar elementos
# tupla_numeros[0] = 10  # gera erro

# --------------------------
# 6.5 Métodos úteis de tuplas
# --------------------------
tupla_exemplo = (1, 2, 3, 2, 2, 4)
print("Contagem de 2:", tupla_exemplo.count(2))
print("Índice do 3:", tupla_exemplo.index(3))

# --------------------------
# 6.6 Iterando sobre tuplas
# --------------------------
for numero in tupla_numeros:
    print(numero)

# --------------------------
# 6.7 Tuplas aninhadas
# --------------------------
tupla_matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("Elemento central:", tupla_matriz[1][1])  # 5

for linha in tupla_matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
