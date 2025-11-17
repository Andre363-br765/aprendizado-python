# 🔁 Parte 3 – Estruturas de Repetição em Python

## 🎯 Objetivo Geral
Conhecer as **estruturas de repetição** `for` e `while` e aprender **quando utilizá-las**.

---

## 🧠 1. O que são estruturas de repetição?

As **estruturas de repetição** permitem que um trecho de código seja executado **mais de uma vez**.  

- O número de repetições pode ser:  
  - **Conhecido previamente** → usamos `for`.  
  - **Determinável através de uma condição lógica** → usamos `while`.

### 📖 Exemplo: sem repetição
```python
print("Linha 1")
print("Linha 2")
print("Linha 3")
```

📖 Exemplo: com repetição (for):
```python
for i in range(3):
    print(f"Linha {i+1}")
```
 🗒️ **Observação:**
 Repetir manualmente cada comando é trabalhoso e pouco eficiente.
 Loops automatizam essa tarefa.

---

## 🔸 2. Comando `for` e a função `range`

### 📝 Comando `for`
O `for` é usado para percorrer um **objeto iterável** (como listas, strings ou sequências de números).  

É ideal quando sabemos o **número exato de repetições** ou queremos percorrer **todos os elementos de um iterável**.

### 📖 Exemplo:
```python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
```

### 📝 Função `range`
A função built-in `range` gera uma **sequência de números inteiros**.

  - **Estrutura:** ```range(start, stop, step)```
   - **start** → início da sequência (opcional, padrão = 0)  
   - **stop** → fim da sequência (obrigatório, exclusivo)  
   - **step** → incremento (opcional, padrão = 1)

#### 📖 Exemplos de `range`:
```py
range(5)        # Produz: 0, 1, 2, 3, 4
range(2, 6)     # Produz: 2, 3, 4, 5
range(1, 10, 2) # Produz: 1, 3, 5, 7, 9
```

#### 📖 Utilizando range com for:
```py
for i in range(5):
    print(f"Número {i}")
```

---

## 🔹 3. Comando while
O `while` repete um bloco enquanto uma condição for verdadeira.
 - Ideal quando não sabemos o número exato de repetições.

### 📖 Exemplo:
```py
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
```
 🗒️ **Observação:**  
 Se a condição nunca se tornar falsa, o loop `while` será **infinito**.  
 Sempre certifique-se de **atualizar variáveis de controle** dentro do loop.

---

## ✅ Checklist de Estruturas de Repetição

1. Use **for** quando souber **quantas vezes repetir** ou quando precisar percorrer um **iterável**.  
2. Use **while** quando a repetição depender de uma **condição lógica**.  
3. Cada bloco dentro do loop deve ser **indentado com +4 espaços**.  
4. Tome cuidado com **loops infinitos** no `while`.  
5. Loops podem ser **aninhados**, mas mantenha a indentação clara para evitar confusão.

---

## 📘 Em resumo:
- Estruturas de repetição permitem **automatizar tarefas repetitivas** e controlar o fluxo de execução.  
- Saber **quando usar `for` ou `while`** é essencial para escrever código eficiente e legível.

✍️ **Próxima aula:** [3.4_resumo_estrutura](4_resumo.md)