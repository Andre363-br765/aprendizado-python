# Aula 18.5 – Versionamento e Boas Práticas Avançadas

## 1️⃣ Versionamento de APIs
Permite que a API evolua sem quebrar clientes existentes.

- Exemplo:
    - `/v1/users` → primeira versão
    - `/v2/users` → segunda versão com melhorias
- Recomenda-se incluir a versão na URL ou nos headers.

---

## 2️⃣ Paginação e Filtros
- Evita retorno de muitos dados de uma só vez
- Exemplo:
    - `/products?limit=10&page=2`
    - `/orders?status=paid&sort=date`

---

## 3️⃣ Autenticação e Segurança
- Use tokens (JWT) ou OAuth2
- Sempre valide permissões para cada recurso

---

## 4️⃣ Mensagens de Erro Padronizadas
- Use sempre códigos HTTP corretos:
    - 200 → sucesso
    - 201 → recurso criado
    - 400 → requisição inválida
    - 401 → não autorizado
    - 404 → recurso não encontrado
    - 500 → erro no servidor
- Inclua mensagens JSON claras:
```json
{
  "error": "Usuário não encontrado",
  "code": 404
}
```

> Referência: [Boas Práticas para APIs RESTful](https://aline-antunes.gitbook.io/boas-praticas-para-apis-restful)

---

✍️ **Próxima aula:** [18.6 – Resumo Final](18_6_resumo_final.md)