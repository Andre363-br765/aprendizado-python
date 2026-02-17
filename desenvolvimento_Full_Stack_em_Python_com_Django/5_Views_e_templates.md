Aqui está o arquivo **5_Views_e_templates.md** seguindo o padrão dos anteriores:

---

# **Views e Templates no Django**

As **views** e **templates** são dois dos componentes principais do Django.
Elas trabalham juntas para entregar páginas dinâmicas:

* **Views** → processam requisições e retornam respostas.
* **Templates** → definem o HTML exibido ao usuário.

---

## **1. O que são Views?**

Views são funções ou classes que recebem uma requisição (`request`) e retornam uma resposta (`HttpResponse`), geralmente renderizando um template.

Existem dois tipos:

### **1.1. Views baseadas em função (FBV – Function-Based Views)**

Exemplo simples:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

### **1.2. Views baseadas em classe (CBV – Class-Based Views)**

Exemplo simples:

```python
from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
```

CBVs fornecem muito mais recursos e reaproveitamento de código.

---

## **2. O que são Templates?**

Templates são arquivos HTML que podem conter:

* Variáveis
* Estruturas condicionais
* Loops
* Inclusão de outros templates
* Blocos substituíveis
* Filtros

Eles usam a **Template Language** do Django.

Exemplo de template:

```html
<h1>Olá, {{ usuario }}</h1>
```

---

## **3. Estrutura de Templates**

Normalmente criamos uma pasta:

```
/app/
    templates/
        app/
            home.html
```

E registramos no `settings.py` se for usar templates globais:

```python
'DIRS': [BASE_DIR / 'templates']
```

---

## **4. Renderizando Templates**

A função `render()` junta a view com o template:

```python
def home(request):
    contexto = {
        'titulo': 'Página Inicial',
        'usuario': 'Visitante'
    }
    return render(request, 'app/home.html', contexto)
```

---

## **5. Template Language – Recursos Principais**

### **5.1. Variáveis**

```html
<p>{{ nome }}</p>
```

### **5.2. Estrutura condicional**

```html
{% if logado %}
  <p>Bem-vindo!</p>
{% else %}
  <p>Faça login.</p>
{% endif %}
```

### **5.3. Laços**

```html
{% for item in lista %}
  <li>{{ item }}</li>
{% endfor %}
```

### **5.4. Comentários**

```html
{# Comentário invisível no HTML final #}
```

### **5.5. Filtros**

```html
{{ nome|upper }}
{{ data|date:"d/m/Y" }}
```

---

## **6. Herança de Templates**

Um dos recursos mais poderosos:
Permite criar um HTML base e extender nas páginas.

### **6.1. Template base**

`base.html`:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <title>{% block titulo %}{% endblock %}</title>
</head>
<body>
  <header>Menu principal</header>

  <main>
    {% block conteudo %}{% endblock %}
  </main>

  <footer>Rodapé</footer>
</body>
</html>
```

### **6.2. Template filho**

`home.html`:

```html
{% extends 'base.html' %}

{% block titulo %}Home{% endblock %}

{% block conteudo %}
  <h1>Bem-vindo à Home!</h1>
{% endblock %}
```

---

## **7. Views + Templates + URLs**

Fluxo completo:

1. Usuário acessa `/home/`
2. URL chama a view
3. View processa e envia dados para o template
4. Template é renderizado e devolvido ao cliente

Exemplo:

### **7.1. urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

## **Resumo Final**

* Views processam as requisições e retornam respostas.
* Templates definem o HTML que será exibido ao usuário.
* A template language do Django permite lógica simples (loops, condições, filtros).
* Herança de templates organiza e reaproveita muito o código.
* A integração entre URLs → Views → Templates forma o fluxo principal de uma aplicação Django.