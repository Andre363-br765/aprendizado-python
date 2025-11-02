# 23_2 - Uso de Tokens para Autenticação

- Para APIs RESTful modernas, usamos **JWT (JSON Web Tokens)**.
- JWT é **stateless**: não precisa salvar sessão no servidor.

## Criando e verificando JWT
```python
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "SUA_CHAVE_SECRETA"
ALGORITHM = "HS256"

# Criar token
def criar_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verificar token
def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario = payload.get("sub")
        if usuario is None:
            raise ValueError("Token inválido")
        return usuario
    except JWTError:
        raise ValueError("Token inválido ou expirado")
```

## Exemplo de rota de login
```python
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/token")
async def login(username: str, password: str):
    # Aqui você valida usuário e senha
    if username == "admin" and password == "1234":
        token = criar_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
```

## Protegendo rotas com JWT
```python
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        usuario = verificar_token(token)
        return {"username": usuario}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )
```

- Rotas protegidas continuam usando:
```python
@app.get("/alunos/me")
async def ler_meus_dados(current_user: dict = Depends(get_current_user)):
    return {"usuario": current_user}
```

## ✅ Resumo

- `OAuth2PasswordBearer` cria dependência de token.
- JWT permite autenticação sem estado (stateless).
- Protege rotas com `Depends(get_current_user)`.
- Tokens podem ter expiração configurável e são validados em cada requisição.

---

✍️ **Próxima aula:** [24 – Próximo Tópico](../24_Testando_APIs/1_Testando_APIs.md)