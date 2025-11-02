# Aula 18.4 – Exemplo Prático com Flask-RESTful

Aqui temos um exemplo simples de como criar uma API RESTful usando Flask e Flask-RESTful em Python.

```python
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Banco de dados simulado
usuarios = []

# Recurso Usuário
class Usuario(Resource):
    def get(self, user_id=None):
        if user_id is None:
            return usuarios, 200
        for u in usuarios:
            if u['id'] == user_id:
                return u, 200
        return {"mensagem": "Usuário não encontrado"}, 404

    def post(self):
        novo_usuario = request.get_json()
        usuarios.append(novo_usuario)
        return novo_usuario, 201

    def put(self, user_id):
        dados = request.get_json()
        for i, u in enumerate(usuarios):
            if u['id'] == user_id:
                usuarios[i] = dados
                return dados, 200
        return {"mensagem": "Usuário não encontrado"}, 404

    def delete(self, user_id):
        for i, u in enumerate(usuarios):
            if u['id'] == user_id:
                del usuarios[i]
                return {"mensagem": "Usuário deletado"}, 200
        return {"mensagem": "Usuário não encontrado"}, 404

# Rotas
api.add_resource(Usuario, '/users', '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
```

✅ Demonstra:

- `GET /users` → listar usuários
- `GET /users/1` → obter usuário específico
- `POST /users` → criar novo usuário
- `PUT /users/1` → atualizar usuário
- `DELETE /users/1` → deletar usuário

> Referência: [Flask-RESTful Docs](https://flask-restful.readthedocs.io/en/latest/)

---

✍️ **Próxima aula:** [18.5 – Versionamento e Boas Práticas Avançadas](18_5_versionamento_e_boas_praticas_avancadas.md)
