# 22_5_3 - Resolvendo o problema de CORS

CORS (Cross-Origin Resource Sharing) impede requisições externas sem permissão.

## Exemplo de configuração
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou lista de domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

- Permite que front-ends externos consumam sua API sem erros de CORS.

---

✍️ **Próxima aula:** [26 – Próximo Tópico](4_Pydantic_Settings.md)