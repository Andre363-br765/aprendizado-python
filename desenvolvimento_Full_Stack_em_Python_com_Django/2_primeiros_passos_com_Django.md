Aqui está o arquivo **2_primeiros_passos_com_Django.md**, totalmente organizado e pronto para o seu módulo de estudos:

---

````md
# 📘 2 – Primeiros Passos com Django

Neste capítulo, você aprenderá como iniciar um projeto Django, entender sua estrutura básica e criar sua primeira aplicação funcional dentro do framework.

---

## 🚀 Instalando o Django

Antes de tudo, é necessário instalar o Django utilizando o `pip`.

### **Instalação:**
```bash
pip install django
````

Para verificar se tudo deu certo:

```bash
django-admin --version
```

---

## 📁 Criando um novo projeto Django

O primeiro passo é criar o **projeto**, que representa a configuração principal da aplicação.

### **Criando o projeto:**

```bash
django-admin startproject meu_projeto
```

A estrutura criada será parecida com:

```
meu_projeto/
│
├── manage.py
└── meu_projeto/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

### Significado dos arquivos principais:

* **manage.py**: Executa comandos administrativos.
* **settings.py**: Configurações gerais do projeto.
* **urls.py**: Rotas principais.
* **wsgi.py / asgi.py**: Pontos de entrada para servidores web.

---

## 🧩 Criando um aplicativo (app) dentro do projeto

Projetos Django são organizados em **apps**, que representam funcionalidades independentes.

### Criando um app:

```bash
python manage.py startapp core
```

Estrutura do app:

```
core/
│
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py   (criado manualmente depois)
└── views.py
```

### Registrando o app no projeto:

No arquivo `settings.py`, adicione:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

---

## 🛠️ Criando a primeira view

A view é responsável pela lógica da resposta a uma requisição.

No arquivo `core/views.py`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao meu primeiro projeto Django!")
```

---

## 🌐 Criando rotas (URLs)

Primeiro, crie o arquivo `core/urls.py`:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

Agora, conecte o app ao `urls.py` principal:

Em `meu_projeto/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

---

## ▶️ Executando o servidor de desenvolvimento

Para rodar o servidor local:

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

Você verá a mensagem da sua primeira view.

---

## 🔁 Estrutura MTV do Django

O Django utiliza a arquitetura **MTV** (Model–Template–View):

* **Model** → Representa dados e regras de negócio
* **Template** → Interface visual (HTML)
* **View** → Lógica de processamento das requisições

É similar ao MVC, mas com responsabilidades mais bem definidas.

---

## ✔️ Conclusão

Você agora aprendeu:

* Instalar o Django
* Criar um projeto
* Criar um app
* Registrar apps
* Criar views
* Criar URLs
* Rodar o servidor
* Entender a estrutura MTV

Com isso, já é possível construir funcionalidades reais utilizando o Django.