# 22_1_2 - Modelos de Dados em FastAPI

Para validação e serialização de dados, usamos **Pydantic**.

## Exemplo de modelo de dados
```python
from pydantic import BaseModel

class Aluno(BaseModel):
    id: int | None = None
    nome: str
    idade: int
    curso: str
```

## Uso em rotas

- **Request body:** valida entrada de dados
- **Response model:** padroniza saída da API

```py
@app.post("/alunos", response_model=Aluno)
async def criar_aluno(aluno: Aluno):
    return aluno
```

---

✍️ **Próxima aula:** [22 – Próximo Tópico](3_CRUD_Assincrono.md)