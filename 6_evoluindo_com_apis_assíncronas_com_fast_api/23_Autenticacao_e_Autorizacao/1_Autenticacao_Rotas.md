# 23_1 - Como iremos autenticar as nossas rotas

FastAPI permite proteger rotas usando **dependências** e **security schemes**.

## Importando dependências
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
```

## Criando esquema de autenticação
```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

- `tokenUrl` é a rota que gera tokens (login).
- Dependência que valida o token em rotas protegidas:

```python
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Aqui validamos o token
    if token != "SECRET_TOKEN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )
    return {"username": "usuario_exemplo"}
```

---

## Protegendo uma rota
```python
@app.get("/alunos/me")
async def ler_meus_dados(current_user: dict = Depends(get_current_user)):
    return {"usuario": current_user}
```

- Rotas que usam `Depends(get_current_user)` exigem autenticação.

---

✍️ **Próxima aula:** [23 – Próximo Tópico](2_Tokens.md)