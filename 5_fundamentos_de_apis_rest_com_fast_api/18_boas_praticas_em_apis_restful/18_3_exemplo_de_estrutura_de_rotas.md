# Aula 18.3 – Exemplo de Estrutura de Rotas RESTful

### Recursos de Usuários

| Método | Rota             | Descrição                     |
|--------|-----------------|-------------------------------|
| GET    | /users           | Lista todos os usuários       |
| POST   | /users           | Cria um novo usuário          |
| GET    | /users/{userId}  | Detalhes de um usuário        |
| PUT    | /users/{userId}  | Atualiza um usuário           |
| DELETE | /users/{userId}  | Remove um usuário             |

### Recursos de Pedidos (aninhados com Usuários)

| Método | Rota                          | Descrição                         |
|--------|-------------------------------|-----------------------------------|
| GET    | /users/{userId}/orders        | Lista pedidos de um usuário       |
| POST   | /users/{userId}/orders        | Cria um novo pedido para usuário  |

> Referência: [Exemplo Completo](https://aline-antunes.gitbook.io/boas-praticas-para-apis-restful/boas-praticas-para-apis-restful/exemplo-completo-de-estrutura-de-rotas-restful)


---

✍️ **Próxima aula:** [18.4 – Exemplo Prático com Flask-RESTful](18_4_exemplo_pratico_flask_restful.md)
