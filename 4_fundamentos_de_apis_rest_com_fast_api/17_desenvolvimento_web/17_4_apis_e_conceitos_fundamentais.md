# Aula 17.4 – APIs e Conceitos Fundamentais

## 1️⃣ O que é uma API?
**API** = Application Programming Interface (Interface de Programação de Aplicações)  
É um conjunto de regras que permite que diferentes sistemas conversem entre si.

💡 **Analogia:**  
Uma API é como um garçom:  
- Leva o pedido do cliente (front-end) até a cozinha (back-end)  
- Traz a resposta de volta para o cliente

**Exemplo real:**  
O aplicativo de clima no seu celular usa uma API para buscar informações do tempo em um servidor e exibir na tela.

---

## 2️⃣ Como uma API funciona
- **Cliente:** faz uma requisição HTTP (ex: GET)  
- **Servidor (API):** recebe a requisição, processa e envia uma resposta (geralmente em JSON)

**Estrutura geral:**

Request → `https://api.exemplo.com/usuarios`
Response ← {"id": 1, "nome": "Ana", "idade": 25}

---

## 3️⃣ Tipos de APIs
As mais usadas são **APIs baseadas em HTTP (Web APIs)**.

**Formatos comuns de dados:**
- **JSON (JavaScript Object Notation):** mais comum  
- **XML (Extensible Markup Language):** usado em sistemas mais antigos

---

## 4️⃣ Por que as APIs são importantes?
- Permitem que sistemas diferentes troquem dados facilmente  
- Aplicativos móveis e sites podem usar os mesmos dados  
- Empresas podem disponibilizar serviços publicamente (ex: Google Maps, Twitter)

---

## 5️⃣ Exemplo prático com Python
```python
import requests

# Requisição GET para API pública
url = "https://api.agify.io/?name=joao"
resposta = requests.get(url)

# Exibe os dados retornados
print("Status:", resposta.status_code)  # 200 = sucesso
print("Dados JSON:", resposta.json())   # ex: {'name': 'joao', 'age': 32, 'count': 12345}
```

---

## 7️⃣ Estrutura básica de uma API (Flask)
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/mensagem')
def mensagem():
    return jsonify({"mensagem": "Olá! Esta é uma API simples."})

app.run()
```

---

## 6️⃣ Endpoints

Um **endpoint** é o “endereço” (rota) de um recurso dentro da API.

**Exemplos:**
- `https://api.meusite.com/usuarios` → retorna todos os usuários  
- `https://api.meusite.com/usuarios/1` → retorna o usuário com ID 1

## 8️⃣ Diferença entre API e Sistema Web

- **Sistema Web:** tem interface visual (HTML, CSS, JS)  
- **API:** não tem interface; só fornece dados para outros sistemas

---

## 🧠 Resumo

- ✅ API é uma ponte de comunicação entre sistemas  
- ✅ Usa protocolo HTTP (requisições e respostas)  
- ✅ Retorna dados em JSON ou XML  
- ✅ Muito usada para conectar front-end e back-end  

---

✍️ **Próxima aula:** [17.5 – Tipos de APIs](17_5_tipos_de_apis.md)
