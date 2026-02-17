# 🧮 Resumo — Conjuntos (Sets)

## 1. O que são conjuntos

Um **set** é uma coleção que **não permite elementos repetidos**.  
Podemos usar sets para representar **conjuntos matemáticos** ou **remover duplicatas** de listas, strings ou outros iteráveis.

---

## 2. Como criar conjuntos

**Exemplos de criação:**

```python
# A partir de uma lista (duplicatas são removidas)
set([1, 2, 3, 1, 3, 4])  # Resultado: {1, 2, 3, 4}

# A partir de uma string
set("java")  # Resultado: {'j', 'a', 'v'}

# A partir de uma tupla
set(("java", "html", "css"))  # Resultado: {'java', 'html', 'css'}
```

---

## 3. Acessando elementos

Conjuntos em Python **não suportam indexação nem fatiamento**.
Para acessar elementos, converta o set em **lista** ou **tupla**:

```python
numeros = {1, 2, 3, 4}
numeros_lista = list(numeros)
print(numeros_lista[0])  # Exibe o primeiro elemento da lista
```

---

## 4. Principais métodos de sets

| Método             | Descrição                                            |
| ------------------ | ---------------------------------------------------- |
| `add(x)`           | Adiciona um elemento `x` ao set                      |
| `update(iterável)` | Adiciona múltiplos elementos de um iterável          |
| `remove(x)`        | Remove o elemento `x` (gera erro se não existir)     |
| `discard(x)`       | Remove o elemento `x` (não gera erro se não existir) |
| `pop()`            | Remove e retorna um elemento aleatório               |
| `clear()`          | Remove todos os elementos do set                     |
| `copy()`           | Retorna uma cópia do set                             |

---

## 5. Operações matemáticas com conjuntos

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.union(B)                 # União: {1, 2, 3, 4, 5}
A.intersection(B)          # Interseção: {3}
A.difference(B)            # Diferença: {1, 2}
A.symmetric_difference(B)  # Diferença simétrica: {1, 2, 4, 5}
```

---

## 🎓 Conclusão

Neste resumo você aprendeu a:

* Criar conjuntos (`set`) e remover duplicatas
* Acessar elementos convertendo o set para lista ou tupla
* Usar métodos úteis da classe `set`
* Realizar operações matemáticas com conjuntos

Estas técnicas são essenciais para manipulação de coleções e eliminação de duplicatas em Python.
