# 📘 Módulo 3 – Estruturas de Controle

## 🧠 Resumo Geral

As **estruturas de controle** permitem definir **como** e **quando** partes do código serão executadas.
Neste módulo, aprendemos sobre **indentação**, **condições** e **repetições** — três pilares fundamentais da lógica em Python.

---

|                   Aula                   | Título                        | Conteúdo Principal                                                      |
| :--------------------------------------: | :---------------------------- | :---------------------------------------------------------------------- |
|      [3.1](#31--indentação-e-blocos)     | 📏 Indentação e Blocos        | Define os blocos de código usando espaços; base da estrutura do Python. |
|   [3.2](#32--estrutura-condicional-if)   | 🔍 Estrutura Condicional `if` | Executa ações somente se uma condição for verdadeira.                   |
|           [3.3](#33--if--else)           | 🔀 `if / else`                | Define dois caminhos de execução: condição verdadeira ou falsa.         |
|        [3.4](#34--if--elif--else)        | 🪜 `if / elif / else`         | Permite testar múltiplas condições em sequência.                        |
|          [3.5](#35--if-aninhado)         | 🧩 `if` aninhado              | Um `if` dentro de outro para decisões encadeadas.                       |
|          [3.6](#36--if-ternário)         | ⚡ If Ternário                 | Escreve condições em formato compacto (uma linha).                      |
|  [3.7](#37--estrutura-de-repetição-for)  | 🔁 Repetição `for`            | Itera sobre sequências ou repete ações um número definido de vezes.     |
| [3.8](#38--estrutura-de-repetição-while) | 🔄 Repetição `while`          | Repete ações enquanto a condição for verdadeira.                        |
|  [3.9](#39--loops-infinitos-e-cuidados)  | 🚨 Loops Infinitos            | Como evitar loops sem fim e boas práticas importantes.                  |

---

## 1️⃣ Indentação e Blocos

A **indentação é essencial no Python** e define os **blocos de código**.

Diferente de outras linguagens (como **Java ou C**, que usam `{ }`), o Python utiliza **espaços ou tabulações** para indicar o início e o fim de um bloco.

* Sem indentação correta, o código **gera erro**.
* A indentação também melhora a **legibilidade** e a **organização visual** do programa.

### ✅ Exemplo:

```python
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

---

## 2️⃣ Estruturas Condicionais

As estruturas condicionais são usadas para **tomar decisões** com base em **expressões lógicas** (verdadeiro ou falso).

---

### ➤ `if`

Executa um bloco apenas se a condição for **verdadeira**.

#### 📖 Exemplo:

```python
if idade >= 18:
    print("Maior de idade")
```

### ➤ `if / else`

Define **dois caminhos possíveis**:

* um quando a condição é **verdadeira**,
* outro quando a condição é **falsa**.

#### 📖 Exemplo:

```python
if idade >= 18:
    print("Maior")
else:
    print("Menor")
```

### ➤ `if / elif / else`

Permite fazer **múltiplas verificações**, testando várias condições em sequência.

#### 📖 Exemplo:

```python
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Boa")
else:
    print("Insuficiente")
```

### ➤ `if` aninhado

Um `if` dentro de outro.

### ➤ `if` ternário

Escreve uma condição em uma única linha:

```py
mensagem = "Maior" if idade >= 18 else "Menor"
```

---

## 3️⃣ Estruturas de Repetição

Usadas para executar ações várias vezes, com ou sem número definido de repetições.

### ➤ `for`

Usado quando sabemos quantas vezes queremos repetir ou quando percorremos objetos iteráveis.

```py
for i in range(3):
    print("Olá")
```

* `range()` gera uma sequência numérica.

  * `range(inicio, fim, passo)`

### ➤ `while`

Usado quando não sabemos o número exato de repetições.
Repete enquanto a condição for verdadeira.

```py
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

🚨 Cuidado: se a condição nunca mudar para falsa, o loop será **infinito**.

---

## 🧩 Conclusão

* A **indentação** dá estrutura ao código.
* As **condições** controlam o fluxo lógico.
* As **repetições** automatizam tarefas repetitivas.

Juntas, essas ferramentas formam a **base do pensamento lógico em Python**, permitindo criar programas **organizados**, **claros** e **eficientes**.

✍️ **Próxima aula:** [4.1 - strings](../4_strings/1_strings.md)