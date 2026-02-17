Aqui está o capítulo **3_Modelos_e_Banco_de_Dados_no_Django.md**, organizado, corrigido e formatado em **Markdown**, seguindo o padrão dos anteriores:

---

````md
# 📘 3 – Modelos e Banco de Dados no Django

Neste capítulo, você aprenderá como o Django lida com dados utilizando **modelos**, **ORM** e **migrações**. Essa é uma das partes mais poderosas do framework, permitindo trabalhar com banco de dados de forma simples e eficiente.

---

## 🧩 O que são Modelos?

**Modelos (Models)** são classes Python que representam tabelas no banco de dados.  
Cada atributo da classe é um campo na tabela.

Exemplo simples de modelo:

```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
````

Quando você cria esse modelo, o Django automaticamente gera SQL equivalente para criar a tabela no banco.

---

## 🛠️ Criando Modelos

Todos os modelos são criados dentro do arquivo:

```
core/models.py
```

Exemplo completo:

```python
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
```

### Campos mais comuns:

| Tipo de Campo     | Descrição                      |
| ----------------- | ------------------------------ |
| `CharField`       | Texto curto                    |
| `TextField`       | Texto longo                    |
| `IntegerField`    | Número inteiro                 |
| `DecimalField`    | Valores decimais (ex.: preços) |
| `BooleanField`    | Verdadeiro/Falso               |
| `DateField`       | Datas                          |
| `DateTimeField`   | Data + hora                    |
| `EmailField`      | E-mail válido                  |
| `ForeignKey`      | Relacionamento 1:N             |
| `ManyToManyField` | Relacionamento N:N             |

---

## 🔗 Relacionamentos Entre Modelos

### 1. **Um para Muitos (ForeignKey)**

```python
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
```

### 2. **Muitos para Muitos**

```python
class Tag(models.Model):
    nome = models.CharField(max_length=50)

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
```

### 3. **Um para Um**

```python
class Perfil(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField()
```

---

## 🏗️ Migrações (Migrations)

As migrações são como **versões do banco de dados**.
Sempre que alterar um modelo, você deve gerar e aplicar migrações.

### Criar migração:

```bash
python manage.py makemigrations
```

### Aplicar migrações:

```bash
python manage.py migrate
```

Isso cria ou atualiza as tabelas automaticamente.

---

## 📦 Usando o Django ORM

O ORM do Django permite consultar o banco usando Python, sem escrever SQL.

### Criar um objeto:

```python
from core.models import Produto

Produto.objects.create(nome="Mouse", preco=50.00, estoque=10)
```

### Buscar todos:

```python
Produto.objects.all()
```

### Buscar um item:

```python
Produto.objects.get(id=1)
```

### Filtrar:

```python
Produto.objects.filter(estoque__gt=5)
```

### Atualizar:

```python
p = Produto.objects.get(id=1)
p.preco = 60.00
p.save()
```

### Deletar:

```python
Produto.objects.get(id=1).delete()
```

---

## 🛠️ Trabalhando no Shell do Django

O Django oferece um shell interativo para testar o ORM:

```bash
python manage.py shell
```

Dentro dele, você pode manipular o banco diretamente usando Python.

---

## 🗄️ Configurando o Banco de Dados

Por padrão, o Django usa SQLite.
No arquivo `settings.py`, você pode trocar para:

* PostgreSQL
* MySQL
* MariaDB
* Oracle

Exemplo com PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'meubanco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## ✔️ Conclusão

Neste capítulo, você aprendeu:

* O que são modelos e como criá-los
* Tipos de campos
* Relacionamentos entre tabelas
* Como funcionam migrações
* Como usar o ORM para criar, consultar, atualizar e deletar dados
* Como configurar o banco de dados

Com essa base, você já tem o núcleo fundamental para o desenvolvimento full stack com Django.