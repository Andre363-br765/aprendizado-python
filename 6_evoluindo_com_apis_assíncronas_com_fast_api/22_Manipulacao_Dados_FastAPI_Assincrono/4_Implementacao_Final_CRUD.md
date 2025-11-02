# 22_1_4 - Implementação Final do CRUD

- Combina **conexão assíncrona**, **modelos Pydantic** e **rotas CRUD**.
- Estrutura recomendada:

```text
app/
├─ main.py # Inicialização FastAPI e eventos
├─ database.py # Conexão assíncrona
├─ models.py # Classes Pydantic
├─ routes/
│ └─ alunos.py # CRUD de alunos
```

### main.py
```python
from fastapi import FastAPI
from routes import alunos

app = FastAPI()
app.include_router(alunos.router)

@app.on_event("startup")
async def startup():
    await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()
```

## Destaques

- Rotas assíncronas permitem múltiplas requisições simultâneas.
- Validação automática com Pydantic reduz erros de dados.
- Estrutura modular facilita manutenção e escalabilidade.

---

✍️ **Próxima aula:** [23 – Próximo Tópico](../23_Autenticacao_e_Autorizacao/1_Autenticacao_Rotas.md)