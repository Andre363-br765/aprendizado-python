# 26_2 - Documentação Automática

FastAPI gera documentação automática em:
- `/docs` → Swagger UI
- `/redoc` → ReDoc

## Exemplo de rota com descrição e resposta
```python
@app.get("/alunos", summary="Lista todos os alunos", response_description="Lista de alunos")
async def listar_alunos():
    """
    Retorna todos os alunos cadastrados no banco.
    """
    return await database.fetch_all("SELECT * FROM alunos")
```

- Use `summary`, `description` e `response_model` para detalhar a API.

---

✍️ **Próxima aula:** [26 – Próximo Tópico](3_CORS.md)