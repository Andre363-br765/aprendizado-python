# 25_2 - Criando o Banco de Dados

- Configure o banco de dados remoto (PostgreSQL, MySQL, etc.).
- Ajuste a conexão assíncrona:
```python
import os
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")
database = Database(DATABASE_URL)
```

## Rodar migrations ou criar tabelas iniciais:
```python
from models import Base
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(DATABASE_URL)
async def criar_tabelas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
```

## Garantir que a API conecte corretamente no startup e shutdown:
```python
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
```

---

✍️ **Próxima aula:** [25 – Próximo Tópico](3_Ajuste_CRUD.md)