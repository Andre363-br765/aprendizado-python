## 27_4 - Técnicas de Engenharia de Prompt

Essas técnicas ajudam a obter respostas **mais inteligentes e contextualizadas** do Copilot e outras IAs.

### 🧠 1. Prompt Contextual

Inclua partes do código, docstrings ou comentários:
```py
# Classe responsável por gerenciar usuários no sistema
# Adicione um método para verificar se o usuário está ativo
```

### ⚙️ 2. Prompt Iterativo

Aperfeiçoe a resposta com base no resultado anterior.

- Se a sugestão não ficou boa, complemente:
```sql
# Agora adicione verificação de senha e retorne True ou False
```

### 🧩 3. Chain of Thought (encadeamento lógico)

Descreva passo a passo o que deve ser feito:

```python
# 1. Ler um arquivo CSV
# 2. Filtrar apenas as linhas com idade > 18
# 3. Salvar em um novo arquivo CSV
```

### 🧮 4. Role Prompting (definindo o papel)

Diga à IA o que ela é antes de pedir algo:
```py
# Você é um desenvolvedor Python especializado em APIs REST.
# Crie uma rota FastAPI que cadastre um novo produto.
```

### 📚 5. Few-shot prompting

Forneça exemplos:

```py
# Exemplo 1: saudação("Ana") → "Olá, Ana!"
# Exemplo 2: saudação("Lucas") → "Olá, Lucas!"
# Agora implemente a função saudação(nome)
```

### ✅ Conclusão
Nesta aula aprendemos:
- O que é o `GitHub Copilot` e como ele auxilia no desenvolvimento.
- Como `instalar, configurar e usar` o Copilot no VS Code.
- Fundamentos de ``Prompt Engineering`` para melhorar as sugestões.
- `Técnicas avançadas de prompts` para criar código mais inteligente e produtivo.

✍️ **Próxima aula:** [27_5 - Boas Práticas no Uso de IA e GitHub](5_Boas_Praticas_no_Uso_de_IA_e_GitHub.md)