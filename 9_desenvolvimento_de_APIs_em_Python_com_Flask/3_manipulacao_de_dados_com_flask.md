Aqui está o arquivo **`3_manipulacao_de_dados_com_flask.md`**, organizado, claro e pronto para fazer parte da sua série de estudos.

---

````md
# Manipulação de Dados com Flask

Neste capítulo, você aprenderá como o Flask lida com **dados enviados e recebidos** em uma API RESTful.  
Vamos explorar requisições HTTP, métodos, envio de JSON, leitura de dados do cliente e boas práticas para trabalhar com dados em APIs.

---

## 📥 Métodos HTTP e Suas Finalidades

Uma API REST geralmente utiliza os seguintes métodos HTTP:

| Método | Função | Exemplo |
|-------|--------|---------|
| **GET** | Buscar dados | Listar usuários |
| **POST** | Criar dados | Criar um novo usuário |
| **PUT** | Atualizar dados (completo) | Atualizar todas as infos de um usuário |
| **PATCH** | Atualizar dados (parcial) | Atualizar só o email de um usuário |
| **DELETE** | Remover dados | Deletar um usuário |

---

## 📤 Enviando e Recebendo JSON no Flask

Para APIs modernas, o formato mais utilizado é **JSON**.

### Acessando JSON enviado pelo cliente
```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/usuario", methods=["POST"])
def criar_usuario():
    dados = request.get_json()
    return {"mensagem": "Usuário criado", "dados_recebidos": dados}, 201
````

### Retornando JSON para o cliente

```python
@app.route("/status")
def status():
    return {"status": "API funcionando!"}
```

O Flask converte automaticamente dicionários Python em JSON.

---

## 🗃️ Manipulando Dados em Memória (exemplo)

Antes de integrar um banco de dados, é comum armazenar os dados em memória para testar a API.

```python
usuarios = []

@app.route("/usuarios", methods=["POST"])
def add_usuario():
    dados = request.get_json()
    usuarios.append(dados)
    return {"mensagem": "Usuário adicionado"}, 201

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return {"usuarios": usuarios}
```

---

## 🔄 Manipulação de Dados (CRUD)

CRUD significa:
**Create, Read, Update, Delete**
São as quatro operações básicas de uma API.

### Criar (POST)

```python
@app.route("/item", methods=["POST"])
def criar_item():
    dados = request.get_json()
    return {"item": dados}, 201
```

### Ler (GET)

```python
@app.route("/item/<int:id>", methods=["GET"])
def obter_item(id):
    return {"id": id}
```

### Atualizar (PUT ou PATCH)

```python
@app.route("/item/<int:id>", methods=["PUT"])
def atualizar_item(id):
    dados = request.get_json()
    return {"mensagem": "Item atualizado", "dados": dados}
```

### Deletar (DELETE)

```python
@app.route("/item/<int:id>", methods=["DELETE"])
def deletar_item(id):
    return {"mensagem": f"Item {id} deletado"}
```

---

## ⚠️ Validação de Dados

Antes de aceitar dados enviados pelo cliente, sempre valide!

### Exemplo simples:

```python
@app.route("/produto", methods=["POST"])
def criar_produto():
    dados = request.get_json()

    if "nome" not in dados:
        return {"erro": "Campo 'nome' é obrigatório"}, 400

    return {"mensagem": "Produto criado com sucesso"}
```

---

## 📌 Boas Práticas ao Manipular Dados

* Nunca confie nos dados enviados pelo cliente
* Sempre valide e trate erros
* Utilize códigos HTTP adequados (200, 201, 400, 404, 500…)
* Evite repetição de código
* Organize rotas e funções conforme o projeto cresce
* Retorne JSON consistente em todas as rotas

---

## ✔️ Conclusão

Neste capítulo você aprendeu:

* Como lidar com dados enviados via JSON
* Como retornar dados no formato JSON
* Estrutura de rotas CRUD
* Validação básica
* Boas práticas de manipulação de dados

Com isso, você já tem a base para construir APIs de verdade antes mesmo de integrar um banco de dados.

```