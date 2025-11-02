# aula_4_strings_resumo.py
# Aula 4: Strings e Fatiamento
# --------------------------
# Resumo das seções 4.1 a 4.4

# --------------------------
# 4.1 Conhecimentos da Classe String
# --------------------------
texto = "Olá, mundo!"
print(texto)

# Acessando caracteres
print("Primeiro:", texto[0], "Último:", texto[-1])

# Fatiamento básico
print("Fatia 0-4:", texto[0:4], "Do 5 ao final:", texto[5:])

# Comprimento da string
print("Tamanho:", len(texto))

# Métodos úteis
print(texto.upper(), texto.lower(), texto.capitalize(), texto.title())
print(texto.strip(), texto.replace("mundo", "Python"))

# Verificação de conteúdo
print(texto.isalpha(), "Python".isalpha(), "123".isdigit())

# Divisão e junção
palavras = texto.split()
print("Split:", palavras)
print("Join:", "-".join(palavras))

# Presença de substring
print("mundo" in texto, "Python" in texto)


# --------------------------
# 4.2 Interpolação de Variáveis
# --------------------------
nome = "Ana"
idade = 20
altura = 1.65

# Várias formas de interpolação
print("Nome:", nome, "Idade:", idade)
print("Nome: " + nome + " Idade: " + str(idade))
print(f"Nome: {nome} Idade: {idade}")
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {n} Idade: {i}".format(n=nome, i=idade))

# Cálculos dentro da f-string
print(f"{nome} tem {idade} anos e {altura*100:.0f} cm de altura")


# --------------------------
# 4.3 Fatiamento de Strings (Slicing)
# --------------------------
texto2 = "Python é incrível!"

# Básico
print(texto2[0:6], texto2[:6], texto2[7:], texto2[:], texto2[::2], texto2[1::2])

# Índices negativos
print(texto2[-1], texto2[-8:-1], texto2[::-1])

# Combinações
subtexto = texto2[0:6]
print(subtexto.upper(), texto2[7:15].capitalize())


# --------------------------
# 4.4 Strings de Múltiplas Linhas
# --------------------------
# Três aspas simples
texto_mult1 = '''Esta é uma string
que ocupa várias
linhas.'''
print(texto_mult1)

# Três aspas duplas
texto_mult2 = """Também podemos
usar aspas duplas
para múltiplas linhas."""
print(texto_mult2)

# Quebra de linha com \n
texto_mult3 = "Linha 1\nLinha 2\nLinha 3"
print(texto_mult3)

# Evitando quebra de linha no código com \
texto_mult4 = "Linha muito longa, \
continua na próxima linha do código."
print(texto_mult4)

# Combinação com f-strings
texto_mult5 = f"""Nome: {nome}
Idade: {idade}
Mensagem: Bem-vinda ao Python!"""
print(texto_mult5)