# 🧮 Resumo Completo — Conjuntos (Sets) em Python

## 1. O que são conjuntos

Um **set** é uma coleção **não ordenada** de elementos **únicos**, ou seja, **não permite duplicatas**.  
Eles são ideais para representar **conjuntos matemáticos** ou **eliminar elementos repetidos** de listas, strings ou outros iteráveis.

💡 Observação: sets **não possuem índice**, portanto não suportam fatiamento ou acesso direto por posição.

---

## 2. Criando conjuntos

### 2.1 A partir de iteráveis

```python
# A partir de uma lista
set([1, 2, 3, 1, 3, 4])  # Resultado: {1, 2, 3, 4}

# A partir de uma string
set("python")  # Resultado: {'p','y','t','h','o','n'}

# A partir de uma tupla
set(("java", "html", "css"))  # Resultado: {'java','html','css'}
````

### 2.2 Conjunto vazio

```python
# Forma correta
meu_set = set()

# Atenção: {} cria um dicionário vazio, não um set
```

---

## 3. Acessando elementos

Como sets não têm índice, para acessar elementos é necessário **converter para lista ou tupla**:

```python
numeros = {10, 20, 30}
numeros_lista = list(numeros)
print(numeros_lista[0])  # Pode exibir qualquer elemento, ordem não garantida
```

---

## 4. Principais métodos da classe `set`

| Método             | Descrição                                      | Exemplo               |
| ------------------ | ---------------------------------------------- | --------------------- |
| `add(x)`           | Adiciona um elemento ao set                    | `s.add(5)`            |
| `update(iterável)` | Adiciona vários elementos                      | `s.update([6,7])`     |
| `remove(x)`        | Remove elemento (erro se não existir)          | `s.remove(5)`         |
| `discard(x)`       | Remove elemento (não gera erro se não existir) | `s.discard(5)`        |
| `pop()`            | Remove e retorna um elemento aleatório         | `s.pop()`             |
| `clear()`          | Remove todos os elementos                      | `s.clear()`           |
| `copy()`           | Retorna uma cópia do set                       | `novo_set = s.copy()` |
| `len()`            | Retorna o tamanho                              | `len(s)`              |
| `in`               | Verifica se elemento existe                    | `3 in s`              |

---

## 5. Operações matemáticas com conjuntos

```python
A = {1, 2, 3}
B = {3, 4, 5}

# União
A.union(B)  # {1, 2, 3, 4, 5}

# Interseção
A.intersection(B)  # {3}

# Diferença
A.difference(B)  # {1, 2}

# Diferença simétrica
A.symmetric_difference(B)  # {1, 2, 4, 5}
```

### 5.1 Operadores equivalentes

```python
A | B   # União
A & B   # Interseção
A - B   # Diferença
A ^ B   # Diferença simétrica
```

---

## 6. Conjuntos imutáveis — `frozenset`

Um **frozenset** é **imutável**, ou seja, não permite alterações após a criação.
Útil como chave de dicionários ou elementos de outros sets.

```python
s = frozenset([1,2,3])
# s.add(4)  # Erro, não pode alterar
```

---

## 7. Conversão entre tipos

```python
# Lista para set
lista = [1,2,2,3]
set(lista)  # {1,2,3}

# String para set
set("banana")  # {'b','a','n'}

# Set para lista ou tupla
meu_set = {1,2,3}
list(meu_set)   # [1,2,3]
tuple(meu_set)  # (1,2,3)
```

---

## 8. Dicas importantes

* Sets **não mantêm ordem**.
* Útil para **eliminar duplicatas** rapidamente.
* Pode-se usar operadores ou métodos para **operações matemáticas**.
* Para conjuntos imutáveis, use **frozenset**.

---

## 🎓 Conclusão

Aprendemos a:

* Criar e manipular **conjuntos** (`set`) e **conjuntos imutáveis** (`frozenset`)
* Acessar elementos convertendo para lista ou tupla
* Usar **métodos importantes** como `add`, `remove`, `update`, `discard`, `pop`
* Realizar **operações matemáticas** com conjuntos: união, interseção, diferença e diferença simétrica

Conjuntos são essenciais para **eliminar duplicatas**, **comparar coleções** e **trabalhar com lógica matemática** em Python.