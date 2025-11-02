# Aula 0: Terminal e Comandos Básicos

> Guia rápido de comandos essenciais de **Python**, **Git** e **Terminal**.

## 1️⃣ Executar arquivos Python
- [Python](http://www.python.org)
- [instalação ](https://python.org.br/instalacao-windows)

### No terminal:
```bash
python nome_do_arquivo.py
python aula1_Python_basico.py
```

#### 💡 Dica: Em alguns sistemas, usar python3

---

## 2️⃣ Ver e navegar entre pastas 📂

| Sistema      | Comando     | Descrição                 |
|-------------|------------|---------------------------|
| Windows     | `dir`      | Lista arquivos e pastas    |
|             | `cd nome`  | Entra na pasta 'nome'      |
|             | `cd ..`    | Volta uma pasta            |
| Linux/macOS | `ls`       | Lista arquivos e pastas    |
|             | `cd nome`  | Entra na pasta 'nome'      |
|             | `cd ..`    | Volta uma pasta            |

#### 💡 Dica: No Linux/macOS, `ls -l` mostra detalhes e `ls -a` arquivos ocultos.

---

## 3️⃣ Limpar a tela 🧹

| Sistema      | Comando |
|-------------|---------|
| Windows     | `cls`   |
| Linux/macOS | `clear` |

---

## 4️⃣ Git Básico ⚡

**Clonar repositório:**
```bash
git clone https://github.com/usuario/repositorio.git
```

### Ver status dos arquivos
```bash
git status
```

### Adicionar arquivos para commit
```bash
git add .
```

### Salvar alterações (commit)
```bash
git commit -m "mensagem"
```
#### 💡 Dica: Use mensagens claras no commit, ex: "Adiciona exercícios da aula 0"

### Enviar para o GitHub (push)
```bash
git push
```

### Comandos extras:
- Histórico de commits
 ```bash
 git log
 ```
- Alterações não commitadas
 ```bash
 git diff
 ```
- Lista branches
 ```bash
 git branch
 ```
- Troca de branch
 ```bash
 git checkout nome
 ```
- Mescla branch
 ```bash
 git merge nome
 ```
 #### 💡 Dicas Git:
 - Sempre cheque `git status` antes de dar push.
 - Use commits curtos e descritivos.
 
---

## 5️⃣ Python e Bibliotecas 📦

### Instalar pacote
```bash
pip install nome_do_pacote
```

### Listar pacotes instalados
```bash
pip list
```

### Comandos extras
- Detalhes do pacote
```bash
pip show nome_do_pacote
```
- Remove pacote
```bash
pip uninstall nome_do_pacote
```
---

## 6️⃣ Terminal Extras 💻

### Sair do terminal
```bash
exit
```

### Comandos adicionais

- Diretório atual (Linux/macOS)
```bash
pwd
```
- Usuário atual
```bash
whoami
```
#### 💡 Lembre-se: praticar esses comandos todos os dias ajuda a memorizar e evitar erros comuns.

---

## 🔗 Recursos Extras

### Python 🐍
- [Documentação oficial Python](https://www.python.org/doc/)
               
### Git ⚡
- [Documentação oficial Git](https://git-scm.com/docs)

### Terminal 💻
- [Guia de comandos Linux](https://linuxcommand.org/lc3_learning_the_shell.php)
- [Cheatsheet Terminal básico](https://ss64.com/bash/)

---

✍️ **Próxima aula:** [1 – Próximo Tópico](../1_primeiros_passos_em_python/aula_1_conhecendo_a_linguagem/1_1_tipos_de_dados_basicos.md)