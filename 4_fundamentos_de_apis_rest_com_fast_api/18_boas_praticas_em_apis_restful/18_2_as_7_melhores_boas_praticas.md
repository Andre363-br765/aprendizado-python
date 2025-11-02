# Aula 18.2 – As 7 Melhores Boas Práticas para APIs RESTful

Seguindo padrões de design RESTful, podemos organizar a API de forma profissional. Aqui estão 7 práticas fundamentais:

---

## 1️⃣ Utilização de Substantivos em Rotas
Use **substantivos plurais** para representar recursos:

❌ Incorreto: `/getUsers`, `/retrieveAllProducts`  
✅ Correto: `/users`, `/products`, `/orders`

---

## 2️⃣ Utilização de Métodos HTTP
- `GET` → recuperar recursos  
- `POST` → criar novos recursos  
- `PUT` / `PATCH` → atualizar recursos existentes  
- `DELETE` → excluir recursos

---

## 3️⃣ Hierarquia e Aninhamento em Rotas
Para recursos relacionados, use URLs consistentes:

✅ `/users/{userId}/orders` → pedidos de um usuário específico

---

## 4️⃣ Nomes de Ações
Evite verbos na URL; use o método HTTP adequado:

✅ `POST /users` para criar um usuário (não `/createUser`)

---

## 5️⃣ Versionamento de Rotas
Permite evoluir a API sem quebrar clientes existentes:

- `/v1/users`  
- `/v2/users`

---

## 6️⃣ Parâmetros de Consulta
Use query params para filtros, paginação e ordenação:

✅ `/products?category=electronics&limit=10&page=1&sort=price`

---

## 7️⃣ Tratamento de Erros
Use códigos de status HTTP apropriados:

- `200 OK` → sucesso  
- `400 Bad Request` → requisição inválida  
- `404 Not Found` → recurso não encontrado

> Referência: [Boas Práticas para APIs RESTful](https://aline-antunes.gitbook.io/boas-praticas-para-apis-restful/boas-praticas-para-apis-restful/por-que-seguir-boas-praticas)

---

✍️ **Próxima aula:** [18.3 – Exemplo de Estrutura de Rotas](18_3_exemplo_de_estrutura_de_rotas.md)
