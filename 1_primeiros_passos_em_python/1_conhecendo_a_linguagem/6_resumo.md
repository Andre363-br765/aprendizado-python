# 🐍 Aula 1 – Conhecendo a Linguagem Python

## 📘 Conteúdos
1. **Tipos de dados básicos** – strings, números inteiros, floats e booleanos.  
2. **Modo interativo e funções úteis** – uso do terminal e função `dir()`.  
3. **Variáveis e constantes** – criação, boas práticas e listas.  
4. **Conversão de tipos (casting)** – `int()`, `float()`, `str()`, `bool()` e diferenças de divisão.  
5. **Entrada e saída de dados** – `print()` e `input()`, além dos parâmetros `end` e `sep`.

---
## 📚 Índice das Aulas

|                           Aula                          | Título                                 | Conteúdo Principal                                                         |
| :-----------------------------------------------------: | :------------------------------------- | :------------------------------------------------------------------------- |
|        [1.1](#🧩-aula-11--tipos-de-dados-básicos)       | 🧩 Tipos de Dados Básicos              | Principais tipos (`int`, `float`, `str`, `bool`) e uso da função `type()`. |
| [1.2](#💬-aula-12--modo-interativo-e-ferramentas-úteis) | 💬 Modo Interativo e Ferramentas Úteis | Testar comandos com o terminal e explorar objetos com `dir()`.             |
|        [1.3](#📦-aula-13--variáveis-e-constantes)       | 📦 Variáveis e Constantes              | Diferença entre valores mutáveis e imutáveis, boas práticas e exemplos.    |
|      [1.4](#🔄-aula-14--conversão-de-tipos-casting)     | 🔄 Conversão de Tipos (Casting)        | Transformar tipos de dados: `int()`, `float()`, `str()`, `bool()`.         |
|     [1.5](#🖥️-aula-15--funções-de-entrada-e-saída)     | 🖥️ Funções de Entrada e Saída         | Uso de `print()` e `input()`, e parâmetros `sep` e `end`.                  |

---

## 🧩 Aula 1.1 – Tipos de Dados Básicos

### 🔹 Tipos principais

| Tipo | Exemplo | Descrição |
|------|----------|------------|
| `int` | `10` | Número inteiro |
| `float` | `3.14` | Número decimal |
| `complex` | `2 + 3j` | Número complexo |
| `bool` | `True`, `False` | Lógico (verdadeiro/falso) |
| `str` | `"Olá, mundo!"` | Cadeia de texto |

💡 **Dica:** use `type(valor)` para saber o tipo de uma variável.

---

## 💬 Aula 1.2 – Modo Interativo e Ferramentas Úteis

O **modo interativo** do Python é ótimo para testar comandos rapidamente.  
Pode ser acessado via:

- Terminal → `python` ou `python3`  
- IDLE (interface oficial do Python)  
- Ou executando scripts com `python -i arquivo.py`

💡 Permite **testar código, fazer cálculos e explorar funções** sem precisar criar arquivos.

### 🧠 Função útil: `dir()`

Mostra todos os métodos e propriedades disponíveis para um objeto:

```python
texto = "Python"
print(dir(texto))
```
  💡 Ideal para descobrir o que pode ser feito com cada tipo de dado.

---

## 📦 Aula 1.3 – Variáveis e Constantes
🔹 Variáveis

Servem para armazenar valores que podem mudar:
```py
nome = "Ana"
idade = 20
altura = 1.65
```

💡 Você pode alterar o valor a qualquer momento:
```py
idade = 21
nome = "Leo"
```

🔹 Constantes

Não mudam durante a execução (por convenção, nome em MAIÚSCULAS):
```py
PI = 3.14159
TAXA = 0.05
DIAS_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
```

### 💡 Boas práticas

1. Use nomes claros (`saldo_total`, `idade_usuario`)
2. Evite sobrescrever palavras reservadas (`for`, `if`, `print`)
3. Use maiúsculas em constantes (`PI`, `MAX_USUARIOS`)

---

## 🔄 Aula 1.4 – Conversão de Tipos (Casting)

Converter valores é comum ao lidar com entradas de usuário ou cálculos.

🔹 Exemplos:
```py
# int()
x = int(3.14)
y = int("10")

# float()
a = float(10)
b = float("10.10")

# str()
valor = 10
valor_str = str(valor)

# bool()
v1 = bool(1)      # True
v2 = bool(0)      # False
v3 = bool("")     # False
v4 = bool("abc")  # True
```

🔹 Diferença entre divisões
```py
print(100 / 2)   # 50.0 -> float
print(100 // 2)  # 50   -> inteiro
```

---

## 🖥️ Aula 1.5 – Funções de Entrada e Saída
🔹 Saída de dados com `print()`
```py
nome = "Ana"
idade = 20

print("Nome:", nome, "Idade:", idade)
print(f"Nome: {nome}, Idade: {idade}")
```

🧱 **Parâmetros úteis**

| Parâmetro | Função                | Exemplo                              |
|------------|----------------------|--------------------------------------|
| `sep`      | Define o separador   | `print("A", "B", sep="#") → A#B`     |
| `end`      | Define o final da linha | `print("Oi", end="!") → Oi!`       |

🔹 **Entrada de dados com `input()`**

```python
usuario = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Olá {usuario}, idade {idade}, altura {altura}m")
```

💡 **Dica:**  
Por padrão, `input()` sempre retorna **string**, então é preciso converter quando for número.

---

# 📘 Resumo Geral (Aulas 1 a 5)

| **Tema**              | **Conceito Principal**                          | **Exemplo**            |
|-----------------------|--------------------------------------------------|------------------------|
| **Tipos de dados**    | Diferentes formas de armazenar informações      | `int`, `float`, `str`, `bool` |
| **Modo interativo**   | Testar código direto no terminal                | `>>> print(2 + 2)`     |
| **Variáveis**         | Armazenam valores mutáveis                      | `idade = 18`           |
| **Constantes**        | Valores fixos, usados como referência           | `PI = 3.14`            |
| **Conversão de tipos**| Mudar o tipo de um dado                         | `float("10.5")`        |
| **Saída**             | Exibir dados                                    | `print()`              |
| **Entrada**           | Receber dados do usuário                        | `input()`              |

---

## ✅ Boas Práticas Gerais

- Use **nomes claros e descritivos** para variáveis.  
- Sempre **converta tipos** antes de usar em cálculos (`int()`, `float()`).  
- Utilize **f-strings** para formatar saídas.  
- Mantenha **constantes em maiúsculas**.  
- **Teste comandos pequenos** no modo interativo antes de colocá-los no script.

✍️ **Próxima aula:** [2.1 - operacoes](../2_operacoes/1_operações_aritméticas.md)