# 22_1_3 - Operações CRUD Assíncronas em APIs RESTful

## Criar (POST)
```python
@app.post("/alunos")
async def criar_aluno(aluno: Aluno):
    query = "INSERT INTO alunos (nome, idade, curso) VALUES (:nome, :idade, :curso)"
    aluno_id = await database.execute(query, values=aluno.dict())
    return {"id": aluno_id, **aluno.dict()}
```

## Ler (GET)

```py
@app.get("/alunos")
async def listar_alunos():
    query = "SELECT * FROM alunos"
    return await database.fetch_all(query)
```

## Atualizar (PUT)

```py
@app.put("/alunos/{aluno_id}")
async def atualizar_aluno(aluno_id: int, aluno: Aluno):
    query = """
    UPDATE alunos SET nome=:nome, idade=:idade, curso=:curso WHERE id=:id
    """
    await database.execute(query, values={**aluno.dict(), "id": aluno_id})
    return {"id": aluno_id, **aluno.dict()}
```

## Deletar (DELETE)

```py
@app.delete("/alunos/{aluno_id}")
async def remover_aluno(aluno_id: int):
    query = "DELETE FROM alunos WHERE id = :id"
    await database.execute(query, values={"id": aluno_id})
    return {"status": "removido", "id": aluno_id}
```

---

✍️ **Próxima aula:** [22 – Próximo Tópico](4_Implementacao_Final_CRUD.md)