# Aula 19.1 – Introdução ao FastAPI

FastAPI é um framework moderno para criar APIs RESTful rápidas e assíncronas em Python.  
Ele se destaca por:
- Ser rápido (baseado no Starlette e Pydantic)
- Suporte nativo a Python async/await
- Geração automática de documentação interativa (Swagger UI / ReDoc)
- Validação de dados automática com Pydantic

---

## 19.1.1 – Benefícios e Limitações do FastAPI

**Benefícios:**
- ✅ Muito rápido e performático
- ✅ Suporte completo a APIs assíncronas
- ✅ Fácil de criar e manter APIs RESTful
- ✅ Documentação automática
- ✅ Validação de dados robusta com Pydantic

**Limitações:**
- ⚠️ Pode ser mais complexo para quem nunca usou async/await
- ⚠️ Ecosistema menor que frameworks mais maduros (Django, Flask)
- ⚠️ Requer cuidado com dependências e versionamento de Python

---

## 19.1.2 – Configuração do Ambiente de Desenvolvimento

1️⃣ **Criar um ambiente virtual (recomendado)**  
Linux / Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

2️⃣ **Instalar FastAPI e servidor ASGI (Uvicorn)**

```bash
pip install fastapi uvicorn
```

3️⃣ **Estrutura inicial do projeto**

```text
my_fastapi_project/
├── main.py          <- arquivo principal da API
├── requirements.txt <- dependências
└── venv/            <- ambiente virtual
```

### Exemplo mínimo de FastAPI
```py
from fastapi import FastAPI

app = FastAPI()  # instanciando a aplicação

@app.get("/")
def read_root():
    return {"message": "Olá, FastAPI!"}
```

Para rodar a aplicação:
```bash
uvicorn main:app --reload
```

Depois acessar:

- Aplicação: http://127.0.0.1:8000
- Documentação interativa: http://127.0.0.1:8000/docs

---

✍️ **Próxima aula:** [19.2 – Aplicação FastAPI](19_2_rotas_e_parametros_fastapi.md)