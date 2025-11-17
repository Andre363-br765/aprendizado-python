# 🧵 Aula 4 — Strings no Python

## 🎯 Objetivo Geral
Aprender como manipular textos (**strings**) em Python usando:

- Métodos úteis da classe `string`
- Interpolação de variáveis
- Fatiamento (**slicing**)
- Strings de múltiplas linhas

---

## 4.1 — Conhecendo métodos úteis da classe `string`

### 📝 Introdução
A classe `str` do Python é **muito rica em funcionalidades**.  
Diferente de outras linguagens, manipular texto em Python é simples e direto graças à grande quantidade de métodos disponíveis.

As strings possuem métodos para:

- **Formatar textos**
- **Alterar maiúsculas/minúsculas**
- **Remover espaços**
- **Encontrar palavras**
- **Substituir trechos**
- E muito mais!

Ao longo desta aula, veremos os métodos mais importantes para o dia a dia da programação.

#### 🔠 Maiúscula, minúscula e título
```py
texto = "python é incrível"

print(texto.upper())    # PYTHON É INCRÍVEL
print(texto.lower())    # python é incrível
print(texto.capitalize()) # Python é incrível
print(texto.title())    # Python É Incrível
```

✂️ Eliminando espaços em branco
```py
frase = "   Olá, Python!   "
print(frase.strip())   # remove dos dois lados
print(frase.lstrip())  # remove da esquerda
print(frase.rstrip())  # remove da direita
```

🔗 Junções e centralização
```py
lista = ["Python", "é", "legal"]
print("-".join(lista))    # Python-é-legal

print("Python".center(20, "-"))
# -------Python--------
```

---

## 4.2 — Interpolação de Variáveis

### 📝 Introdução
Existem 3 formas de inserir variáveis dentro de uma string:

 1. **Old style (%)** → pouco usado hoje
 2. **Método** `.format()`
 3. **F-strings** (recomendado e mais moderno)

#### 🔵 1. Old Style (%) — Não recomendado
```py
nome = "Ana"
idade = 20
print("Nome: %s, Idade: %d" % (nome, idade))
```

#### 🔵 2. Método format()
```py
print("Nome: {}, Idade: {}".format(nome, idade))
print("Nome: {n}, Idade: {i}".format(n=nome, i=idade))
```

#### 🔵 3. F-Strings (moderna, prática e recomendada)
```py
print(f"Nome: {nome}, Idade: {idade}")
```
##### 💡 Cálculos dentro da f-string
```py
altura = 1.70
print(f"{nome} tem {altura*100:.0f} cm de altura")
```

---

## 4.3 — Fatiamento de Strings (Slicing)

### 📝 Introdução
Fatiar uma string significa pegar apenas **uma parte dela**, usando:

- **start** → índice inicial (inclusivo)
- **stop** → índice final (exclusivo)
- **step** → salto opcional

✂️ Exemplos de fatiamento
```py
texto = "Python é incrível!"

print(texto[0:6])   # Python
print(texto[:6])    # Python
print(texto[7:])    # é incrível!
print(texto[::2])   # Ptoécrvl
print(texto[::-1])  # !levírcni é nohtyP
```

## 4.4 — Strings de Múltiplas Linhas
📝 Introdução
Strings de múltiplas linhas são definidas com:

 - `''' três aspas simples '''`
 - `""" três aspas duplas """`

Elas preservam quebras de linha e espaços.

### 🧱 Strings triplas
```py
texto = """Esta é uma string
que ocupa várias
linhas."""
print(texto)
```

### 🔤 Com quebra de linha usando \n
```py
msg = "Linha 1\nLinha 2\nLinha 3"
print(msg)
```

### 🔄 Linha longa dividida com \ (escape)
```py
texto = "Esta linha é muito longa, \
mas continua na próxima linha sem quebrar no resultado."
print(texto)
```

### 🧩 Usando strings triplas + f-string
```py
nome = "Ana"
idade = 20

texto = f"""Nome: {nome}
Idade: {idade}
Mensagem: Bem-vinda ao Python!"""
print(texto)
```

✍️ **Próxima aula:** [4.2 - strings](2_strings_resumo.md)