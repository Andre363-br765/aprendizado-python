# Testando APIs RESTful em Flask

Garantir a qualidade de uma API RESTful é essencial, e para isso utilizamos **testes automatizados**.  
Neste capítulo, vamos explorar como testar APIs construídas com Flask usando **pytest**, incluindo testes unitários, testes de integração e o uso do `FlaskClient`.

---

## 🧪 Por que testar uma API?

Testes garantem que:

- As rotas funcionam como esperado  
- Os dados retornados estão corretos  
- Regressões são evitadas  
- Erros são detectados cedo  
- A API permanece confiável conforme evolui  

Existem dois tipos principais de testes:

---

## 🔹 Testes Unitários

Focam em **unidades pequenas** do código:
- Funções  
- Métodos  
- Serviços isolados  

Eles são rápidos e ajudam a detectar erros logo no início.

---

## 🔸 Testes de Integração

Testam como **componentes interagem entre si**, por exemplo:

- Rota + banco de dados  
- Rota + autenticação  
- Rota + serviços internos  

São essenciais para garantir que a API funciona como um todo.

---

## ⚙️ Configurando o Pytest

Instale o pytest:

```bash
pip install pytest
````

Crie uma estrutura básica de testes:

```
meu_projeto/
│
├── app.py
└── tests/
    └── test_rotas.py
```

---

## 🧰 Usando o FlaskClient para testar rotas

O Flask possui uma ferramenta integrada para testes, chamada **FlaskClient**, que simula requisições HTTP.

### Exemplo de configuração do app para testes

No `app.py`:

```python
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return {"mensagem": "Olá, Flask!"}

    return app
```

---

## 🧪 Primeiro teste com pytest

Crie o arquivo `tests/test_rotas.py`:

```python
from app import create_app

def test_hello():
    app = create_app()
    cliente = app.test_client()

    resposta = cliente.get("/hello")

    assert resposta.status_code == 200
    assert resposta.get_json() == {"mensagem": "Olá, Flask!"}
```

Execute os testes:

```bash
pytest
```

---

## 📤 Testando rotas POST (enviando JSON)

```python
def test_post_usuario():
    app = create_app()
    cliente = app.test_client()

    usuario = {"nome": "Ana"}

    resposta = cliente.post(
        "/usuarios",
        json=usuario
    )

    assert resposta.status_code == 201
    assert resposta.get_json()["mensagem"] == "Usuário criado"
```

---

## 🔐 Testando Rotas Protegidas com JWT

Se sua API usa JWT (com flask-jwt-extended), é possível testar rotas protegidas.

### Exemplo:

```python
from flask_jwt_extended import create_access_token

def test_rota_protegida():
    app = create_app()
    app.config["JWT_SECRET_KEY"] = "teste"
    cliente = app.test_client()

    with app.app_context():
        token = create_access_token(identity="teste")

    headers = {"Authorization": f"Bearer {token}"}

    resposta = cliente.get("/protegida", headers=headers)

    assert resposta.status_code == 200
```

---

## 🔄 Testando erros e respostas inválidas

Também é importante testar comportamentos inesperados:

```python
def test_usuario_sem_nome():
    app = create_app()
    cliente = app.test_client()

    resposta = cliente.post("/usuarios", json={})

    assert resposta.status_code == 400
    assert "erro" in resposta.get_json()
```

---

## 🧩 Fixtures do pytest

Fixtures ajudam a compartilhar configurações entre testes:

```python
import pytest
from app import create_app

@pytest.fixture
def cliente():
    app = create_app()
    return app.test_client()
```

Usando a fixture:

```python
def test_status(cliente):
    resposta = cliente.get("/status")
    assert resposta.status_code == 200
```

---

## ✔️ Conclusão

Neste capítulo você aprendeu:

* Diferença entre testes unitários e de integração
* Como usar pytest com Flask
* Como testar rotas GET, POST, PUT, DELETE
* Como testar autenticação baseada em JWT
* Como validar erros e respostas
* Como usar fixtures do pytest

Com testes bem escritos, sua API se torna muito mais segura, confiável e fácil de manter conforme o projeto cresce.

```
