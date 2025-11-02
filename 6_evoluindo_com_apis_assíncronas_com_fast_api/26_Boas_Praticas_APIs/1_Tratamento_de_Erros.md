# 26_1 - Tratamento de Erros

FastAPI permite tratar erros de forma clara, retornando status HTTP e mensagens amigáveis.

## Exemplo de exceção personalizada
```python
from fastapi import HTTPException, status

@app.get("/alunos/{aluno_id}")
async def obter_aluno(aluno_id: int):
    aluno = await database.fetch_one("SELECT * FROM alunos WHERE id = :id", values={"id": aluno_id})
    if not aluno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aluno {aluno_id} não encontrado"
        )
    return aluno
```

- Use `HTTPException` para erros HTTP.
- Retorne mensagens claras para o usuário e logs para o desenvolvedor.

---

✍️ **Próxima aula:** [26 – Próximo Tópico](2_Documentacao_Automatica.md)