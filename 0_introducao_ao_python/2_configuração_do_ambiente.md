# ⚙️ 0.2 – Configuração do Ambiente de Desenvolvimento

## 🎯 1. Objetivo Geral

Instalar e configurar o ambiente necessário para **desenvolver projetos em Python** de forma simples, prática e eficiente.

---

## 🐍 2. Instalando o Python

### 🧩 2.1 Linux e macOS

Na maior parte das distribuições Linux e macOS, o Python já vem instalado.
Para verificar a versão disponível, abra o terminal e execute:

```bash
python -V
# ou
python3 -V
```

Se aparecer algo como `Python 3.x.x`, está tudo certo.

Caso precise instalar manualmente, utilize o gerenciador de pacotes:

```bash
sudo apt install python3
```

---

### 🪟 2.2 Windows

No **Windows**, será necessário instalar o Python manualmente:

1. Acesse o site oficial:
   👉 [https://www.python.org](https://www.python.org)
2. Baixe a versão mais recente.
3. **Marque a opção “Add Python to PATH”** antes de instalar.
4. Conclua seguindo as instruções na tela.
   👉 Tutorial detalhado: [https://python.org.br/instalacao-windows/](https://python.org.br/instalacao-windows/)

Após a instalação, confirme no CMD:

```bash
python -V
```

---

## 💻 3. Instalando e Configurando a IDE

Para escrever seus códigos Python, usaremos uma **IDE**.
As mais recomendadas são:

* **Visual Studio Code (VS Code)**
* **PyCharm**

---

### 💡 3.1 Nossa Escolha: VS Code

O **VS Code** será nossa IDE principal, pois é:

* 🟢 Gratuito
* ⚙️ Leve e rápido
* 🧠 Altamente personalizável
* 🌍 Multiplataforma

Baixe em:
👉 [https://code.visualstudio.com/](https://code.visualstudio.com/)

Após instalar, abra o VS Code e instale a **extensão oficial do Python**:

> 💡 Pressione `Ctrl + Shift + X` → pesquise por “Python” → clique em **Instalar**.

---

## 🧪 4. Testando o Ambiente

Agora vamos testar seu ambiente Python! 🚀

1. Crie um arquivo com extensão `.py`
2. Digite:

```python
print("Olá, mundo!")
```

3. Execute pelo terminal:

```bash
python nome_do_arquivo.py
```

Se aparecer **Olá, mundo!**, tudo está funcionando perfeitamente! 🎉

---

✍️ **Próxima aula:** [0.3 – Terminal e Comandos Básicos](3_terminal_e_comandos_basicos.md)