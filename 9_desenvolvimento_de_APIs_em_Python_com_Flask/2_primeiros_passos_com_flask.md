# 2 Primeiros Passos com Flask

Neste capítulo, exploramos como iniciar um projeto simples usando o **Flask**, entendendo sua estrutura básica, como instalar, criar rotas e executar a aplicação localmente.

---

## 🚀 Instalação do Flask

Antes de tudo, é necessário instalar o Flask em seu ambiente Python.

### **Instalação usando pip**
```bash
pip install flask
````

Após instalar, você já pode criar sua primeira aplicação.

---

## 🧩 Estrutura Básica de um Projeto Flask

O esqueleto mínimo de uma aplicação em Flask contém:

* Uma **instância de `Flask`**
* Definição de **rotas**
* Execução da aplicação

### Exemplo básico:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🛣️ Criando Rotas

Rotas são caminhos (URLs) que o usuário acessa.
Cada rota é associada a uma função chamada **view function**.

### Exemplo:

```python
@app.route("/sobre")
def sobre():
    return {"mensagem": "API criada com Flask!"}
```

Flask permite retornar:

* Texto simples
* HTML
* JSON
* Respostas personalizadas

Em APIs REST, normalmente retornamos **JSON**.

---

## ⚙️ Execução da Aplicação

Para rodar o projeto, execute no terminal:

```bash
python app.py
```

Ou usando a variável de ambiente:

```bash
set FLASK_APP=app.py
flask run
```

Após executar, a aplicação estará acessível em:

```
http://127.0.0.1:5000/
```

---

## 🔁 Modo Debug

Durante o desenvolvimento, é útil ativar o **modo debug**, que:

* Reinicia automaticamente o servidor a cada alteração
* Exibe erros detalhados no navegador

Isso é feito com:

```python
app.run(debug=True)
```

---

## 🧱 Estrutura Recomendada de Pastas (mínima)

Para APIs pequenas, você pode usar apenas um arquivo, mas o recomendado é evoluir para uma estrutura organizada:

```
meu_projeto/
│
├── app.py
├── requirements.txt
└── venv/
```

Para APIs maiores, você poderá dividir em módulos como:

* `routes/`
* `models/`
* `controllers/`
* `config/`
* `tests/`

Será visto nos próximos capítulos.

---

## ✔️ Conclusão

Você agora conhece:

* Como instalar o Flask
* Como criar uma aplicação básica
* Como definir rotas
* Como executar o servidor
* Como utilizar o modo debug

Esses são os fundamentos essenciais para começar a desenvolver APIs RESTful com Flask.
```