# 🧩 Parte 1 – Indentação e Blocos em Python

## 🎯 Objetivo Geral
Aprender como o **interpretador Python** utiliza a **indentação do código** para delimitar os **blocos de comandos**.

---

## ✨ A estética e a função da indentação

Indentação (ou **identar o código**) é o ato de mover linhas de código para dentro (geralmente com **4 espaços**), tornando o código **mais legível e organizado**.  
Em muitas linguagens, isso é apenas uma questão **estética**.  
Mas em **Python**, a indentação é **obrigatória** e **funcional**.

> 💡 Em Python, a indentação **não é apenas estilo**, é **parte da sintaxe da linguagem**.  
> O interpretador **usa a indentação** para saber onde **um bloco começa e termina**.

---

## 🧱 Bloco de Comando

Em linguagens como **C** ou **Java**, os blocos são delimitados por **chaves `{ }`** ou palavras reservadas.  
No **Python**, os blocos são delimitados **somente pela indentação**.

### 🔸 Exemplo: Bloco em Java
```java
if (x > 0) {
    System.out.println("Número positivo");
} else {
    System.out.println("Número não positivo");
}
```
 🧠 Em Java, o uso das chaves define os blocos.

### 🔹 Mesmo bloco em Python
```Python
if x > 0:
    print("Número positivo")
else:
    print("Número não positivo")
```
 🧠 Em Python, os espaços (indentação) cumprem esse papel.

---

## 👁️ Comparando visualmente

### Sem formatador (errado em Python):
```Python
if x > 0:
print("Número positivo")
else:
print("Número não positivo")
```
 ❌ Isso gera um erro de indentação:
 ```Python
 IndentationError: expected an indented block
 ```

### Com formatador (correto):
```Python
if x > 0:
    print("Número positivo")
else:
    print("Número não positivo")
```
 ✅ Agora o código está correto e legível.

---

## ✅ Conclusão

- A indentação em Python **substitui o uso de símbolos** como `{}`.
- Cada bloco é delimitado por **níveis de indentação**.
- Um código bem identado é **mais fácil de entender e evita erros**.
- Python **obriga** o programador a manter uma estrutura visual **clara e organizada**.

---

## 📘 Em resumo:

 Enquanto outras linguagens permitem “código bagunçado” com chaves,
 o Python **exige clareza** — e isso o torna **mais legível e elegante** por natureza.

✍️ **Próxima aula:** [3.2 - estruturas condicionais em python](2_estruturas_condicionais_em_python.md)