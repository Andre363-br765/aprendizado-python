# 📘 **Aula 2.2 – Operadores de Comparação (Expandida)**

> Aprenda a comparar valores em Python usando operadores que retornam **True** ou **False**, essenciais para condições, decisões e lógica de programas.

---

## 🧠 **1️⃣ O que são operadores de comparação?**

Operadores de comparação servem para **verificar relações** entre valores.
Toda comparação retorna apenas **duas opções**:

* `True` → verdadeiro
* `False` → falso

Esses operadores são a base de estruturas como `if`, `while`, validações e sistemas lógicos.

---

## 📊 **2️⃣ Tabela completa de operadores**

| Operação       | Símbolo | Exemplo    | Resultado | Descrição                               |
| -------------- | ------- | ---------- | --------- | --------------------------------------- |
| Igualdade      | `==`    | `10 == 10` | `True`    | Verifica se dois valores são iguais     |
| Diferente      | `!=`    | `10 != 5`  | `True`    | Verifica se dois valores são diferentes |
| Maior que      | `>`     | `10 > 5`   | `True`    | Se o valor da esquerda é maior          |
| Menor que      | `<`     | `3 < 2`    | `False`   | Se o valor da esquerda é menor          |
| Maior ou igual | `>=`    | `10 >= 10` | `True`    | Maior ou igual                          |
| Menor ou igual | `<=`    | `5 <= 7`   | `True`    | Menor ou igual                          |

---

## 🧪 **3️⃣ Exemplos básicos**

```python
x = 10
y = 5

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
```

🔎 Saída:

```
x == y: False
x != y: True
x > y: True
x < y: False
x >= y: True
x <= y: False
```

---

## 🔍 **4️⃣ Comparação funciona com…**

### ✔️ Números

```python
print(20 > 10)  # True
```

### ✔️ Strings (ordem alfabética – comparação lexicográfica)

```python
print("Ana" == "Ana")   # True
print("ana" == "Ana")   # False (case-sensitive)
print("bola" > "abacate")  # True → b vem depois de a
```

### ✔️ Booleanos

`True` → vale como `1`
`False` → vale como `0`

```python
print(True > False)  # True (1 > 0)
```

---

## ⚠️ **5️⃣ Comparações inválidas**

Python **não permite** comparar tipos totalmente diferentes:

```python
# print(10 > "10")   # ❌ Erro: TypeError
```

Sempre mantenha tipos coerentes antes de comparar.

---

## 🧬 **6️⃣ Comparação encadeada (recurso exclusivo do Python)**

Python permite comparar valores como na matemática:

```python
print(5 < 10 < 20)   # True
print(5 < 10 > 3)    # True
```

Equivalente a:

```python
print(5 < 10 and 10 < 20)
```

💡 Muito útil em validações:

```python
idade = 17
print(13 <= idade <= 19)  # Verifica "adolescente"
```

---

## 🧠 **7️⃣ Comparações com floats (atenção à precisão)**

```python
print(0.1 + 0.2 == 0.3)  # False (imprecisão de ponto flutuante)
```

Use `round()` se quiser comparar com precisão controlada:

```python
print(round(0.1 + 0.2, 1) == 0.3)  # True
```

---

## 🧪 **8️⃣ Exemplos práticos**

### ✔️ Verificando idade mínima:

```python
idade = 18
print(idade >= 18)  # True
```

### ✔️ Checando senha:

```python
senha_digitada = "1234"
senha_correta = "1234"
print(senha_digitada == senha_correta)
```

### ✔️ Comparando notas:

```python
media = 7.5
print(media >= 7)   # Aprovado?
```

---

## 💡 **9️⃣ Boas práticas**

1. **Não use comparação desnecessária com booleanos**

   ```python
   if ativo == True:     # ❌ errado
   if ativo:             # ✔️ certo
   ```

2. **Use nomes de variáveis que explicam a lógica**

   ```python
   idade_usuario >= IDADE_MINIMA
   ```

3. **Cuidado com maiúsculas e minúsculas em strings**

   ```python
   nome.lower() == "joão"
   ```

4. **Evite comparar floats diretamente sem arredondar**

---

## 💻 **🔟 Exemplo completo**

```python
def exemplos_comparacao():
    x = 10
    y = 5

    print("x == y:", x == y)
    print("x != y:", x != y)
    print("x > y:", x > y)
    print("x < y:", x < y)
    print("x >= y:", x >= y)
    print("x <= y:", x <= y)

    # Comparações com strings
    nome1 = "Ana"
    nome2 = "ana"
    print("Nomes iguais?", nome1 == nome2)

    # Comparação encadeada
    idade = 17
    print("É adolescente?", 13 <= idade <= 19)

    # Comparação com float
    print("0.1 + 0.2 == 0.3?", 0.1 + 0.2 == 0.3)
    print("Arredondando:", round(0.1 + 0.2, 1) == 0.3)


if __name__ == "__main__":
    exemplos_comparacao()
```

---

## 🧾 **Resumo rápido**

| Operador | Significado    | Exemplo    | Resultado |
| -------- | -------------- | ---------- | --------- |
| `==`     | Igual          | `7 == 7`   | True      |
| `!=`     | Diferente      | `7 != 5`   | True      |
| `>`      | Maior          | `10 > 2`   | True      |
| `<`      | Menor          | `2 < 10`   | True      |
| `>=`     | Maior ou igual | `10 >= 10` | True      |
| `<=`     | Menor ou igual | `2 <= 3`   | True      |

---

