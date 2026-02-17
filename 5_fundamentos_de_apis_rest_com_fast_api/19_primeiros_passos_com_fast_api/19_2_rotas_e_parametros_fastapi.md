# Aula 19.2 – Aplicação FastAPI

Nesta aula, vamos criar uma aplicação FastAPI completa e entender a estrutura básica de uma API.

---

## 19.2.1 – Criando uma aplicação FastAPI

### Estrutura mínima do projeto:
```text
my_fastapi_app/
├── main.py          <- ponto de entrada da aplicação
├── requirements.txt <- dependências
└── venv/            <- ambiente virtual
```

### Exemplo de código `main.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha Primeira API")

# Rota de teste
@app.get("/")
def home():
    return {"message": "Bem-vindo à minha API FastAPI!"}

# Rota com parâmetro
@app.get("/usuario/{usuario_id}")
def ler_usuario(usuario_id: int):
    return {"usuario_id": usuario_id, "nome": f"Usuário {usuario_id}"}

# Rota POST simples
class Usuario(BaseModel):
    nome: str
    idade: int

@app.post("/usuario/")
def criar_usuario(usuario: Usuario):
    return {"mensagem": "Usuário criado com sucesso!", "usuario": usuario}
```

Para rodar a aplicação:
```bash
uvicorn main:app --reload
```
---
## 19.2.2 – Estrutura básica de uma API FastAPI

### Uma aplicação FastAPI geralmente segue essa estrutura:
```text
my_fastapi_app/
├── app/
│   ├── main.py        <- instancia FastAPI e configura rotas
│   ├── routers/
│   │   ├── usuario.py <- rotas relacionadas a usuários
│   │   └── pedidos.py <- rotas relacionadas a pedidos
│   ├── models.py      <- modelos Pydantic para validação de dados
│   └── database.py    <- configuração de banco de dados
├── requirements.txt
└── venv/
```

### Exemplo de modularização

routers/usuario.py:
```py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/usuario", tags=["Usuário"])

class Usuario(BaseModel):
    nome: str
    idade: int

@router.post("/")
def criar_usuario(usuario: Usuario):
    return {"mensagem": "Usuário criado!", "usuario": usuario}

```

main.py:
```py
from fastapi import FastAPI
from routers import usuario

app = FastAPI(title="API Modularizada")
app.include_router(usuario.router)
```

---

✍️ **Próxima aula:** [19.3 – Rotas e Endpoints](19_3_rotas_e_endpoints.md)