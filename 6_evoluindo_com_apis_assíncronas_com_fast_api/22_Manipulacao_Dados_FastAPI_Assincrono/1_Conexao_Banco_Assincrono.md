# 22_1_1 - Conexão a Banco de Dados Assíncrono

FastAPI permite criar APIs **assíncronas**, usando `async`/`await` para melhorar a performance.

## Bibliotecas comuns
- `Databases` (SQLite, PostgreSQL, MySQL)
- `SQLAlchemy Async` (ORM assíncrono)

## Exemplo com Databases e SQLite
```python
from databases import Database

DATABASE_URL = "sqlite+aiosqlite:///academia.db"
database = Database(DATABASE_URL)

async def connect_db():
    await database.connect()

async def disconnect_db():
    await database.disconnect()
```

---

## Integrando com FastAPI

```py
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup():
    await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()
```

---

✍️ **Próxima aula:** [22 – Próximo Tópico](2_Modelos_de_Dados.md)