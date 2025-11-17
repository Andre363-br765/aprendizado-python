# 🧵 **Resumo — Aula 4: Strings**

## ✔️ **O que você aprendeu neste módulo**

As *strings* representam textos em Python, e neste módulo você viu como manipulá-las com eficiência usando métodos, interpolação, fatiamento e strings de múltiplas linhas.

---

# ## **1. Métodos úteis da classe string**

### 🔤 Transformações de texto

* `upper()` → tudo maiúsculo
* `lower()` → tudo minúsculo
* `capitalize()` → primeira letra maiúscula
* `title()` → iniciais maiúsculas

### 🧼 Remoção de espaços

* `strip()` → remove dos dois lados
* `lstrip()` → esquerda
* `rstrip()` → direita

### 🔗 Divisão e junção

* `split()` → divide em lista
* `"separador".join(lista)` → junta elementos

### 📏 Outros

* `len()` → tamanho da string
* `replace(a, b)` → troca trechos
* `in` → verifica substring

---

# ## **2. Interpolação de Variáveis**

### Três formas:

#### 1. **Old Style (%)**

Pouco usado hoje.

#### 2. **`format()`**

Versátil, funciona com nomes e índices.

#### 3. **F-Strings (recomendado)**

Simples, moderno, suporta cálculos.

Exemplo:

```python
print(f"{nome} tem {idade} anos")
```

---

# ## **3. Fatiamento de Strings (Slicing)**

Usa a sintaxe:

```
[start : stop : step]
```

### Exemplos:

* `texto[:6]` → do início até o índice 5
* `texto[7:]` → do 7 até o final
* `texto[::-1]` → inverte a string
* `texto[::2]` → pega de 2 em 2

Serve para extrair partes específicas da string.

---

# ## **4. Strings de Múltiplas Linhas**

Criadas com:

* `'''   '''`
* `"""   """`

Elas **mantêm todas as quebras de linha e espaços**.

Também podem ser usadas com f-strings:

```python
f"""Nome: {nome}
Idade: {idade}"""
```

---

# 🎓 **Conclusão**

Neste módulo você aprendeu a:

* Manipular textos com métodos úteis
* Inserir variáveis dentro de strings
* Fatiar e extrair partes de textos
* Criar textos organizados com múltiplas linhas

Essas técnicas são essenciais para qualquer programa que lide com **entrada, saída, mensagens, arquivos e interfaces**.

---

✍️ **Próxima aula:** [5.1 - Listas]()