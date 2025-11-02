# Aula 17.2 – Como a Web Funciona

## 🌐 Modelo Cliente-Servidor
A web funciona com base em um modelo chamado **cliente-servidor**.  
Esse modelo define como o seu computador (**cliente**) se comunica com outro computador (**servidor**) para trocar informações através da internet.

### 🔹 Cliente e Servidor
- **Cliente:** quem faz o pedido (geralmente o navegador, como Chrome ou Firefox)  
- **Servidor:** recebe o pedido, processa e envia uma resposta (ex: servidores da Google, Netflix, etc.)

**Fluxo básico:**

Cliente (navegador) ➜ faz uma **REQUISIÇÃO** ➜ Servidor  
Servidor ➜ processa e envia uma **RESPOSTA** ➜ Cliente (navegador)

---

## 📩 O que é uma Requisição (Request)?
É a mensagem que o cliente envia ao servidor pedindo alguma informação.  

**Exemplo:** quando você acessa um site, o navegador envia uma requisição pedindo a página HTML.

---

## 📤 O que é uma Resposta (Response)?
É o que o servidor devolve para o cliente.  
Pode ser:
- Uma página HTML  
- Um arquivo ou imagem  
- Dados em formato JSON (em APIs)

---

## 🔗 URL – Localizador de Recurso
**URL** significa *Uniform Resource Locator* (Localizador Uniforme de Recursos)  
É o endereço que identifica onde está o recurso que você quer acessar.

**Exemplo:** `https://www.exemplo.com/produtos?id=10`  
- `https` → protocolo de comunicação  
- `www.exemplo.com` → domínio (onde está o servidor)  
- `/produtos` → caminho/rota do recurso  
- `?id=10` → parâmetro enviado junto na requisição

---

## 🛡️ Protocolo HTTP/HTTPS
- **HTTP:** HyperText Transfer Protocol (Protocolo de Transferência de Hipertexto)  
- **HTTPS:** versão segura do HTTP (usa criptografia)

É o "idioma" que o cliente e o servidor usam para conversar, definindo regras de requisição e resposta.

---

## ⚙️ Processo simplificado de um site
1. O usuário digita um endereço no navegador  
2. O navegador envia uma requisição HTTP para o servidor  
3. O servidor processa a requisição (pode consultar banco de dados, rodar códigos, etc.)  
4. O servidor envia uma resposta HTTP (página, dados, etc.)  
5. O navegador exibe o resultado para o usuário

---

## 🐍 Exemplo prático em Python
```python
import requests  # biblioteca para fazer requisições HTTP

resposta = requests.get("https://api.github.com")  # cliente faz uma requisição GET
print("Status:", resposta.status_code)  # código de status (200 = sucesso)
print("Conteúdo:", resposta.text[:200])  # mostra parte do conteúdo da resposta
```
## 🧠 Resumo

- A web funciona com **cliente e servidor**  
- O cliente envia **requisições** e o servidor devolve **respostas**  
- O protocolo **HTTP/HTTPS** define como a comunicação acontece  
- A **URL** indica onde está o recurso que você quer acessar  
- É possível simular requisições e respostas usando **Python** com a biblioteca `requests`

✍️ **Próxima aula:** [17.2 – Como a Web Funciona](17_3_tecnologias_frontend_e_backend.md)