# 🌀 Aula 0.5 — Versionamento de Código com Git e GitHub

> Aprenda o que é **versionamento de código**, como funciona o **Git**, para que serve o **GitHub**, e como autenticar seu computador usando **Token** ou **SSH**.

---

## 1️⃣ O que é Versionamento de Código 📜

O versionamento funciona como um **histórico inteligente** do seu projeto.
Cada mudança importante é registrada, permitindo:

* 🕐 **Voltar no tempo** quando algo dá errado
* ✍️ Saber **quem fez cada alteração**
* 🤝 Trabalhar em equipe sem conflitos
* ☁️ Manter **backups** na nuvem

💡 **Analogia:**
É como o “Salvar como” do Word, só que **automático e organizado**, sem criar dezenas de arquivos como:

```
projeto_final_v6_versao_que_agora_vai.py
```

O Git faz tudo isso para você.

---

## 2️⃣ O que é Git ⚙️

O **Git** é a ferramenta que registra versões **no seu computador**.

### 🔧 Conceitos importantes

* **Repositório (repo):** pasta monitorada pelo Git
* **Commit:** um “salvamento” com mensagem explicando a mudança
* **Branch:** linha paralela de desenvolvimento
* **Merge:** união de uma branch com outra
* **.gitignore:** lista do que o Git deve ignorar

💡 **Resumo rápido:**

> **Git = ferramenta local**
> **GitHub = nuvem onde você envia seus repositórios**

---

## 3️⃣ O que é GitHub 🌐

O **GitHub** é uma plataforma para hospedar repositórios Git online.

### No GitHub você pode:

* Criar repositórios remotos
* Fazer backup automático
* Trabalhar com equipe usando **pull requests**
* Criar **issues**, documentações e wikis
* Publicar projetos

💡 **Alternativas:** GitLab, Bitbucket, Gitea.

---

## 4️⃣ Instalando o Git 🧰

1. Acesse:
   👉 [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Baixe para seu sistema (Windows, macOS ou Linux).
3. No Windows, deixe as opções padrão.
4. Verifique a instalação:

```bash
git --version
```

---

## 5️⃣ Autenticação 🔑

Desde 2021, não é mais possível usar **senha** no GitHub via terminal.
Agora você deve escolher entre:

* **Token pessoal (HTTPS)**
* **Chave SSH (recomendado)**

---

# 🔸 Opção 1 — Autenticação via Token (HTTPS)

Método simples e rápido.

### 🧭 Criando o Token

1. Entre em:
   👉 [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. “Generate new token” → “Fine-grained token”
3. Configure:

   * Nome do token
   * Validade
   * Permissões:

     * ✔️ `repo`
     * ✔️ `workflow`
     * ✔️ `delete_repo`
4. Clique **Generate Token**
5. Copie e guarde o token com segurança ⚠️

---

### 🖥️ Usando no terminal

Ao fazer `git push` ou `git pull`:

```bash
Username: seu_usuario
Password: cole_o_token_aqui
```

Para memorizar o token:

```bash
git config --global credential.helper store
```

---

# 🔸 Opção 2 — Autenticação via Chave SSH (Recomendada)

Mais segura e não exige senha nunca mais.

---

## 1️⃣ Criar uma chave SSH

```bash
ssh-keygen -t ed25519 -C "seu_email@exemplo.com"
```

Se não funcionar:

```bash
ssh-keygen -t rsa -b 4096 -C "seu_email@exemplo.com"
```

---

## 2️⃣ Copiar a chave pública

```bash
cat ~/.ssh/id_ed25519.pub
```

(Linux/macOS e Git Bash no Windows)

---

## 3️⃣ Adicionar no GitHub

GitHub → **Settings** → **SSH and GPG Keys** → **New SSH key**

* Title: nome do seu PC
* Key: cole a chave pública

---

## 4️⃣ Testar a conexão

```bash
ssh -T git@github.com
```

Se tudo estiver certo:

```
Hi usuario! You’ve successfully authenticated...
```

🎉 Pronto! Agora você faz push/pull sem senha.

---

## ⚙️ Dica Extra — Usar SSH em um repo que já existe

```bash
git remote set-url origin git@github.com:usuario/repositorio.git
```

---

# ✅ Conclusão

Agora você sabe:

* 🧠 O que é versionamento
* 💾 Como o Git funciona
* ☁️ Como o GitHub hospeda seus projetos
* 🔐 Como autenticar usando **HTTPS (Token)** ou **SSH**

Seu ambiente está pronto para trabalhar de maneira profissional!

---

✍️ **Próxima aula:** [1 — Tipos de Dados Básicos](../1_primeiros_passos_em_python/1_conhecendo_a_linguagem/1_tipos_de_dados_basicos.md)