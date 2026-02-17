# Aula 17.3 – Tecnologias Front-end e Back-end

## 🌐 Introdução
O desenvolvimento web é dividido em duas grandes áreas:  
- **Front-end:** o lado que o usuário vê e interage  
- **Back-end:** o lado que processa, guarda e envia os dados

---

## 1️⃣ Front-end
É a parte visual da aplicação — o que aparece na tela do navegador.

### Linguagens principais
- **HTML:** estrutura da página (os "blocos" de conteúdo)  
- **CSS:** aparência (cores, tamanhos, layout)  
- **JavaScript:** interatividade (menus, animações, cliques, formulários dinâmicos)

### Tecnologias e frameworks populares
- React (JavaScript)  
- Vue.js  
- Angular  
- Bootstrap (CSS)  
- Tailwind (CSS utilitário)

### Função
Criar interfaces bonitas, rápidas e responsivas.

### Exemplo simples de front-end (HTML + CSS + JS)
```html
<html>
  <head>
    <style>
      button { background: blue; color: white; padding: 10px; }
    </style>
  </head>
  <body>
    <button onclick="alert('Olá!')">Clique aqui</button>
  </body>
</html>
```

## 2️⃣ Back-end

O **Back-end** é o cérebro da aplicação. Fica no servidor, processando pedidos, salvando dados e aplicando regras de negócio.

### Linguagens e frameworks populares
- **Python:** Django, Flask, FastAPI  
- **JavaScript:** Node.js, Express  
- **PHP:** Laravel  
- **Java:** Spring Boot  
- **C#:** ASP.NET  
- **Ruby:** Rails

### Função
- Receber requisições do **Front-end**  
- Acessar o banco de dados  
- Processar informações  
- Devolver respostas ao cliente

### Exemplo simples (servidor com Flask em Python)
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, mundo! Este é o Back-end respondendo."

app.run()
```

## 3️⃣ Como Front-end e Back-end trabalham juntos

1. O usuário interage com o **Front-end** (navegador)  
2. O Front-end envia uma **requisição HTTP** para o **Back-end**  
3. O Back-end processa, acessa o banco de dados e envia uma **resposta**  
4. O Front-end exibe o resultado na tela

---

## 4️⃣ Banco de Dados

Local onde as informações são armazenadas.

- **Relacional (SQL):** MySQL, PostgreSQL, SQLite  
- **Não-relacional (NoSQL):** MongoDB, Firebase, Redis

---

## 5️⃣ Pilhas de Tecnologias (Stacks)

São combinações comuns de ferramentas usadas juntas.

- **LAMP:** Linux + Apache + MySQL + PHP  
- **MERN:** MongoDB + Express + React + Node.js  
- **PERN:** PostgreSQL + Express + React + Node.js  
- **Django + PostgreSQL:** muito usada com Python

---

## 🧠 Resumo

- **Front-end:** experiência do usuário (HTML, CSS, JS)  
- **Back-end:** lógica e dados (Python, Node, PHP, Java)  
- **Comunicação:** via HTTP e troca de informações em JSON  

---

✍️ **Próxima aula:** [17.4 – APIs e Conceitos Fundamentais](17_4_apis_e_conceitos_fundamentais.md)