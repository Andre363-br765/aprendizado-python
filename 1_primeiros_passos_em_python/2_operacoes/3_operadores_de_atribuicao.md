# 🧮 Aula 2.3 – Operadores de Atribuição 💾

> Nesta aula, você vai aprender o que são **operadores de atribuição** e como utilizá-los para atualizar valores de variáveis de forma prática e rápida.

---

## 1️⃣ O que são Operadores de Atribuição?

Os **operadores de atribuição** servem para **definir** ou **atualizar** o valor de uma variável.  
Eles são usados para **armazenar resultados de cálculos** diretamente na própria variável.

👉 Em resumo: **atribuem um novo valor** a uma variável.

---

## 2️⃣ Atribuição Simples

A forma mais básica é o **sinal de igual (`=`)**, usado para **inicializar ou redefinir** o valor de uma variável.

```python
saldo = 500
print(saldo)  # 500
```

---

## 3️⃣ Atribuição com Operadores Matemáticos

O Python permite **combinar a atribuição com operações aritméticas**, tornando o código mais **compacto e legível**.

| Operador | Exemplo | Equivalente a... | Resultado Final |
|:----------:|------------------|--------------------------|------------------|
| `+=` | `saldo += 200` | `saldo = saldo + 200` | Soma e atualiza |
| `-=` | `saldo -= 100` | `saldo = saldo - 100` | Subtrai e atualiza |
| `*=` | `saldo *= 2` | `saldo = saldo * 2` | Multiplica e atualiza |
| `/=` | `saldo /= 5` | `saldo = saldo / 5` | Divide e atualiza *(float)* |
| `//=` | `saldo //= 5` | `saldo = saldo // 5` | Divide *(inteiro)* e atualiza |
| `%=` | `saldo %= 480` | `saldo = saldo % 480` | Guarda o resto da divisão |
| `**=` | `saldo **= 2` | `saldo = saldo ** 2` | Eleva e atualiza |

---

## 4️⃣ Exemplos Práticos 💡

```python
# --------------------------
# Operadores de Atribuição
# --------------------------

saldo = 500
print("Saldo inicial:", saldo)

saldo += 200    # soma
print("Após depósito:", saldo)

saldo -= 100    # subtração
print("Após saque:", saldo)

saldo *= 2      # multiplicação
print("Saldo dobrado:", saldo)

saldo /= 5      # divisão
print("Dividindo o saldo:", saldo)

saldo //= 2     # divisão inteira
print("Divisão inteira:", saldo)

saldo %= 480    # resto da divisão
print("Resto da divisão:", saldo)

saldo **= 2     # potência
print("Saldo ao quadrado:", saldo)
```
🖨️ Saída esperada (valores variam conforme o ponto de partida):
```yaml
Saldo inicial: 500
Após depósito: 700
Após saque: 600
Saldo dobrado: 1200
Dividindo o saldo: 240.0
Divisão inteira: 120.0
Resto da divisão: 120.0
Saldo ao quadrado: 14400.0
```

---

5️⃣ Exemplo Completo 🧮

```python
# --------------------------
# Operadores de Atribuição (Resumo)
# --------------------------

saldo = 1500
saldo += 500     # 2000
saldo -= 300     # 1700
saldo *= 2       # 3400
saldo /= 2       # 1700.0
saldo //= 100    # 17.0
saldo %= 7       # 3.0

print("Saldo final:", saldo)
```
 🧾 Resultado final: 3.0

---

##  6️⃣ Dica Extra 💬

Você também pode usar operadores de atribuição com strings e listas!

```python
mensagem = "Olá"
mensagem += ", mundo!"
print(mensagem)  # "Olá, mundo!"

lista = [1, 2]
lista += [3, 4]
print(lista)     # [1, 2, 3, 4]
```

---

## 7️⃣ Resumo Rápido

| Operador | Ação                     | Exemplo        | Resultado |
|:----------:|---------------------------|----------------|------------|
| `=`   | Atribuição simples        | `x = 10`        | `10`  |
| `+=`  | Soma e atribui            | `x += 5`        | `15`  |
| `-=`  | Subtrai e atribui         | `x -= 3`        | `12`  |
| `*=`  | Multiplica e atribui      | `x *= 2`        | `24`  |
| `/=`  | Divide e atribui          | `x /= 4`        | `6.0` |
| `//=` | Divide inteiro e atribui  | `x //= 2`       | `3.0` |
| `%=`  | Guarda o resto            | `x %= 2`        | `1.0` |
| `**=` | Eleva e atribui           | `x **= 3`       | `1.0` |

✍️ **Próxima aula:** [2.4 - Operadores lógicos](4_operadores_logicos.md)