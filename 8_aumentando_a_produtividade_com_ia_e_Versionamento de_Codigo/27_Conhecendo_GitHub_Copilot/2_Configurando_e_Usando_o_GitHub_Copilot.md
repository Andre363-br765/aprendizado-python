## 27_2 - Configurando e Usando o GitHub Copilot

### 🪄 Instalação no VS Code:
1. Vá até **Extensões (Ctrl+Shift+X)**.
2. Procure **GitHub Copilot**.
3. Clique em **Instalar**.
4. Faça login com sua conta GitHub.
5. Ative a extensão.

### ⚙️ Configuração:
- Vá em **Configurações → Copilot**.
- Ative:
  - Sugestões automáticas.
  - Painel lateral de sugestões alternativas.

### 💻 Uso básico:
Digite um comentário explicando o que quer:
```python
# Função para calcular a média de uma lista
```

O Copilot sugerirá automaticamente:
```python
def calcular_media(lista):
    return sum(lista) / len(lista)
```

### 📘 Dicas:

Use comentários claros (em português ou inglês).
Escreva passo a passo: o Copilot entende contexto incremental.
Teste sugestões com `Ctrl+Enter` para ver opções alternativas.

---

✍️ **Próxima aula:** [3 - Bases de Prompt Engineering](3_Bases_de_Prompt_Engineering_para_o_GitHub_Copilot.md)