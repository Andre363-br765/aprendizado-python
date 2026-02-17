# Aula 19 – FastAPI: Resumo

## 1️⃣ Introdução
- FastAPI é um framework moderno para criar APIs RESTful assíncronas em Python.
- Permite alta performance, validação automática e documentação interativa.

## 2️⃣ Benefícios
- Rápido e eficiente.
- Suporte nativo a async/await.
- Validação automática de dados com Pydantic.
- Geração automática de documentação Swagger e Redoc.

## 3️⃣ Estrutura básica de uma aplicação FastAPI
- Estrutura mínima:

```text
my_fastapi_app/
├── main.py <- ponto de entrada da aplicação
├── requirements.txt <- dependências
└── venv/ <- ambiente virtual
```

- Modularização recomendada:
```text
app/
├── main.py <- instancia FastAPI e configura rotas
├── routers/ <- rotas separadas por recurso (usuarios.py, pedidos.py)
├── models.py <- modelos Pydantic
└── database.py <- configuração de banco de dados
```

## 4️⃣ Rotas e Endpoints
- **Path Parameters**: obrigatórios, vêm da URL.
- **Query Parameters**: opcionais, usados para filtros e paginação.
- **Request Body**: usado para criar ou atualizar recursos.
- **Cookies e Headers**: acesso a informações de sessão, autenticação ou controle de estado.
- **APIRouter**: organiza rotas por módulos para manter o código limpo e escalável.

## 5️⃣ Ciclo básico de uma requisição
1. Cliente faz requisição HTTP (GET, POST, PUT, DELETE, etc.).
2. FastAPI recebe e valida os dados.
3. Processa lógica ou acessa banco de dados.
4. Retorna resposta em JSON.

## 6️⃣ Dicas finais
- Sempre definir tipos nos parâmetros (int, str, Optional).
- Aproveitar a documentação automática (`/docs` e `/redoc`).
- Modularizar a aplicação com APIRouter para projetos maiores.

✍️ **Próxima aula:** [20 – Próximo Tópico](../../5_sIntegrando_python_com_banco_de_dados_relacionais/20_introdução_banco_de_dados/20_1_introducao.md)