# 22_5_6 - Adicionando script de inicialização no Render

- Render e outros serviços permitem rodar **scripts no deploy**.
- Exemplo para criar tabelas iniciais:
```bash
#!/bin/bash
# script_init.sh
export DATABASE_URL="postgres://usuario:senha@host:port/db"
python criar_tabelas.py
```

---

✅ **Resumo 22_5**
- Trate erros de forma clara com `HTTPException`.
- Documentação automática com `/docs` e `/redoc`.
- Configure CORS para front-ends externos.
- Use **Pydantic Settings** para centralizar configurações.
- Use **Alembic** para migrations do banco.
- Scripts de inicialização automatizam setup no deploy.

---

✍️ **Próxima aula:** [26 – Próximo Tópico](../../7_aumentando_a_produtividade_com_ia_e_Versionamento%20de_Codigo/7_aumentando_a_produtividade_com_ia_e_Versionamento%20de_Codigo.md)