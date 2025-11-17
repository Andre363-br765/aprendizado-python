# 📘 Aula 1.1 – Tipos de Dados Básicos em Python 🐍

> Um guia simples e direto mostrando os principais tipos de dados em **Python** e como cada um se comporta.

---

## 1️⃣ O que são tipos de dados?

Os **tipos de dados** definem *que tipo de informação* um valor representa e *quais operações podem ser feitas* com ele.

Exemplos:

* Alguns tipos permitem **operações matemáticas** (`int`, `float`).
* Outros representam **texto** (`str`).
* Alguns guardam **coleções de valores** (`list`, `tuple`, `dict`).

Em Python, **tudo é um objeto**, e cada valor pertence a algum tipo.

---

## 2️⃣ Principais tipos de dados

### 🔹 Tipos numéricos e lógicos

| Tipo        | Exemplo           | Descrição         |
| ----------- | ----------------- | ----------------- |
| **int**     | `1`, `10`, `-100` | Números inteiros  |
| **float**   | `1.5`, `-10.5`    | Números decimais  |
| **complex** | `2 + 3j`, `1j`    | Números complexos |
| **bool**    | `True`, `False`   | Valores lógicos   |

---

### 🔹 Texto

| Tipo    | Exemplo           | Descrição                    |
| ------- | ----------------- | ---------------------------- |
| **str** | `"Python"`, `'a'` | Cadeia de caracteres (texto) |

---

### 🔹 Coleções

| Tipo          | Exemplo              | Descrição               |
| ------------- | -------------------- | ----------------------- |
| **list**      | `[1, 2, 3]`          | Sequência mutável       |
| **tuple**     | `(1, 2, 3)`          | Sequência imutável      |
| **range**     | `range(5)`           | Sequência de números    |
| **dict**      | `{"nome": "Ana"}`    | Pares chave-valor       |
| **set**       | `{1, 2, 3}`          | Conjunto sem repetições |
| **frozenset** | `frozenset([1,2,3])` | Conjunto imutável       |

---

### 🔹 Manipulação de bytes

| Tipo           | Exemplo              | Descrição               |
| -------------- | -------------------- | ----------------------- |
| **bytes**      | `b"Python"`          | Imutável                |
| **bytearray**  | `bytearray([1,2,3])` | Mutável                 |
| **memoryview** | `memoryview(b"abc")` | Acesso direto à memória |

---

## 3️⃣ Exemplos práticos 💻

```python
# Tipos básicos
print("Python")    # str
print(10)          # int
print(3.14)        # float
print(True)        # bool
print(False)       # bool

# Coleções
print([1, 2, 3])                 # list
print((1, 2, 3))                 # tuple
print({"nome": "Ana", "idade": 25})  # dict
print({1, 2, 3})                 # set
```

💡 **Python identifica automaticamente o tipo de cada valor.**

---

## 4️⃣ Verificando o tipo de um valor 🔍

Use **`type()`**:

```python
print(type("Python"))   # <class 'str'>
print(type(10))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>
print(type([1, 2, 3]))  # <class 'list'>
```

---

## 5️⃣ Conversão de tipos (Casting) 🔄

Convertendo valores entre tipos:

```python
print(int(1.99))      # 1 — corta os decimais
print(int("10"))      # 10
print(float("10.10")) # 10.1
print(float(100))     # 100.0

valor = 10
valor_str = str(valor)

print(type(valor))      # int
print(type(valor_str))  # str
```

---

## 6️⃣ Divisão normal vs divisão inteira ➗

```python
print(100 / 2)   # 50.0  → divisão normal (float)
print(100 // 2)  # 50    → divisão inteira (descarta decimais)
```

---

## 7️⃣ Resumo 📘

| Função / Operador | Descrição              |
| ----------------- | ---------------------- |
| `type()`          | Mostra o tipo          |
| `int()`           | Converte para inteiro  |
| `float()`         | Converte para decimal  |
| `str()`           | Converte para string   |
| `bool()`          | Converte para booleano |
| `/`               | Divisão normal         |
| `//`              | Divisão inteira        |

---

✍️ **Próxima aula:** [1.2 – Modo Interativo do Python (Shell)](2_modo_interativo.md)