# Deploy de uma API Flask

Depois de desenvolver e testar sua API Flask, o próximo passo é colocá-la no ar para que outras pessoas ou serviços possam utilizá-la.  
Neste capítulo, você aprenderá como funcionam os conceitos essenciais de deploy e como publicar uma API Flask em diferentes ambientes.

---

## 🌐 O que é Deploy?

**Deploy** significa colocar sua aplicação em um servidor para que ela possa ser acessada pela internet ou por uma rede interna.

O processo envolve:

- Escolher um ambiente (local, nuvem, Docker, VPS, etc.)
- Configurar servidor web (Gunicorn, Nginx, etc.)
- Ajustar variáveis de ambiente
- Lidar com logs, erros e escalabilidade

---

# 📦 1. Preparando o Projeto para Deploy

Antes de enviar sua API para produção, é importante preparar alguns arquivos:

---

## 📄 requirements.txt

Liste todas as dependências:

```bash
pip freeze > requirements.txt
````

---

## 🔒 Variáveis de ambiente

Nunca deixe senhas, tokens, chaves JWT ou credenciais dentro do código.

Exemplo usando `os.environ`:

```python
import os

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
```

No servidor, você define:

```bash
export JWT_SECRET_KEY="minha-chave-produção"
```

---

# 🚀 2. Rodando Flask em Produção

### ❌ Nunca use o servidor interno do Flask em produção!

Ele é apenas para desenvolvimento.

### ✔️ Em produção usamos:

* **Gunicorn** (Linux)
* **Waitress** (Windows)
* **uWSGI** (alternativa robusta)
* **Nginx** como proxy reverso

---

## Exemplo usando Gunicorn (Linux)

Instale:

```bash
pip install gunicorn
```

Execute:

```bash
gunicorn app:app
```

Se você usa a função `create_app()`, então:

```bash
gunicorn "app:create_app()"
```

---

# 🌍 3. Deploy em Serviços Populares

Aqui estão os ambientes mais usados para publicar APIs Flask.

---

## 🟦 Deploy no Railway (muito simples)

Railway é gratuito e fácil para iniciantes.

### Passos:

1. Criar conta em railway.app
2. Criar novo projeto → Deploy from GitHub
3. Ter no repositório:

   * `requirements.txt`
   * `Procfile` (opcional)
4. Railway detecta Flask automaticamente

### Exemplo de **Procfile**:

```
web: gunicorn app:app
```

---

## 🟪 Deploy no Render.com

Muito parecido com Railway.

Criar um **Web Service** e apontar para seu GitHub.

Comando de start:

```
gunicorn app:app
```

---

## 📦 Deploy com Docker

Docker é uma solução profissional e muito usada.

### Criando um Dockerfile:

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

### Build:

```bash
docker build -t minha-api .
```

### Executar o container:

```bash
docker run -p 8000:8000 minha-api
```

---

## 🖥️ Deploy em VPS (Ubuntu + Nginx)

Arquitetura comum:

```
Nginx  →  Gunicorn  →  Flask App
```

### Instalar Nginx:

```bash
sudo apt update
sudo apt install nginx
```

### Configurar Gunicorn + serviço systemd

Crie:

```
/etc/systemd/system/minhaapi.service
```

Conteúdo:

```
[Unit]
Description=API Flask rodando com Gunicorn
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/minhaapi
ExecStart=/usr/bin/gunicorn app:app --bind 127.0.0.1:8000

[Install]
WantedBy=multi-user.target
```

Ativar:

```bash
sudo systemctl start minhaapi
sudo systemctl enable minhaapi
```

### Configurar Nginx como proxy reverso

Arquivo:

```
/etc/nginx/sites-available/minhaapi
```

Conteúdo:

```
server {
    listen 80;
    server_name seu_dominio.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

Ativar e reiniciar:

```bash
sudo ln -s /etc/nginx/sites-available/minhaapi /etc/nginx/sites-enabled
sudo systemctl restart nginx
```

---

# 📊 4. Logs e Monitoramento

Para API em produção, monitore:

* Erros (500)
* Lentidão
* Quantidade de requisições
* Uso de CPU/RAM

Ferramentas úteis:

* Loguru
* Sentry
* Prometheus + Grafana

---

# 🧪 5. Ambiente de Testes, Staging e Produção

Ambientes recomendados:

* **Dev** → código local
* **Staging** → simula produção
* **Produção** → servidor real

Cada ambiente deve ter suas próprias variáveis e banco de dados.

---

# ✔️ Conclusão

Neste capítulo você aprendeu:

* Como preparar o projeto Flask para deploy
* Como rodar a aplicação com Gunicorn
* Como configurar Docker
* Deploy em Railway, Render e VPS
* Como usar Nginx como proxy reverso
* Boas práticas para produção

Com isso, sua API Flask pode ser publicada em qualquer ambiente moderno, de forma profissional e escalável.