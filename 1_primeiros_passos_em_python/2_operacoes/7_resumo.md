# 🧮 Módulo 2 – Operadores em Python

Neste módulo, aprendemos sobre os **principais operadores da linguagem Python** — ferramentas essenciais para realizar **cálculos, comparações, atribuições e verificações lógicas**.

Esses operadores são a **base para controlar o fluxo de decisões** e o **comportamento das variáveis** em qualquer programa.

---

## 📚 Índice das Aulas

|                    Aula                   | Título                      | Conteúdo Principal                                                                        |
| :---------------------------------------: | :-------------------------- | :---------------------------------------------------------------------------------------- |
|   [2.1](#aula-21--operações-aritméticas)  | 🧮 Operações Aritméticas    | Realiza cálculos matemáticos: soma, subtração, multiplicação, divisão, módulo e potência. |
| [2.2](#aula-22--operadores-de-comparação) | ⚖️ Operadores de Comparação | Compara valores, retornando `True` ou `False`.                                            |
| [2.3](#aula-23--operadores-de-atribuição) | 💼 Operadores de Atribuição | Define ou atualiza valores de variáveis.                                                  |
|    [2.4](#aula-24--operadores-lógicos)    | 🔗 Operadores Lógicos       | Combina condições com `and`, `or` e `not`.                                                |
| [2.5](#aula-25--operadores-de-identidade) | 🆔 Operadores de Identidade | Verifica se dois objetos ocupam a mesma posição na memória.                               |
| [2.6](#aula-26--operadores-de-associação) | 🧩 Operadores de Associação | Testa se um elemento está presente (ou não) em uma sequência.                             |

---

## 🧮 Aula 2.1 – Operações Aritméticas

Os operadores aritméticos permitem realizar cálculos matemáticos básicos e avançados.

| Operação         | Símbolo | Exemplo   | Resultado |
| ---------------- | ------- | --------- | --------- |
| Soma             | `+`     | `10 + 5`  | `15`      |
| Subtração        | `-`     | `10 - 5`  | `5`       |
| Multiplicação    | `*`     | `10 * 5`  | `50`      |
| Divisão          | `/`     | `10 / 5`  | `2.0`     |
| Divisão inteira  | `//`    | `10 // 3` | `3`       |
| Resto da divisão | `%`     | `10 % 3`  | `1`       |
| Potência         | `**`    | `2 ** 3`  | `8`       |
 📘 Precedência dos operadores:

 1. Parênteses
 2. Expoentes
 3. Multiplicações e divisões
 4. Somas e subtrações

---

## ⚖️ Aula 2.2 – Operadores de Comparação

Comparam valores e retornam verdadeiro (`True`) ou falso (`False`).

| Operador | Significado    | Exemplo    | Resultado |
| :------: | -------------- | ---------- | --------- |
|   `==`   | Igualdade      | `10 == 10` | `True`    |
|   `!=`   | Diferença      | `10 != 5`  | `True`    |
|    `>`   | Maior que      | `8 > 3`    | `True`    |
|    `<`   | Menor que      | `2 < 5`    | `True`    |
|   `>=`   | Maior ou igual | `7 >= 7`   | `True`    |
|   `<=`   | Menor ou igual | `6 <= 4`   | `False`   |

---

## 💼 Aula 2.3 – Operadores de Atribuição

Definem valores para variáveis ou atualizam o valor existente.

| Operador | Exemplo   | Equivalente a | Resultado       |
| :------: | --------- | ------------- | --------------- |
|    `=`   | `x = 10`  | —             | `10`            |
|   `+=`   | `x += 5`  | `x = x + 5`   | Soma            |
|   `-=`   | `x -= 5`  | `x = x - 5`   | Subtração       |
|   `*=`   | `x *= 5`  | `x = x * 5`   | Multiplicação   |
|   `/=`   | `x /= 5`  | `x = x / 5`   | Divisão         |
|   `//=`  | `x //= 5` | `x = x // 5`  | Divisão inteira |
|   `%=`   | `x %= 5`  | `x = x % 5`   | Módulo          |
|   `**=`  | `x **= 2` | `x = x ** 2`  | Potência        |
 > 💡 Dica: use parênteses para deixar as expressões mais legíveis!
---

## 🔗 Aula 2.4 – Operadores Lógicos

Permitem combinar múltiplas condições.

| Operador | Significado                               | Exemplo                | Resultado |
| :------: | ----------------------------------------- | ---------------------- | --------- |
|   `and`  | Verdadeiro se **todas** forem verdadeiras | `(10 > 5) and (8 > 2)` | `True`    |
|   `or`   | Verdadeiro se **uma** for verdadeira      | `(10 > 5) or (8 < 2)`  | `True`    |
|   `not`  | Inverte o resultado lógico                | `not (10 > 5)`         | `False`   |
 
 🧠 Exemplo:
 ```py
 curso = "Python"
 nome_curso = curso
 print(curso is nome_curso)      # True
 print(curso is not nome_curso)  # False
 ```

---

## 🧩 Aula 2.6 – Operadores de Associação

Verificam se um elemento está presente (ou não) em uma sequência.

| Operador | Significado          | Exemplo                | Resultado |
| :------: | -------------------- | ---------------------- | --------- |
|   `in`   | Presença do elemento | `"banana" in frutas`   | `True`    |
| `not in` | Ausência do elemento | `"maçã" not in frutas` | `True`    |

---

## 🧾 Resumo Geral do Módulo

| Tipo de Operador | Função            | Exemplo             | Resultado   |
| ---------------- | ----------------- | ------------------- | ----------- |
| Aritmético       | Calcula valores   | `10 + 5`            | `15`        |
| Comparação       | Compara valores   | `10 > 5`            | `True`      |
| Atribuição       | Define valores    | `x += 2`            | `x = x + 2` |
| Lógico           | Combina condições | `(x > 0 and y < 5)` | `True`      |
| Identidade       | Compara objetos   | `a is b`            | `True`      |
| Associação       | Verifica presença | `"a" in texto`      | `True`      |

---

### 🧠 Conclusão

 Com os operadores, conseguimos controlar o comportamento das variáveis e decisões em nossos programas.
 Eles formam a base da lógica de programação — sem eles, o Python não saberia comparar, calcular ou decidir o que fazer.

✍️ **Próxima aula:** [3.1 - Indentação e blocos em python](../3_estrutura_condicional/1_Indentação_e_blocos_em_python.md)