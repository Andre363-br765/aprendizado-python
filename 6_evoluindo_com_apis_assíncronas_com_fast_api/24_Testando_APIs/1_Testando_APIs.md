# 23_1 - Testando APIs RESTful Assíncronas em FastAPI

Testar APIs assíncronas é fundamental para garantir que rotas CRUD, autenticação e lógica de negócios funcionem corretamente.

---

## Bibliotecas recomendadas
- `pytest` → framework de testes.
- `httpx` → cliente HTTP assíncrono para simular requisições.
- `pytest-asyncio` → permite usar `async def` nos testes.

---

## Estrutura básica do teste

```python
import pytest
from httpx import AsyncClient
from main import app  # seu FastAPI app

@pytest.mark.asyncio
async def test_listar_alunos():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/alunos")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
```

---

## Testando CRUD

### Criar aluno (POST)
```python
@pytest.mark.asyncio
async def test_criar_aluno():
    aluno_data = {"nome": "Teste", "idade": 20, "curso": "Python"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/alunos", json=aluno_data)
        assert response.status_code == 200
        assert response.json()["nome"] == "Teste"
```

### Atualizar aluno (PUT)
```python
@pytest.mark.asyncio
async def test_atualizar_aluno():
    aluno_data = {"nome": "Teste Atualizado", "idade": 21, "curso": "Python"}
    aluno_id = 1
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put(f"/alunos/{aluno_id}", json=aluno_data)
        assert response.status_code == 200
        assert response.json()["nome"] == "Teste Atualizado"
```

### Deletar aluno (DELETE)
```python
@pytest.mark.asyncio
async def test_deletar_aluno():
    aluno_id = 1
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete(f"/alunos/{aluno_id}")
        assert response.status_code == 200
        assert response.json()["status"] == "removido"
```


### Testando autenticação com JWT
```python
@pytest.mark.asyncio
async def test_login_e_acesso_protegido():
    login_data = {"username": "admin", "password": "1234"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # login
        token_response = await ac.post("/token", data=login_data)
        assert token_response.status_code == 200
        token = token_response.json()["access_token"]

        # acessar rota protegida
        headers = {"Authorization": f"Bearer {token}"}
        response = await ac.get("/alunos/me", headers=headers)
        assert response.status_code == 200
        assert response.json()["usuario"]["username"] == "admin"
```

## ✅ Resumo

- Use `pytest` e `httpx` para testar APIs assíncronas.
- Cada teste pode criar, atualizar, deletar ou ler dados do banco.
- Teste autenticação separadamente para validar tokens JWT.
- Rotas assíncronas devem ser testadas usando `AsyncClient` e `async def`.

---

✍️ **Próxima aula:** [25 – Próximo Tópico](../25_Deploy_FastAPI_Assincrona/1_Repositorio_e_Servidor.md)