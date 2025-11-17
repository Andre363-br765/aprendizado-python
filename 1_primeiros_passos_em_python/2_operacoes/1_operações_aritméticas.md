# 🧮 Aula 2 – Operadores e Atribuições em Python

Nesta aula, vamos entender como funcionam os principais **operadores da linguagem Python**.  
Eles são responsáveis por realizar cálculos, comparações, atribuições, verificações lógicas e muito mais.

---

## 📘 Aula 2.1 – Operações Aritméticas

Os **operadores aritméticos** permitem realizar cálculos matemáticos básicos e avançados.

| Operação           | Símbolo | Exemplo   | Resultado |
|--------------------|----------|------------|------------|
| Soma               | `+`      | `10 + 5`   | `15`       |
| Subtração          | `-`      | `10 - 5`   | `5`        |
| Multiplicação      | `*`      | `10 * 5`   | `50`       |
| Divisão            | `/`      | `10 / 5`   | `2.0`      |
| Divisão inteira    | `//`     | `10 // 5`  | `2`        |
| Resto da divisão   | `%`      | `10 % 5`   | `0`        |
| Potência           | `**`     | `10 ** 5`  | `100000`   |

---

### 1️⃣ Exemplos práticos
```python
print(1 + 1)   # 2 → soma
print(10 - 2)  # 8 → subtração
print(4 * 3)   # 12 → multiplicação
print(12 / 3)  # 4.0 → divisão normal
print(12 // 5) # 2 → divisão inteira
print(10 % 3)  # 1 → resto da divisão
print(2 ** 3)  # 8 → exponenciação
```

---

### 2️⃣ Precedência de Operadores

Em Python (como na matemática), a **ordem das operações importa**. Segue a hierarquia:

1. **Parênteses** `( )` → Sempre resolvidos primeiro  
2. **Expoentes** `**` → Potenciação  
3. **Multiplicação** `*`, **Divisão** `/`, **Divisão inteira** `//` e **Módulo** `%` → Executados da esquerda para a direita  
4. **Soma** `+` e **Subtração** `-` → Executados da esquerda para a direita

---

#### Exemplos Práticos:

```python
print(10 - 5 * 2)       # 0 → multiplicação antes da subtração
print((10 - 5) * 2)     # 10 → parênteses alteram a ordem
print(10**2 * 2)        # 200 → expoente antes da multiplicação
print(10**(2*2))        # 10000 → parênteses definem ordem dos expoentes
print(10 / 2 * 4)       # 20.0 → divisão e multiplicação da esquerda para a direita
```
 >💡 **Dica:** Sempre use parênteses para deixar a ordem de cálculo clara e evitar erros inesperados.

### 3️⃣ Resumo Rápido 🧾

| Operador | Operação          | Exemplo   | Resultado |
|----------|-----------------|-----------|-----------|
| `+`      | Adição           | `2 + 3`   | `5`       |
| `-`      | Subtração        | `5 - 2`   | `3`       |
| `*`      | Multiplicação    | `4 * 3`   | `12`      |
| `/`      | Divisão normal   | `12 / 3`  | `4.0`     |
| `//`     | Divisão inteira  | `12 // 5` | `2`       |
| `%`      | Módulo (resto)   | `10 % 3`  | `1`       |
| `**`     | Exponenciação    | `2 ** 3`  | `8`       |

---

✍️ **Próxima aula:** [2.2 - Operadores de comparacao](2_Operadores_de_comparacao.md)