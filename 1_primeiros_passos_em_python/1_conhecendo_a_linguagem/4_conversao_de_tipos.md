# Aula 1.4 – Conversão de Tipos (Casting) 🔄

> Entenda como transformar dados de um tipo para outro em **Python** — um recurso essencial para evitar erros e trabalhar com informações de diferentes formatos.

---

## 1️⃣ O que é Conversão de Tipos?

A **conversão de tipos** (ou *type casting*) é o processo de transformar um valor de um tipo em outro.

Por exemplo:

- Converter um número em texto (`int → str`)
- Converter um texto em número (`str → int` ou `float`)
- Converter valores em `bool` para verificar se são **verdadeiros** ou **falsos**

Em Python, isso é feito com as funções:
```python
int(), float(), str(), bool()
```

---

## 2️⃣ Conversão para Inteiro (int) 🔢

A função `int()` converte valores para inteiro.
Ela remove casas decimais e também pode converter strings numéricas.

```py
# Float → Int
preco = 10.30
print(preco)      # 10.3
preco = int(preco)
print(preco)      # 10

# String → Int
idade = "28"
print(int(idade))  # 28

# Erro de conversão
texto = "python"
# print(int(texto))  # ❌ ValueError: não é possível converter
```

## 3️⃣ Conversão para Decimal (`float`) 💧
```py
# Int → Float
preco = 10
print(preco)        # 10
preco = float(preco)
print(preco)        # 10.0

# String → Float
valor = "10.50"
print(float(valor))  # 10.5
```

💡 Dica: Use `float()` quando precisar de valores com casas decimais, como preços, médias, ou medidas.

---

## 4️⃣ Conversão para Texto (str) ✍️
```py
Transforma qualquer valor em texto (string).
Muito útil para exibir informações ou concatenar valores com frases.

vpreco = 10.50
idade = 28

print(str(preco))  # "10.5"
print(str(idade))  # "28"

texto = f"Idade {idade} | Preço {preco}"
print(texto)       # Idade 28 | Preço 10.5
```
   Sempre converta números em `str` antes de concatenar com textos!

---

## 5️⃣ Conversão para Booleano (bool) ⚙️

A função `bool()` converte valores para **verdadeiro (True)** ou **falso (False)**.

| Valor convertido | Resultado | Observação |
|------------------|------------|-------------|
| `bool(1)`        | `True`     | Qualquer número ≠ 0 é verdadeiro |
| `bool(0)`        | `False`    | Zero é falso |
| `bool("")`       | `False`    | String vazia é falsa |
| `bool("Python")` | `True`     | Qualquer string não vazia é verdadeira |

Exemplo:
```py
v1, v2, v3, v4 = bool(1), bool(0), bool(""), bool("Python")
print(v1, v2, v3, v4)
```
 💡 **Dica:** Essas conversões são muito usadas em **condições** (`if`, `while`, etc.), onde o Python avalia se algo é verdadeiro ou falso automaticamente.

---

## 6️⃣ Diferença entre Divisão Normal e Inteira ➗

Em Python, há dois tipos de divisão:

| Operação | Símbolo | Resultado | Exemplo |
|-----------|----------|------------|----------|
| **Divisão normal** | `/` | Retorna *float* | `100 / 2` → `50.0` |
| **Divisão inteira** | `//` | Descarta decimais | `100 // 2` → `50` |

Exemplo em código:

```python
print(100 / 2)   # 50.0 → divisão normal (float)
print(100 // 2)  # 50   → divisão inteira (int)
```

## 7️⃣ Exemplo Completo 💻

```py
def exemplos_conversao():
    # Para inteiro
    x = int(3.14)
    y = int("10")
    print(x, y)

    # Para float
    a = float(10)
    b = float("10.10")
    print(a, b)

    # Para string
    preco = 10.50
    idade = 28
    print(str(preco))
    print(str(idade))
    texto = f"Idade {idade} | Preço {preco}"
    print(texto)

    # Para booleano
    v1, v2, v3, v4 = bool(1), bool(0), bool(""), bool("Python")
    print(v1, v2, v3, v4)

    # Divisão normal vs inteira
    preco = 10
    print(preco / 2)   # 5.0
    print(preco // 2)  # 5

if __name__ == "__main__":
    exemplos_conversao()
```

---

## 8️⃣ Resumo Rápido 🧾

| Função | De → Para | Exemplo | Resultado |
|--------|------------|----------|------------|
| `int()` | Float/String → Int | `int(3.9)` | `3` |
| `float()` | Int/String → Float | `float("10.5")` | `10.5` |
| `str()` | Qualquer tipo → String | `str(100)` | `"100"` |
| `bool()` | Qualquer tipo → Bool | `bool("")` | `False` |
| `/` | Divisão normal | `10 / 3` | `3.333...` |
| `//` | Divisão inteira | `10 // 3` | `3` |

---

✍️ **Próxima aula:** [1.5 – Entrada e Saída de Dados](5_entrada_e_saida_de_dados.md)
