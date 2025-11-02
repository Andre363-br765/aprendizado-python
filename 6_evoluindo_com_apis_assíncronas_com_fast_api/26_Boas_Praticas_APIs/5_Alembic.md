# 26_5 - Configurando Alembic

Alembic permite controlar **migrations** do banco de dados.

## Passos básicos:
1. Inicializar Alembic:

## alembic init alembic

2. Configurar `alembic.ini` e `env.py` com a URL do banco.
3. Criar migrations:

## alembic revision --autogenerate -m "Criar tabela alunos"

4. Aplicar migrations:

## alembic upgrade head

- Garante que estrutura do banco seja consistente em diferentes ambientes.

---

✍️ **Próxima aula:** [26 – Próximo Tópico](6_Script_Inicializacao_Render.md)