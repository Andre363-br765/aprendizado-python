# 19.4 – Retornando dados em JSON e APIRouter

```py
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API FastAPI - JSON e APIRouter")
```
---
## 19.4.1 – Retornando dados em JSON
```py
FastAPI retorna automaticamente dados em JSON. Podemos usar dicionários, listas ou Pydantic Models.

usuarios = [
    {"id": 1, "nome": "Ana", "idade": 25},
    {"id": 2, "nome": "Carlos", "idade": 30},
]

@app.get("/usuarios_json/")
def obter_usuarios():
    # Retornando lista de dicionários → FastAPI converte em JSON
    return usuarios
```

Também podemos retornar Pydantic Models:
```py
class Usuario(BaseModel):
    id: int
    nome: str
    idade: int

@app.get("/usuarios_model/", response_model=List[Usuario])
def listar_usuarios_model():
    return usuarios
```
---
## 19.4.2 – Organizando rotas com APIRouter

APIRouter permite dividir a aplicação em módulos e organizar rotas.

```py
router_usuarios = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router_usuarios.get("/")
def listar_todos_usuarios():
    return usuarios

@router_usuarios.get("/{usuario_id}")
def obter_usuario(usuario_id: int):
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router_usuarios.post("/")
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario.dict())
    return {"mensagem": "Usuário criado com sucesso!", "usuario": usuario}

# Registrando o router na aplicação principal
app.include_router(router_usuarios)
```

---

## Observações sobre FastAPI

- FastAPI converte automaticamente qualquer retorno em **JSON**.
- **APIRouter** ajuda a separar rotas por funcionalidade (ex: usuários, pedidos, produtos).
- **response_model** valida e documenta o retorno da API.
- **HTTPException** permite retornar erros com **status code** apropriado.

---

✍️ **Próxima aula:** [19.5 – Resumo Final da Aula 19](19_5_resumo_final.md)