# 🧮 Aula 2.4 – Operadores Lógicos 🔗

> **Objetivo Geral:** Entender o que são operadores lógicos e como utilizá-los em conjunto com operadores de comparação para criar expressões complexas.

---

## 1️⃣ O que são Operadores Lógicos?

Os **operadores lógicos** são usados para **combinar condições** (comparações) em expressões mais elaboradas.  
Eles retornam sempre um valor **booleano**: `True` ou `False`.

Em resumo:
> ➕ Juntam comparações.  
> 🔁 Fazem verificações múltiplas.  
> ✅ Retornam verdadeiro ou falso.

---

## 2️⃣ Expressões Lógicas

Quando usamos operadores de comparação, obtemos valores **booleanos** (`True` / `False`).  
Os operadores lógicos permitem **combinar** essas expressões:

📘 Estrutura geral:
```python
op_comparacao + op_logico + op_comparacao + ...
```

Exemplo:
```python
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)   # True
print(saque <= limite)  # False
```

---

## 3️⃣ Operadores Lógicos em Python

| Operador | Descrição | Exemplo | Resultado |
|:----------:|------------|----------|------------|
| `and` | Verdadeiro se **ambas as condições** forem verdadeiras | `True and True` | `True` |
| `or`  | Verdadeiro se **ao menos uma condição** for verdadeira | `True or False` | `True` |
| `not` | **Inverte** o valor lógico | `not True` | `False` |

---

## 4️⃣ Operador AND (E)

O operador `and` retorna `True` somente se todas as condições forem verdadeiras.
```python
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)
# saldo >= saque → True
# saque <= limite → False
# True and False → False
```
 📘 Resultado: False
 >💡 Dica: Use and quando tudo precisar ser verdadeiro.

---

## 5️⃣ Operador OR (OU)

O operador `or` retorna `True` se pelo menos uma condição for verdadeira.
```python
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque or saque <= limite)
# saldo >= saque → True
# saque <= limite → False
# True or False → True
```
 📘 Resultado: True
 >💡 Dica: Use or quando qualquer uma das condições puder tornar a expressão verdadeira.

---

## 6️⃣ Operador NOT (Negação)

O operador `not` inverte o resultado lógico da expressão.
```python
contatos_emergencia = []

print(not 1000 > 1500)          # True
print(not contatos_emergencia)  # True (lista vazia é falsa)
print(not "saque 1500;")        # False (string não vazia é verdadeira)
print(not "")                   # True (string vazia é falsa)
```
 >💡 Dica: not é útil para verificar se algo não existe, não está definido, ou está vazio.

---

## 7️⃣ Uso de Parênteses 🧩

Os **parênteses** ajudam a definir a ordem de execução das expressões lógicas — assim como na matemática.
```python
saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
# Resultado: True

# Forma mais clara:
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
# Resultado: True
```
 💬 Mesmo resultado, mas a segunda forma é mais legível e segura.

---

## 8️⃣ Exemplo Prático Completo 💼
```python
# --------------------------
# Operadores Lógicos
# --------------------------

saldo, saque, limite = 1000, 200, 100

print("Saldo suficiente e saque dentro do limite?",
      saldo >= saque and saque <= limite)

print("Saldo suficiente ou saque dentro do limite?",
      saldo >= saque or saque <= limite)

transacao_negada = not (saldo >= saque and saque <= limite)
print("Transação negada?", transacao_negada)
```
🖨️ Saída esperada:
```vbnet
Saldo suficiente e saque dentro do limite? False
Saldo suficiente ou saque dentro do limite? True
Transação negada? True
```

---

## 9️⃣ Resumo Rápido

| Operador | Significado | Quando retorna `True` |
|:----------:|--------------|------------------------|
| `and` | **E** | Quando **todas as condições** forem verdadeiras |
| `or`  | **OU** | Quando **pelo menos uma** for verdadeira |
| `not` | **NÃO** | Quando o valor for **falso** (inverte o resultado) |

---

✍️ **Próxima aula:** [2.5 - operadores de identidade](5-operadores_de_identidade.md)