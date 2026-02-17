# Autenticação e Autorização em Flask

Neste capítulo, abordamos dois pilares fundamentais da segurança em APIs RESTful: **autenticação** e **autorização**.  
Também veremos como aplicá-los no Flask utilizando **JWT (JSON Web Tokens)**, uma das formas mais modernas e seguras de controle de acesso.

---

## 🔐 Diferença entre Autenticação e Autorização

É comum confundir esses dois termos, mas eles têm propósitos diferentes:

### **Autenticação**
É o processo de **verificar quem é o usuário**.  
Exemplos:
- Login com usuário e senha  
- Token de acesso  
- OAuth  
- Biometria  

### **Autorização**
Define **o que o usuário pode fazer** após ser autenticado.  
Exemplos:
- Acesso restrito apenas para admins  
- Usuário comum só acessa seus próprios dados  
- Rotas privadas e rotas públicas  

> **Autenticação:** “Quem é você?”  
> **Autorização:** “O que você pode fazer?”

---

## 🧩 Por que usar JWT?

JWT (JSON Web Token) é um padrão (RFC 7519) que permite enviar informações seguras entre cliente e servidor usando um token codificado.

### **Vantagens do JWT**
- **Stateless:** o servidor não precisa guardar sessão  
- **Compacto:** cabe em headers HTTP, URLs e JSON  
- **Seguro:** pode ser assinado e criptografado  
- **Autocontido:** contém todas as infos do usuário  

JWT é amplamente usado em APIs modernas por sua praticidade e eficiência.

---

## 🧱 Estrutura de um JWT

Um token JWT possui 3 partes separadas por pontos:

```

header.payload.signature

````

### **1. Header**
Define o tipo do token e o algoritmo usado.

### **2. Payload**
Contém dados sobre o usuário (claims).

### **3. Signature**
Garante a integridade do token.

---

## 🔑 Gerando um JWT no Flask

Para usar JWT no Flask, geralmente utilizamos a biblioteca:

```bash
pip install flask-jwt-extended
````

### **Exemplo de criação de token**

```python
from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "senha-secreta-super-segura"

jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()

    if dados["usuario"] != "admin" or dados["senha"] != "123":
        return {"erro": "Credenciais inválidas"}, 401

    token = create_access_token(identity=dados["usuario"])
    return {"token": token}
```

---

## 🔒 Protegendo Rotas com JWT

Para proteger uma rota, usamos o decorador:

```python
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route("/perfil")
@jwt_required()
def perfil():
    usuario = get_jwt_identity()
    return {"mensagem": f"Bem-vindo, {usuario}!"}
```

Agora, essa rota só pode ser acessada enviando um JWT válido no header:

```
Authorization: Bearer <seu_token>
```

---

## 🛡️ Controle de Permissões (Autorização)

Além de autenticar o usuário, podemos controlar o que ele pode acessar.

### Exemplo simples com níveis de acesso

```python
@app.route("/admin")
@jwt_required()
def admin():
    usuario = get_jwt_identity()

    if usuario != "admin":
        return {"erro": "Acesso negado"}, 403

    return {"mensagem": "Bem-vindo, administrador!"}
```

---

## ⚠️ Boas Práticas de Segurança

* Nunca exponha sua `JWT_SECRET_KEY`
* Defina tempo de expiração dos tokens
* Use HTTPS sempre que possível
* Valide dados enviados pelo cliente
* Nunca coloque informações sensíveis no payload do JWT
* Revogue tokens quando necessário

---

## ✔️ Conclusão

Neste capítulo, você aprendeu:

* A diferença entre autenticação e autorização
* Como JWT funciona e por que é a escolha ideal para APIs
* Como gerar tokens e proteger rotas no Flask
* Como implementar diferentes níveis de permissão
* Melhores práticas de segurança

Com esse conhecimento, sua API Flask já pode trabalhar com usuários, sessões e rotas protegidas de forma segura e profissional.

```
