Aqui está o arquivo **Formulários_Django.md** seguindo o mesmo estilo dos anteriores:

---

# **Formulários no Django**

Os **formulários** no Django são uma parte essencial para lidar com entrada de dados, validação e interação com o usuário.
O framework oferece duas abordagens principais:

* **Forms (Django Forms)** – formulários definidos manualmente
* **ModelForms** – formulários gerados automaticamente a partir de modelos

Ambas oferecem recursos completos de validação, limpeza de dados e integração com templates.

---

## **1. O que são Django Forms?**

Um **Form** é uma classe Python que define campos, regras de validação e a lógica necessária para processar dados enviados pelo usuário.

Exemplo básico:

```python
from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
```

---

## **2. Renderizando um Form no Template**

### **2.1. View**

```python
from django.shortcuts import render
from .forms import ContatoForm

def contato(request):
    form = ContatoForm()
    return render(request, 'contato.html', {'form': form})
```

### **2.2. Template**

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Enviar</button>
</form>
```

O Django fornece formas automáticas de renderização:

* `form.as_p` – parágrafos
* `form.as_ul` – lista
* `form.as_table` – tabela

---

## **3. Processando Dados do Formulário**

Quando o formulário é enviado, precisamos validar os dados.

```python
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            mensagem = form.cleaned_data['mensagem']
            # salvar, enviar email, etc.
    else:
        form = ContatoForm()

    return render(request, 'contato.html', {'form': form})
```

Se `form.is_valid()` for verdadeiro:

* Os dados são validados
* Estão acessíveis em `cleaned_data`

---

## **4. Validações Personalizadas**

### **4.1. Validação em campo específico**

```python
def clean_nome(self):
    nome = self.cleaned_data['nome']
    if len(nome.split()) < 2:
        raise forms.ValidationError("Digite seu nome completo.")
    return nome
```

### **4.2. Validação geral**

```python
def clean(self):
    cleaned = super().clean()
    email = cleaned.get('email')
    if email and not email.endswith('@gmail.com'):
        raise forms.ValidationError("O email deve ser do Gmail.")
    return cleaned
```

---

## **5. ModelForms (Formulários baseados em modelos)**

Um **ModelForm** cria automaticamente um formulário baseado em um modelo Django.

### **5.1. Exemplo de Modelo**

```python
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
```

### **5.2. ModelForm**

```python
from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade']
```

Isso elimina necessidade de criar os campos manualmente.

---

## **6. Salvando Dados com ModelForm**

### **View**

```python
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva direto no banco
            return redirect('home')
    else:
        form = ClienteForm()

    return render(request, 'cadastrar.html', {'form': form})
```

---

## **7. Personalizando Formulários**

### **Widgets**

Alteram a aparência (input, textarea, select…):

```python
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'min': 0})
        }
```

---

## **8. Tratamento Automático de Segurança**

Os formulários no Django já incluem:

* Proteção **CSRF**
* Validação automática de tipos
* Limpeza contra injeção HTML
* Serialização segura de dados

---

## **Resumo Final**

* **Forms** permitem criar formulários totalmente personalizados.
* **ModelForms** automatizam a criação baseada em modelos.
* Django oferece um sistema robusto de validação e limpeza de dados.
* Templates rendem facilmente formulários HTML com `{{ form }}`.
* Widgets permitem personalização visual.
* O sistema de formulários integra-se naturalmente com views e banco de dados.