# 🧮 Aula 2.5 – Operadores de Identidade 🧠

> **Objetivo Geral:** Entender o que são operadores de identidade e como utilizá-los para comparar **referências na memória** em Python.

---

## 1️⃣ O que são Operadores de Identidade?

Os **operadores de identidade** são usados para verificar se **duas variáveis apontam para o mesmo objeto na memória**.

Diferente dos operadores de **comparação** (`==` e `!=`), que comparam **valores**,  
os operadores de identidade comparam **endereços de memória**.

📘 Em outras palavras:
> ➕ `==` → compara se os **valores** são iguais.  
> 🔁 `is` → compara se as **variáveis são o mesmo objeto** na memória.

---

## 2️⃣ Operadores Disponíveis

| Operador | Descrição | Exemplo | Resultado |
|-----------|------------|----------|------------|
| `is` | Retorna `True` se os objetos forem o mesmo na memória | `a is b` | `True` |
| `is not` | Retorna `True` se os objetos forem diferentes na memória | `a is not b` | `False` |

---

## 3️⃣ Exemplo Prático 🧩

```python
curso = "curso de py"
nome_curso = curso

saldo, limite = 200, 200

print(curso is nome_curso)      # True  (mesma referência)
print(curso is not nome_curso)  # False (é o mesmo objeto)
print(saldo is limite)          # True  (inteiros pequenos são otimizados em memória)
```
💬 Saída esperada:
```python
True
False
True
```

---

## 4️⃣ Diferença entre == e is
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  → Os valores são iguais
print(a is b)   # False → São objetos diferentes na memória
```
 >💡 Mesmo que listas ou strings tenham o mesmo conteúdo, isso não significa que ocupam o mesmo espaço de memória.

---

## 5️⃣ Testando com `None` 🧱

O valor especial `None` (sem valor) é comumente verificado com `is` — não com `==`.
```python
valor = None

print(valor is None)      # ✅ Forma correta
print(valor == None)      # ⚠️ Evite usar essa forma
```
 >💬 Por convenção e clareza, use sempre `is None` ou `is not None`.

---

## 6️⃣ Exemplo Completo 💻
```python
# --------------------------
# Operadores de Identidade
# --------------------------
limite, saque = 500, 500

print("saque é limite?", saque is limite)
print("saque não é limite?", saque is not limite)

x = limite
print("x é limite?", x is limite)

valor = None
print("valor é None?", valor is None)
```
```sql
🖨️ Saída esperada:
saque é limite? True
saque não é limite? False
x é limite? True
valor é None? True
```

---

## 7️⃣ Resumo Rápido 🧾

| Operador | Tipo | Descrição | Exemplo | Resultado |
|:----------:|--------|------------|------------|------------|
| `is` | Identidade | Verdadeiro se as variáveis forem o **mesmo objeto** | `a is b` | `True` |
| `is not` | Identidade | Verdadeiro se as variáveis forem **objetos diferentes** | `a is not b` | `True` |
| `==` | Comparação | Compara apenas os **valores** | `[1, 2] == [1, 2]` | `True` |
| `is` | Identidade | Compara a **referência na memória** | `[1, 2] is [1, 2]` | `False` |

---

✍️ **Próxima aula:** [2.6 - Operadores de associação](6_operadores_de_associacao.md)