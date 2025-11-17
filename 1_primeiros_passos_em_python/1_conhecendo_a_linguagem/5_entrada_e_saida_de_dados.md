# Aula 1.5 – Funções de Entrada e Saída 💬

Aprenda como exibir mensagens na tela e receber informações do usuário usando as funções básicas de **entrada e saída** em Python.

---

## 1️⃣ O que são Funções de Entrada e Saída?

Em qualquer linguagem de programação, precisamos **comunicar com o usuário** — seja para mostrar resultados ou pedir informações.  
Em **Python**, isso é feito com:

| Tipo   | Função   | Descrição                            |
|:-------|:----------|:-------------------------------------|
| Saída  | `print()` | Exibe informações na tela            |
| Entrada| `input()` | Recebe dados digitados pelo usuário  |

---

## 2️⃣ Exibindo Informações com `print()` 🖨️

A função **`print()`** é usada para mostrar valores, textos e resultados no terminal.

### 🧩 Exemplo:
```python
print("Olá, mundo!")       # Exibe texto simples
print(10 + 5)              # Exibe o resultado de uma operação
```
💬 Saída:
```less
Olá, mundo!
15
```

---

3️⃣ Exibindo Variáveis no `print()` 📦
```python
Você pode combinar texto com variáveis de várias formas:
nome = "Ana"
idade = 20

print("Nome:", nome, "Idade:", idade)
```
💬 Saída:
```makefile
Nome: Ana Idade: 20
```

---

## 4️⃣ F-Strings – A Forma Moderna de Exibir Dados ✨

As f-strings permitem incluir variáveis diretamente dentro do texto, tornando o código mais limpo e legível.
```py
print(f"Nome: {nome}, Idade: {idade}")
```
💬 Saída:
```makefile
Nome: Ana, Idade: 20
```
### 💡 Dica:
Dentro das `{}`, você pode até fazer cálculos:
```py
print(f"Daqui a 5 anos, {nome} terá {idade + 5} anos.")
```

---

## 5️⃣ Personalizando a Saída com `sep` e `end` 🧩

A função `print()` aceita dois parâmetros especiais para ajustar a forma de exibição:

| Parâmetro | Função | Exemplo | Saída |
|------------|---------|----------|--------|
| `sep` | Define o **separador** entre os itens | `print("A", "B", sep="#")` | `A#B` |
| `end` | Define o que será exibido **no final da linha** | `print("Olá", end="...")` | `Olá...` |

Exemplo completo:
```py
print(nome, idade, end="...\n")     # Mantém na mesma linha
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")
```

💬 Saída:
```text
Ana 20...
Ana#20...
Ana#20
```

---

## 6️⃣ Recebendo Dados do Usuário com `input()` ⌨️

A função `input()` pausa o programa e espera o usuário digitar algo.
O valor digitado é sempre uma string por padrão.
```py
usuario = input("Digite seu nome: ")
print("Olá,", usuario)
```

💬 Exemplo de interação:
```text
Digite seu nome: Ana
Olá, Ana
```

---

## 7️⃣ Convertendo o Tipo de Entrada 🧠

Como tudo que vem do `input()` é uma string, precisamos converter quando queremos números:
```py
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

💬 Exemplo:
```text
Digite sua idade: 20
Digite sua altura: 1.65
```

🔎 Sem conversão:
```py
idade = input("Idade: ")
print(idade + 5)  # ❌ ERRO! não pode somar string com número
```

✅ Com conversão:
```py
idade = int(input("Idade: "))
print(idade + 5)  # OK!
```

---

8️⃣ Exemplo Completo 💻
```py
def exemplos_saida():
    nome = "Ana"
    idade = 20
    print("Olá, mundo!")
    print(10 + 5)
    print("Nome:", nome, "Idade:", idade)
    print(f"Nome: {nome}, Idade: {idade}")
    print(nome, idade, end="...\n")
    print(nome, idade, sep="#", end="...\n")
    print(nome, idade, sep="#")

def exemplos_entrada():
    # Recebendo dados do usuário (comente ou descomente para testar)
    # usuario = input("Digite seu nome: ")
    # print("Olá,", usuario)
    # idade = int(input("Digite sua idade: "))
    # altura = float(input("Digite sua altura: "))
    pass

if __name__ == "__main__":
    exemplos_saida()
    # exemplos_entrada()  # Ative se quiser testar input()
```

---

## 9️⃣ Resumo Rápido 🧾

| Função / Recurso | Tipo        | Descrição                                      | Exemplo                          |
|------------------|-------------|------------------------------------------------|----------------------------------|
| `print()`        | Saída       | Exibe mensagens no terminal                    | `print("Olá")`                   |
| `input()`        | Entrada     | Lê dados do usuário (string)                   | `input("Digite: ")`              |
| `sep`            | Saída       | Altera o separador entre valores               | `print("A", "B", sep="#")`       |
| `end`            | Saída       | Altera o final da linha                        | `print("A", end="...")`          |
| `int()` / `float()` | Conversão | Converte o texto recebido pelo `input()`       | `int(input("Idade: "))`          |
| `f"..."`         | Formatação  | Insere variáveis dentro do texto               | `f"Olá {nome}"`                  |

✍️ **Próxima aula:** [1.6 - resumo](6_resumo.md)