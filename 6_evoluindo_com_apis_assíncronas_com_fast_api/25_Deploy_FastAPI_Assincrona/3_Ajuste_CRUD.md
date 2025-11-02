# 25_3 - Ajustando Problemas com o CRUD

Após mover a API para o servidor:

1. **Verifique rotas assíncronas**
   - Certifique-se de que todas as funções `async def` usam `await` corretamente.
2. **Banco remoto**
   - Ajuste queries e conexões para trabalhar com banco assíncrono em produção.
3. **Testes**
   - Rode testes do CRUD e da autenticação no servidor remoto.
4. **Logs e erros**
   - Ative `logging` para monitorar requests e possíveis problemas.

✅ Resumo

- Criar repositório remoto e enviar todo o código.
- Configurar servidor web (Render, Heroku, AWS).
- Conectar corretamente o banco assíncrono remoto.
- Ajustar rotas e queries para funcionar em produção.
- Testar CRUD e autenticação no ambiente deployado.

---

✍️ **Próxima aula:** [26 – Próximo Tópico](../26_Boas_Praticas_APIs/1_Tratamento_de_Erros.md)