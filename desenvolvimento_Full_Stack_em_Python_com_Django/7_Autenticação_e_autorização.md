Aqui está o arquivo **7_Autenticação_e_autorização.md** seguindo o mesmo estilo dos anteriores:

---

# **Autenticação e Autorização no Django**

A **autenticação** e a **autorização** são pilares essenciais na segurança de aplicações web.
O Django fornece um sistema robusto, completo e pronto para uso, permitindo implementar login, controle de acesso, grupos, permissões e proteção de rotas com extrema facilidade.

Este módulo apresenta como esses recursos funcionam e como aplicá-los no desenvolvimento de sistemas Full Stack.

---

## **1. Diferença entre Autenticação e Autorização**

### **✔ Autenticação**

Processo de verificar a identidade de um usuário.
Exemplos comuns:

* login com nome de usuário e senha
* login via token
* autenticação por sessão

### **✔ Autorização**

Processo que define o que cada usuário pode fazer.
Exemplos:

* acesso a páginas restritas
* permissões para editar, excluir ou visualizar dados
* rotas que apenas administradores podem acessar

---

## **2. Sistema de Autenticação do Django**

O Django inclui, nativamente:

* Modelos de usuário prontos
* Login e logout
* Recuperação e redefinição de senha
* Middleware de autenticação
* View genérica de login
* Permissões e grupos
* Decoradores para proteger rotas

Ele segue a filosofia **batteries included**, entregando tudo pronto para usar.

---

## **3. Criando Usuários e Gerenciando Login**

### **3.1. Criando usuário pelo terminal**

```bash
python manage.py createsuperuser
```

### **3.2. View de Login**

O Django já fornece:

```python
from django.contrib.auth.views import LoginView

class LoginUsuario(LoginView):
    template_name = 'login.html'
```

### **3.3. Template de Login**

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Entrar</button>
</form>
```

---

## **4. Verificando Usuário Logado**

No template:

```html
{% if user.is_authenticated %}
  Bem-vindo, {{ user.username }}!
{% else %}
  Você não está logado.
{% endif %}
```

Na view:

```python
if request.user.is_authenticated:
    ...
```

---

## **5. Protegendo Rotas com Decoradores**

### **✔ Login Obrigatório**

```python
from django.contrib.auth.decorators import login_required

@login_required
def painel(request):
    return render(request, 'painel.html')
```

Se o usuário não estiver logado, será redirecionado automaticamente para `/accounts/login/`.

---

## **6. Permissões e Grupos**

### **6.1. Permissões**

O Django cria permissões automaticamente para cada modelo:

* adicionar
* alterar
* excluir
* visualizar

Verificação:

```python
if request.user.has_perm('app.change_modelo'):
    ...
```

### **6.2. Grupos**

Os grupos facilitam o gerenciamento de vários usuários com a mesma permissão.

```python
from django.contrib.auth.models import Group

grupo = Group.objects.create(name='Gerentes')
user.groups.add(grupo)
```

---

## **7. Autorização por Decoradores**

### **Apenas administradores**

```python
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_area(request):
    ...
```

### **Exigir permissão específica**

```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.view_relatorio')
def relatorio(request):
    ...
```

---

## **8. Login e Logout Manual**

```python
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], 
                            password=request.POST['password'])
        if user:
            login(request, user)
```

Logout:

```python
def sair(request):
    logout(request)
    return redirect('home')
```

---

## **9. Reset de Senha (Sistema Completo)**

O Django já fornece todas as views prontas:

* solicitação de reset
* envio de email
* confirmação
* criação de nova senha

Basta adicionar no `urls.py`:

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reset/', auth_views.PasswordResetView.as_view(), name='reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view()),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view()),
]
```

---

## **10. Autenticação com Tokens (APIs)**

Para APIs, geralmente se usa:

* JWT
* Token Authentication
* OAuth2

Com Django REST Framework, por exemplo:

```bash
pip install djangorestframework-simplejwt
```

---

## **Resumo Final**

* **Autenticação** identifica quem é o usuário.
* **Autorização** define o que ele pode fazer.
* O Django fornece um sistema completo:

  * login/logout
  * permissões
  * grupos
  * reset de senha
  * middleware e decoradores
* Ferramentas prontas facilitam o desenvolvimento seguro.
* Integra-se facilmente com soluções modernas como JWT.