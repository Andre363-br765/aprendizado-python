# 🧮 Aula 2.2 – Operadores de Comparação 🔍

> Aprenda como **comparar valores** em Python usando operadores lógicos e relacionais.

---

## 1️⃣ O que são Operadores de Comparação?

Os **operadores de comparação** servem para comparar dois valores e retornar um resultado **booleano** (`True` ou `False`).  
Eles são muito usados em **condições**, como em `if`, `while` e loops em geral.

---

## 2️⃣ Tabela de Operadores de Comparação

| Operador | Descrição                          | Exemplo         | Resultado |
|----------|------------------------------------|----------------|-----------|
| `==`     | Igual a                             | `5 == 5`       | `True`    |
| `!=`     | Diferente de                        | `5 != 3`       | `True`    |
| `>`      | Maior que                           | `10 > 5`       | `True`    |
| `<`      | Menor que                           | `3 < 5`        | `True`    |
| `>=`     | Maior ou igual a                    | `5 >= 5`       | `True`    |
| `<=`     | Menor ou igual a                    | `3 <= 5`       | `True`    |

---

## 3️⃣ Exemplos Práticos

```python
# --------------------------
# Operadores de Comparação
# --------------------------
saldo, saque = 1500, 700

print("Saldo == saque?", saldo == saque)   # False
print("Saldo != saque?", saldo != saque)   # True
print("Saldo > saque?", saldo > saque)     # True
print("Saldo >= saque?", saldo >= saque)   # True
print("Saldo < saque?", saldo < saque)     # False
print("Saldo <= saque?", saldo <= saque)   # False
```

---

## 4️⃣ Comparações Combinadas (AND / OR / NOT) 🧠

Podemos combinar comparações usando **operadores lógicos**, que retornam `True` ou `False`.

| Operador | Descrição | Exemplo | Resultado |
|----------|-----------|---------|-----------|
| `and`    | E lógico  | `True and False` | `False` |
| `or`     | OU lógico | `True or False`  | `True`  |
| `not`    | Negação   | `not True`       | `False` |

### Exemplos Práticos:

```python
saldo, saque = 1500, 700

# E lógico
print("Saldo > 1000 e saque < 800?", saldo > 1000 and saque < 800)  # True

# OU lógico
print("Saldo < 1000 ou saque > 500?", saldo < 1000 or saque > 500)  # True

# Negação
print("Não é verdade que saldo < saque?", not saldo < saque)        # True
```

---

## 5️⃣ Comparando Diferentes Tipos ⚠️

Em Python, **comparações entre tipos diferentes** podem gerar resultados inesperados ou erros.

```python
print(10 == "10")  # False → int não é igual a string
print(10 != "10")  # True
print(10 > "5")    # ❌ TypeError em Python 3
```

> 💡 **Dica:** Sempre verifique os tipos antes de comparar, ou use conversão (int(), float()) se necessário.

---

## 6️⃣ Resumo Rápido 🧾

| Operador | Tipo de Comparação | Exemplo            | Resultado   |
|----------|------------------|------------------|------------|
| `==`     | Igualdade         | `x == y`         | True/False |
| `!=`     | Diferença         | `x != y`         | True/False |
| `>`      | Maior que         | `x > y`          | True/False |
| `<`      | Menor que         | `x < y`          | True/False |
| `>=`     | Maior ou igual    | `x >= y`         | True/False |
| `<=`     | Menor ou igual    | `x <= y`         | True/False |
| `and`    | E lógico          | `cond1 and cond2`| True/False |
| `or`     | OU lógico         | `cond1 or cond2` | True/False |
| `not`    | Negação           | `not cond`       | True/False |

---

✍️ **Próxima aula:** [2.3 - operadores de atribuição](3_operadores_de_atribuicao.md)