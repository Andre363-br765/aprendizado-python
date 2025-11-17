# ⚙️ Parte 2 – Estruturas Condicionais em Python

## 🎯 Objetivo Geral
Compreender **o que são as estruturas condicionais** e **como utilizá-las** para controlar o fluxo de execução de um programa em Python.

---

## 🧠 O que são estruturas condicionais?

As **estruturas condicionais** permitem que um programa **tome decisões** com base em **expressões lógicas** (verdadeiras ou falsas).

Em outras palavras, elas controlam **“o que fazer”** dependendo do resultado de uma condição.

> 💡 O Python executa apenas o **bloco de código** cuja condição for **verdadeira**.  
> Caso contrário, ele ignora aquele bloco e passa para o próximo.

---

## 🔸 1. `if` – Condicional simples

O comando `if` testa uma **expressão lógica**.  
Se o resultado for **verdadeiro (`True`)**, o código dentro do bloco será executado.

### 📖 Exemplo:
```python
idade = 20

if idade >= 18:
    print("Você é maior de idade.")
```
 🗒️ Explicação:
 A condição `idade >= 18` é verdadeira, então a mensagem é exibida.

---

## 🔸 2. **if / else – Condicional com dois desvios**

O `else` é usado para tratar o **caso contrário**, ou seja, quando a condição do `if` **não é satisfeita**.

### 📖 Exemplo:

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```
 🗒️ Explicação:
 Se a condição for falsa, o código do `else` será executado.

---

## 🔸 3. if / elif / else – Condicional com múltiplos caminhos

Quando há mais de duas possibilidades, usamos `elif` (abreviação de else if).

### 📖 Exemplo:
```python
nota = 85

if nota >= 90:
    print("Excelente!")
elif nota >= 70:
    print("Bom desempenho.")
else:
    print("Precisa melhorar.")
```

#### Explicação

Se a primeira condição (`nota >= 90`) for falsa, o Python testa a próxima (`nota >= 70`).
Se nenhuma for verdadeira, executa o **bloco do `else`**.

⚠️ **Dica:**  
Não existe um número máximo de `elif`, mas evite **condições demais**, pois deixam o código mais difícil de entender.

---

## 🔹 4. Estruturas Condicionais Aninhadas

Também é possível colocar uma condição dentro de outra.  
Isso é chamado de **if aninhado (nested if)**.

### 📖 Exemplo:
```python
nota = 95

if nota >= 60:
    print("Aprovado!")
    if nota >= 90:
        print("Aprovado com excelência!")
else:
    print("Reprovado.")
```
#### 🗒️ Explicação:
O segundo `if` só é testado se o primeiro for verdadeiro.

💡 **Boas práticas:**  
- Use `if` aninhado apenas quando necessário.  
- Caso contrário, prefira separar a lógica em funções.

---

## 🔸 5. if ternário – Condicional em uma linha  
O `if` ternário é uma forma compacta de escrever uma condição simples.

### 📖 Estrutura:
```arduino
valor_se_verdadeiro if condição else valor_se_falso
```

### 📖 Exemplo:
```py
idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
```

#### 🗒️ Explicação:  
O Python avalia a condição `idade >= 18`.

- Se for verdadeira → `status` recebe `"Maior de idade"`.  
- Caso contrário → `"Menor de idade"`.

⚠️ **Atenção:**  
Use o **if ternário** apenas para expressões curtas.  
Para blocos maiores, prefira o **if tradicional**.

---

## ✅ Conclusão  
- As estruturas condicionais controlam o fluxo de execução do código.  
- O Python executa apenas o bloco cuja condição for verdadeira.  
- Podemos usar `if`, `if/else`, `if/elif/else`, e também criar condições aninhadas.
- O **if ternário** é útil para escrever condições simples em **uma única linha**.

---

## 📘 Em resumo:  
- Estruturas condicionais são o cérebro das decisões em Python.  
- Elas permitem que o programa pense e aja conforme as situações.

---

✍️ **Próxima aula:** [3.3 Estruturas de Repetição em python](3_estruturas_de_repetição_em_python.md)