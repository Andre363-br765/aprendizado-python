# 27_5 - Boas Práticas no Uso de IA e Git/GitHub

Nesta seção, aprendemos como manter um **fluxo de trabalho profissional** ao usar **IA e versionamento de código** em conjunto.

---

## 🧠 1. Boas Práticas com IA (GitHub Copilot e outras)

### ✅ Faça:
- **Revise sempre o código gerado** antes de aceitar.
- Use o Copilot para **tarefas repetitivas**, como funções auxiliares e estruturas CRUD.
- Combine **seu raciocínio lógico** com a IA — use-a como *assistente*, não substituto.
- Adicione **comentários claros** para orientar a IA com precisão.
- Treine prompts progressivos: comece simples e vá detalhando.

### ⚠️ Evite:
- Aceitar sugestões sem entender o que fazem.
- Usar código sensível (senhas, tokens) em prompts.
- Depender 100% das respostas da IA — revise segurança, performance e legibilidade.

---

## 💾 2. Boas Práticas com Git e GitHub

### 2.1. Versionamento organizado
- Crie commits **frequentes e pequenos**:
```git
git commit -m "fix: corrigindo validação de email no cadastro"
```

- Use convenções de commits:
- `feat:` → nova funcionalidade  
- `fix:` → correção de bug  
- `refactor:` → melhoria sem mudar comportamento  
- `docs:` → atualização de documentação  
- `test:` → adição ou ajuste de testes  

#### 2.2. Uso de branches
Mantenha uma estrutura limpa:

- main → versão estável
- dev → desenvolvimento ativo
- feature/* → novas funcionalidades
- fix/* → correções específicas

Exemplo:
```git
git checkout -b feature/autenticacao-jwt
```


#### 2.3. Evite subir arquivos sensíveis
Crie e mantenha o arquivo `.gitignore`:
Exemplo de .gitignore
```gitignore
.env
pycache/
*.log
*.sqlite3
node_modules/
```

#### 2.4. Proteja o repositório
- Use **repositórios privados** para projetos internos.
- Ative **autenticação de dois fatores (2FA)** no GitHub.
- Revogue tokens e chaves antigas.

---

## ⚙️ 3. Integração entre IA e Git

### Workflow recomendado:
1. Gere o código com o Copilot.
2. Teste e revise.
3. Faça commit somente após validar.
4. Descreva o que a IA ajudou a criar:
```git
git commit -m "feat: adicionado endpoint CRUD gerado parcialmente via Copilot"
```

---

5. Use *pull requests* para revisão colaborativa.

---

## 🧩 4. Dicas para Equipes

- Defina **regras de uso da IA** dentro da equipe.
- Documente quando e como o Copilot foi usado.
- Evite dependência excessiva de sugestões automáticas — revise coletivamente.
- Use **issues e pull requests** para discutir código gerado pela IA.

---

## 🔐 5. Segurança e Privacidade

- Nunca envie **dados sigilosos** em prompts.
- Cuidado com **códigos de terceiros** que o Copilot pode sugerir.
- Prefira sempre criar **lógicas próprias** para áreas sensíveis (autenticação, criptografia, banco de dados).

---

## 💡 6. Produtividade e Manutenção

- Use o Copilot para **documentar código** rapidamente:
```python
# Crie uma docstring para esta função em formato Google
```

- NAutomatize tarefas com Git Hooks (ex: testes antes de cada commit).
- Mantenha a IA como ferramenta de apoio, não como fonte única de decisão técnica.

✅ Resumo da Aula 27.5

- Use IA como aliada, não substituta.
- Faça versionamento limpo e organizado.
- Proteja informações sensíveis com `.gitignore`.
- Valide e documente tudo o que a IA gerar.
- Mantenha segurança, clareza e rastreabilidade em todo o ciclo de desenvolvimento.

