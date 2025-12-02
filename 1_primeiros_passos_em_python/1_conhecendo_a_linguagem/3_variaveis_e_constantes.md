# 📘 Aula 1.3 – Variáveis e Constantes 📝

> Aprenda a criar, alterar e utilizar **variáveis** e **constantes** em Python, com exemplos práticos e boas práticas de código.

---

## 1️⃣ O que são Variáveis?

Variáveis são **nomes que armazenam valores**.
Elas podem mudar ao longo da execução do programa.

### Exemplos:

```python
nome = "Ana"          # String
idade = 20            # Inteiro
altura = 1.65         # Float
ligado = True         # Booleano
saldo = 1500.50       # Float
ativo = False         # Booleano
```

Exibindo valores:

```python
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Ligado?", ligado)
print("Saldo:", saldo)
print("Ativo?", ativo)
```

> 💡 Use `print("-" * 30)` para criar divisores no terminal.

---

## 2️⃣ Alterando valores de variáveis

Variáveis podem ser modificadas livremente:

```python
idade = 21
nome = "Leo"

print("Após alteração -> Nome:", nome, "| Idade:", idade)
```

---

## 3️⃣ Variáveis que guardam listas

Listas permitem armazenar **múltiplos valores**:

```python
limite_saque = 1000
BRAZILIAN_STATES = ["RS", "SP", "RJ", "SC"]  # Constante por convenção

print("Estados brasileiros:", BRAZILIAN_STATES)
```

---

## 4️⃣ Operações com variáveis

Python permite operações matemáticas e lógicas entre variáveis:

```python
total = saldo + limite_saque
print("Total disponível:", total)
```

---

## 5️⃣ Constantes em Python

Python **não possui constantes verdadeiras**, mas usamos **nomes em MAIÚSCULAS** para indicar que não devem ser alteradas.

```python
PI = 3.14159
TAXA = 0.05
MAX_USUARIOS = 1000
DIAS_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

print("PI:", PI)
print("Taxa:", TAXA)
print("Máximo de usuários:", MAX_USUARIOS)
print("Dias da semana:", DIAS_SEMANA)
```

---

## 6️⃣ Boas práticas ao nomear variáveis e constantes

### ✔ 1. Use nomes descritivos

```python
saldo_conta = 1500
idade_usuario = 21
```

### ✔ 2. Constantes sempre em MAIÚSCULAS

```python
MAX_ITENS = 50
```

### ✔ 3. Evite nomes genéricos

Evite: `x`, `y`, `data`, `valor`
Prefira: `idade_usuario`, `preco_produto`, `data_cadastro`.

### ✔ 4. Mantenha o tipo consistente

Evite mudar o tipo de uma variável sem motivo:

```python
saldo = 1500.50
saldo = "agora é texto"
```

---

## 7️⃣ Exemplo Completo

```python
def exemplos_variaveis():
    nome = "Ana"
    idade = 20
    saldo = 1500.50

    print("Nome:", nome)
    print("Idade:", idade)
    print("Saldo:", saldo)

    # Alterando valores
    nome = "Leo"
    idade = 21
    print("Após alteração -> Nome:", nome, "| Idade:", idade)

    # Lista e constantes
    BRAZILIAN_STATES = ["RS", "SP", "RJ", "SC"]
    PI = 3.14159

    print("Estados:", BRAZILIAN_STATES)
    print("PI:", PI)

if __name__ == "__main__":
    exemplos_variaveis()
```

---

✍️ **Próxima aula:** [1.4 – Conversao_De_Tipos](4_conversao_de_tipos.md)