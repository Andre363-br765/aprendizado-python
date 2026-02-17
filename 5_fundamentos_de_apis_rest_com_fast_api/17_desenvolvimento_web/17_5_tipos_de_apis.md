# Aula 17.5 – Tipos de APIs: RESTful, SOAP e GraphQL

## 🌐 Introdução
Existem diferentes padrões de APIs, que definem como os dados são enviados e recebidos.  
Os três mais conhecidos são: **RESTful**, **SOAP** e **GraphQL**.

---

## 1️⃣ RESTful API
**REST** = Representational State Transfer  
É o tipo mais comum hoje na web, usando protocolo HTTP e regras simples.

**Características:**
- Baseada em recursos (ex: `/usuarios`, `/produtos`)  
- Usa verbos HTTP: GET, POST, PUT, DELETE, PATCH  
- Retorna dados geralmente em JSON  
- Simples, leve e fácil de escalar

**Exemplo de endpoints RESTful:**
| Verbo HTTP | Endpoint        | Função                  |
|------------|----------------|------------------------|
| GET        | /usuarios       | Lista todos os usuários |
| GET        | /usuarios/1     | Mostra usuário específico |
| POST       | /usuarios       | Cria um novo usuário   |
| PUT        | /usuarios/1     | Atualiza usuário       |
| DELETE     | /usuarios/1     | Remove usuário         |

**Exemplo prático (Python):**
```python
import requests

resposta = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(resposta.json())
```

---

## 2️⃣ SOAP (Simple Object Access Protocol)

Protocolo mais antigo e formal, usado em sistemas corporativos.  
Diferente do REST, o SOAP usa **XML** para enviar e receber mensagens.

### Características:
- Baseado em **XML**  
- Usa **HTTP** (ou outros protocolos, ex: SMTP)  
- Estrutura rígida e mais burocrática  
- Ideal para sistemas que exigem alta segurança e padronização

### Exemplo de mensagem SOAP (XML):
```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Body>
    <getUser>
      <id>1</id>
    </getUser>
  </soap:Body>
</soap:Envelope>
```

## 3️⃣ GraphQL

Criado pelo Facebook em 2015, o **GraphQL** é uma alternativa moderna ao REST.  
Ele permite que o cliente defina exatamente **quais dados quer receber** — nem mais, nem menos.

### 🌟 Características
- Usa uma única rota (ex: `/graphql`)  
- Permite consultar apenas os campos necessários  
- Reduz o tráfego de dados e evita requisições desnecessárias  

### 📄 Exemplo de consulta GraphQL
```graphql
{
  usuario(id: 1) {
    nome
    idade
    email
  }
}
```

### 📄 Exemplo de resposta:

```json
{
  "usuario": {
    "nome": "João",
    "idade": 30,
    "email": "joao@email.com"
  }
}
```

## 4️⃣ Comparativo rápido

| Tipo     | Formato | Simplicidade | Flexibilidade | Segurança | Popularidade |
|----------|---------|--------------|---------------|-----------|--------------|
| REST     | JSON    | Alta         | Média         | Boa       | Muito Alta   |
| SOAP     | XML     | Baixa        | Baixa         | Muito Alta| Média        |
| GraphQL  | JSON    | Alta         | Muito Alta    | Boa       | Crescendo    |

---

## 5️⃣ Qual usar?

- ✅ **REST:** ideal para a maioria dos sistemas modernos e APIs públicas  
- ✅ **SOAP:** indicado para grandes empresas e sistemas formais  
- ✅ **GraphQL:** ideal para apps complexos que precisam de controle fino sobre os dados

---

## 🧠 Resumo

- **RESTful:** simples, rápido e usa JSON  
- **SOAP:** baseado em XML, mais pesado e formal  
- **GraphQL:** moderno e muito flexível

---

✍️ **Próxima aula:** [17.6 – Verbos HTTP](17_6_verbos_http.md)