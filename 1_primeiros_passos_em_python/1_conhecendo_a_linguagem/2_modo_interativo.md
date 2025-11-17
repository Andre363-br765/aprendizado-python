Aqui está a **versão revisada, padronizada e levemente melhorada** da sua **Aula 1.2 – Modo Interativo e Funções Úteis 💡**.
Agora ela está no mesmo estilo das outras aulas, com explicações claras, seções equilibradas e sem excesso de conteúdo técnico que poderia quebrar o ritmo.

---

# 📘 Aula 1.2 – Modo Interativo e Funções Úteis 💡

> Aprenda a usar o **modo interativo do Python (REPL)** e as funções nativas que ajudam a explorar o comportamento dos objetos.

---

## 1️⃣ O que é o Modo Interativo (REPL)? 🐍

O **modo interativo** é um ambiente onde você digita um comando e vê o resultado na hora — perfeito para testar ideias rapidamente.

Para abrir, digite no terminal:

```bash
python
```

Se tudo estiver certo, o Python exibirá:

```python
>>>
```

Agora é só testar comandos:

```python
>>> 10 + 5
15

>>> print("Olá, Python!")
Olá, Python!
```

> 💡 **Ótimo para testar funções, cálculos, conversões e pequenos trechos de código.**

---

## 2️⃣ Explorando Objetos com `dir()` 🔍

A função `dir()` mostra **todos os métodos e atributos** disponíveis para um objeto.

```python
texto = "Python"
print(dir(texto))
```

Saída (resumida):

```python
['capitalize', 'count', 'find', 'lower', 'upper', ...]
```

> 💡 Ajuda a descobrir *o que dá pra fazer* com um tipo de dado.

---

## 3️⃣ Entendendo Funções e Objetos com `help()` 📘

A função `help()` mostra a **documentação completa** de qualquer objeto, módulo ou função.

```python
help(str)
```

Ou algo mais específico:

```python
help(str.upper)
```

Exemplo de resultado:

```plaintext
upper() -> str
    Return a copy of the string converted to uppercase.
```

> 💡 Use `help()` SEM MEDO — programadores profissionais usam o tempo todo.

---

## 4️⃣ Outras Funções Úteis 🧠

| Função     | Finalidade                    | Exemplo                       |
| ---------- | ----------------------------- | ----------------------------- |
| `type()`   | Mostra o tipo de um valor     | `type(10)` → `int`            |
| `len()`    | Conta elementos               | `len("Python")` → `6`         |
| `id()`     | Endereço de memória do objeto | `id("a")`                     |
| `sum()`    | Soma de itens numéricos       | `sum([1,2,3])` → `6`          |
| `max()`    | Maior valor                   | `max([4, 1, 9])` → `9`        |
| `min()`    | Menor valor                   | `min([4, 1, 9])` → `1`        |
| `sorted()` | Ordena itens                  | `sorted([3,1,2])` → `[1,2,3]` |

---

## 5️⃣ Exemplo Prático 💻

```python
def exemplos_modo_interativo():
    texto = "Python"

    print(dir(texto))     # Lista métodos
    print(texto.upper())  # Usa um método
    print(len(texto))     # Conta caracteres
    print(type(texto))    # Tipo do objeto
    help(str)             # Documentação de strings

if __name__ == "__main__":
    exemplos_modo_interativo()
```

---

## 6️⃣ Resumo Rápido 🧾

| Função      | Uso                       | Objetivo      |
| ----------- | ------------------------- | ------------- |
| `dir(obj)`  | Lista métodos e atributos | Exploração    |
| `help(obj)` | Mostra documentação       | Aprendizado   |
| `type(obj)` | Tipo do objeto            | Identificação |
| `len(obj)`  | Conta itens               | Tamanho       |

---

✍️ **Próxima aula:** *1.3 – Variáveis e Constantes*

---

Se quiser, posso escrever a **Aula 1.3** agora no mesmo padrão. Quer que eu faça?
