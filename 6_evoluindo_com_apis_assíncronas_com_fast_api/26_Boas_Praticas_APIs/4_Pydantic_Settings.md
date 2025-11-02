# 26_4 - Adicionando Pydantic-Settings

- Facilita organizar **configurações e variáveis de ambiente**.
- Exemplo:
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
```

- Agora `settings.DATABASE_URL` e `settings.SECRET_KEY` podem ser usados em todo o projeto.

---

✍️ **Próxima aula:** [26 – Próximo Tópico](5_Alembic.md)