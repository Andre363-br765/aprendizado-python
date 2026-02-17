# 📘 Aula 2.6 – Operadores de Associação

## 🎯 Objetivo Geral

Entender o que são **operadores de associação** e como utilizá-los para **verificar se um elemento faz parte de uma sequência** (como listas, strings, tuplas, conjuntos ou dicionários).

---

## 🧠 O que são Operadores de Associação?

Os **operadores de associação** são usados para **verificar se um objeto está presente ou não dentro de uma sequência**.  
Eles permitem, por exemplo, descobrir se **uma palavra faz parte de uma frase** ou se **um item está em uma lista**.

---

### 🔹 Esses operadores são aplicáveis a:

- **Listas**
- **Tuplas**
- **Strings**
- **Dicionários**
- **Conjuntos (sets)**

---
## 🧮 Operadores Disponíveis

| Operador | Significado                                  | Exemplo                | Resultado |
| :------: | -------------------------------------------- | ---------------------- | --------- |
|   `in`   | Verifica se o elemento está presente         | `"uva" in frutas`      | ✅ `True`  |
| `not in` | Verifica se o elemento **não** está presente | `"maçã" not in frutas` | ✅ `True`  |

💻 Exemplo prático:
```py
# --------------------------
# Operadores de Associação
# --------------------------
# Exemplo prático de uso dos operadores "in" e "not in"

frutas = ["laranja", "banana", "uva", "abacate", "pera"]
verduras = ["alface", "couve", "espinafre", "brócolis"]
legumes = ["cenoura", "batata", "abobrinha"]

# Verificando presença
print("banana está em frutas?", "banana" in frutas)
print("maçã está em frutas?", "maçã" in frutas)

# Usando com variáveis
item = "batata"
if item in legumes:
    print(f"{item} é um legume.")
else:
    print(f"{item} não é um legume.")

# Usando com strings
feira = "feira da fruta"
print("A palavra 'fruta' está em feira?", "fruta" in feira)
print("A palavra 'legume' não está em feira?", "legume" not in feira)
```

🖥️ Saída esperada:
```sql
banana está em frutas? True
maçã está em frutas? False
batata é um legume.
A palavra 'fruta' está em feira? True
A palavra 'legume' não está em feira? True
```

---

## 💡 Dica importante
O operador `in` pode ser usado em strings, listas, tuplas, sets e até em dicionários:
```py
numeros = (10, 20, 30)
print(20 in numeros)   # True

carros = {"marca": "Ford", "ano": 2020}
print("marca" in carros)   # True → verifica se existe a CHAVE
```

---

## 🧠 Resumo Rápido

| Situação            | Código                        | Resultado |
| :------------------ | :---------------------------- | :-------- |
| Elemento presente   | `"banana" in frutas`          | `True`    |
| Elemento ausente    | `"maçã" in frutas`            | `False`   |
| Negação de presença | `"maçã" not in frutas`        | `True`    |
| Verificar substring | `"fruta" in "feira da fruta"` | `True`    |

---

✍️ **Próxima aula:** [2.6 - Operadores de associação](../3_estrutura_condicional/1_Indentação_e_blocos_em_python.md)