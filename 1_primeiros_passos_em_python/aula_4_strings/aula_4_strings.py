# Aula 4: Strings e Fatiamento

# --------------------------
# 4.1 Conhecimentos da Classe String
# --------------------------

# Criando strings
texto = "Olá, mundo!"
print(texto)  # Olá, mundo!

# Acessando caracteres (indexação)
primeiro = texto[0]   # 'O'
ultimo = texto[-1]    # '!'
print("Primeiro:", primeiro, "Último:", ultimo)

# Fatiamento (slicing)
parte = texto[0:4]    # 'Olá,'
ate_o_final = texto[5:]  # 'mundo!'
print("Fatia 0-4:", parte, "Do 5 ao final:", ate_o_final)

# Comprimento da string
tamanho = len(texto)
print("Tamanho:", tamanho)

# Métodos comuns da classe string
print(texto.upper())      # 'OLÁ, MUNDO!'
print(texto.lower())      # 'olá, mundo!'
print(texto.capitalize()) # 'Olá, mundo!'
print(texto.title())      # 'Olá, Mundo!'
print(texto.strip())      # remove espaços extras no início/fim
print(texto.replace("mundo", "Python"))  # 'Olá, Python'

# Verificação de tipos de conteúdo
print(texto.isalpha())  # False, pois há vírgula e espaço
print("Python".isalpha()) # True
print("123".isdigit())    # True

# Divisão e junção de strings
palavras = texto.split()      # ['Olá,', 'mundo!']
juncao = "-".join(palavras)   # 'Olá,-mundo!'
print("Split:", palavras, "Join:", juncao)

# Verificação de presença de substring
print("mundo" in texto)  # True
print("Python" in texto) # False

# =================================================================================
# =================================================================================
# =================================================================================

# --------------------------
# 4.2 Interpolação de Variáveis
# --------------------------

nome = "Ana"
idade = 20

# --------------------------
# Usando vírgula no print (concatenação automática)
# --------------------------
print("Nome:", nome, "Idade:", idade)  # Nome: Ana Idade: 20

# --------------------------
# Usando operador + (precisa converter números para string)
# --------------------------
print("Nome: " + nome + " Idade: " + str(idade))  # Nome: Ana Idade: 20

# --------------------------
# Usando f-strings (forma mais moderna e prática)
# --------------------------
print(f"Nome: {nome} Idade: {idade}")  # Nome: Ana Idade: 20

# --------------------------
# Interpolação com form()
# --------------------------
print("Nome: {} Idade: {}".format(nome, idade))  # Nome: Ana Idade: 20

# --------------------------
# Interpolação com índices e nomes
# --------------------------
print("Nome: {0} Idade: {1}".format(nome, idade))           # Nome: Ana Idade: 20
print("Nome: {n} Idade: {i}".format(n=nome, i=idade))      # Nome: Ana Idade: 20

# --------------------------
# Multiplas variáveis e cálculos dentro da f-string
# --------------------------
altura = 1.65
print(f"{nome} tem {idade} anos e {altura*100:.0f} cm de altura")  # Ana tem 20 anos e 165 cm

# =================================================================================
# =================================================================================
# =================================================================================

# --------------------------
# 4.3 Fatiamento de Strings (Slicing)
# --------------------------

texto = "Python é incrível!"

# --------------------------
# Sintaxe básica: [início:fim:passo]
# --------------------------
# início: índice inicial (inclusive)
# fim: índice final (exclusivo)
# passo: intervalo de salto (opcional)

# Exemplos:
print(texto[0:6])   # 'Python' -> do índice 0 até 5
print(texto[:6])    # 'Python' -> mesmo que acima
print(texto[7:])    # 'é incrível!' -> do índice 7 até o final
print(texto[:])     # 'Python é incrível!' -> toda a string
print(texto[::2])   # 'Ptoécníl' -> pula de 2 em 2
print(texto[1::2])  # 'yhn éncrvl' -> pula de 2 em 2 começando no índice 1

# --------------------------
# Índices negativos
# --------------------------
print(texto[-1])    # '!' -> último caractere
print(texto[-8:-1]) # 'incrível' -> do -8 até -2
print(texto[::-1])  # '!levírcni é nohtyP' -> string invertida

# --------------------------
# Combinações de slicing
# --------------------------
subtexto = texto[0:6]          # 'Python'
print(subtexto.upper())        # 'PYTHON'
print(texto[7:15].capitalize()) # 'É incríve'

# =================================================================================
# =================================================================================
# =================================================================================

# --------------------------
# 4.4 Strings de Múltiplas Linhas
# --------------------------

# --------------------------
# Usando três aspas simples '''...'''
# --------------------------
texto1 = '''Esta é uma string
que ocupa várias
linhas sem problemas.'''
print(texto1)

# --------------------------
# Usando três aspas duplas """..."""
# --------------------------
texto2 = """Também podemos
usar aspas duplas
para múltiplas linhas."""
print(texto2)

# --------------------------
# Quebra de linha com \n
# --------------------------
texto3 = "Linha 1\nLinha 2\nLinha 3"
print(texto3)

# --------------------------
# Evitando quebra de linha no código com \
# --------------------------
texto4 = "Esta é uma linha muito longa, \
mas o Python entende que continua \
na próxima linha do código."
print(texto4)

# --------------------------
# Combinação de múltiplas linhas e f-strings
# --------------------------
nome = "Ana"
idade = 20
texto5 = f"""Nome: {nome}
Idade: {idade}
Mensagem: Bem-vinda ao Python!"""
print(texto5)

# =================================================================================
# =================================================================================
# =================================================================================
