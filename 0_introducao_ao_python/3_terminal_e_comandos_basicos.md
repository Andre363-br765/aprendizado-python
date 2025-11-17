# 💻 Aula 0.3 — Terminal e Comandos Básicos

> Guia rápido com os comandos essenciais de **Terminal**, **Python** e **Git**.
> Ideal para quem está começando a programar e quer dominar o ambiente de desenvolvimento.

---

## 🧭 1. Navegando pelo Terminal

### 🔹 Listar e acessar pastas

| Sistema         | Comando   | Descrição               |
| --------------- | --------- | ----------------------- |
| **Windows**     | `dir`     | Lista arquivos e pastas |
|                 | `cd nome` | Entra na pasta *nome*   |
|                 | `cd ..`   | Volta uma pasta         |
| **Linux/macOS** | `ls`      | Lista arquivos e pastas |
|                 | `cd nome` | Entra na pasta *nome*   |
|                 | `cd ..`   | Volta uma pasta         |

💡 **Dica:**
Use `ls -l` para ver detalhes e `ls -a` para arquivos ocultos.

---

### 🔹 Limpar a tela

| Sistema         | Comando |
| --------------- | ------- |
| **Windows**     | `cls`   |
| **Linux/macOS** | `clear` |

---

### 🔹 Outros comandos úteis

| Ação                    | Comando  | Sistema     |
| ----------------------- | -------- | ----------- |
| Mostrar diretório atual | `pwd`    | Linux/macOS |
| Mostrar usuário atual   | `whoami` | Todos       |
| Sair do terminal        | `exit`   | Todos       |

🧠 *Treine esses comandos todos os dias para ganhar agilidade no terminal!*

---

## 🐍 2. Executando Python pelo Terminal

### 🔹 Executar um arquivo Python

```bash
python nome_do_arquivo.py
```

Exemplo:

```bash
python aula1_python_basico.py
```

💡 Em alguns sistemas, o comando pode ser:

```bash
python3 nome_do_arquivo.py
```

---

### 🔹 Links úteis

* Site oficial: [https://www.python.org](https://www.python.org)
* Instalação no Windows: [https://python.org.br/instalacao-windows](https://python.org.br/instalacao-windows)

---

## 📦 3. Gerenciando Pacotes com `pip`

### 🔹 Instalar pacotes

```bash
pip install nome_do_pacote
```

### 🔹 Ver pacotes instalados

```bash
pip list
```

### 🔹 Outras operações úteis

| Ação                      | Comando                        |
| ------------------------- | ------------------------------ |
| Ver detalhes de um pacote | `pip show nome_do_pacote`      |
| Desinstalar um pacote     | `pip uninstall nome_do_pacote` |

---

## ⚡ 4. Git Básico — Controle de Versão

### 🔹 Clonar um repositório

```bash
git clone https://github.com/usuario/repositorio.git
```

### 🔹 Ver status do repositório

```bash
git status
```

### 🔹 Adicionar arquivos ao commit

```bash
git add .
```

### 🔹 Criar um commit

```bash
git commit -m "mensagem clara e curta"
```

Exemplo:

```bash
git commit -m "Adiciona exercícios da aula 0"
```

### 🔹 Enviar alterações para o GitHub

```bash
git push
```

### 🔹 Comandos adicionais úteis

| Ação                           | Comando             |
| ------------------------------ | ------------------- |
| Ver histórico de commits       | `git log`           |
| Ver diferenças antes do commit | `git diff`          |
| Listar branches                | `git branch`        |
| Trocar de branch               | `git checkout nome` |
| Mesclar branches               | `git merge nome`    |

---

💡 **Boas Práticas Git**

* Sempre confira o repositório com `git status`.
* Faça commits pequenos e descritivos para organizar melhor a evolução do projeto.

---

## 🔗 5. Recursos Recomendados

### 🐍 Python

* Documentação oficial: [https://www.python.org/doc/](https://www.python.org/doc/)

### ⚡ Git

* Documentação Git: [https://git-scm.com/docs](https://git-scm.com/docs)

### 💻 Terminal

* Guia Linux básico: [https://linuxcommand.org/lc3_learning_the_shell.php](https://linuxcommand.org/lc3_learning_the_shell.php)
* Cheatsheet de comandos: [https://ss64.com/bash/](https://ss64.com/bash/)

---

✍️ **Próxima aula:** [0.4 — Primeiro programa em Python](4_primeiro_programa.md)