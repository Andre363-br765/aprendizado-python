# 25_1 - Criando o Repositório e o Servidor Web

Para colocar sua API no ar, você precisa de:

1. **Repositório remoto**
   - GitHub, GitLab ou outro.
   - Suba seu código (`git push`) incluindo:
     - `main.py`
     - `routes/`
     - `models.py`
     - `database.py`
     - `requirements.txt`

2. **Servidor web**
   - Render, Heroku, AWS ou outro.
   - Criar novo serviço para **FastAPI** (Python 3.10+ recomendado).
   - Configurar variáveis de ambiente:
     - `DATABASE_URL`
     - `SECRET_KEY` (para JWT)

---

✍️ **Próxima aula:** [25 – Próximo Tópico](2_Banco_de_Dados.md)