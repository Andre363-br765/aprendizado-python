# 19.3 – Rotas e Endpoints em FastAPI

```py
from fastapi import FastAPI, Query, Path, Header, Cookie
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API FastAPI - Rotas e Endpoints")

```
---
## 19.3.1 – Path Parameters
Permitem capturar valores diretamente da URL.
```py
@app.get("/usuarios/{usuario_id}")
def obter_usuario(usuario_id: int = Path(..., description="ID do usuário")):
    return {"usuario_id": usuario_id, "nome": f"Usuário {usuario_id}"}
```
---

## 19.3.2 – Query Parameters
Permitem enviar filtros ou informações adicionais na URL, ex: /usuarios?idade=25&cidade=SaoPaulo.

```py
@app.get("/usuarios/")
def listar_usuarios(idade: Optional[int] = Query(None, description="Filtra por idade"),
                    cidade: Optional[str] = Query(None, description="Filtra por cidade")):
    return {"idade_filtrada": idade, "cidade_filtrada": cidade}

```

## 19.3.3 – Request Body
Permite enviar dados mais complexos no corpo da requisição (POST/PUT).

```py
class Usuario(BaseModel):
    nome: str
    idade: int
    cidade: Optional[str] = None

@app.post("/usuarios/")
def criar_usuario(usuario: Usuario):
    return {"mensagem": "Usuário criado com sucesso!", "usuario": usuario}
```

## 19.3.4 – Cookies e Headers
Permite acessar informações enviadas pelo cliente no cabeçalho ou cookies.
```py
@app.get("/cookies_headers/")
def ler_cookies_headers(usuario_id: int, 
                        x_token: Optional[str] = Header(None),
                        session_id: Optional[str] = Cookie(None)):
    return {
        "usuario_id": usuario_id,
        "token_header": x_token,
        "session_cookie": session_id
    }
```

## Observações:

- **Path Parameters**: obrigatórios, vêm diretamente da URL.
- **Query Parameters**: opcionais, usados para filtros ou paginação.
- **Request Body**: útil para criar ou atualizar recursos.
- **Cookies e Headers**: permitem acessar informações de sessão, autenticação ou controle de estado.

---

✍️ **Próxima aula:** [19.4 – JSON e APIRouter](19_4_json_e_routers.md)