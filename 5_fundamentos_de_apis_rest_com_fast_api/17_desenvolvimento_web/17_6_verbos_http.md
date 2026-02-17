# Aula 17.6 – Verbos HTTP (GET, POST, PUT, PATCH e DELETE)

O protocolo HTTP define vários "verbos" (ou métodos), que indicam  
qual tipo de ação queremos realizar em uma API ou servidor.

Os principais são: **GET, POST, PUT, PATCH e DELETE**.

---

## 1️⃣ GET → Ler dados
Usado para pedir informações do servidor (não altera nada).  
**Exemplo:** buscar todos os usuários ou um produto específico.

```python
import requests

print("=== GET ===")
resposta_get = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(resposta_get.json())  # mostra os dados do usuário 1
```
---

## 2️⃣ POST → Criar dados

Usado para enviar informações novas ao servidor (criar um recurso).

```python
print("\n=== POST ===")
novo_usuario = {"name": "Carlos", "email": "carlos@exemplo.com"}
resposta_post = requests.post("https://jsonplaceholder.typicode.com/users", json=novo_usuario)
print(resposta_post.json())  # o servidor responde com o recurso criado
```
---

## 3️⃣ PUT → Atualizar (substituir) dados

Substitui completamente um recurso existente.
**Exemplo:** enviar um PUT em /usuarios/1 substitui todos os dados anteriores.

```python
print("\n=== PUT ===")
usuario_atualizado = {"name": "Carlos Atualizado", "email": "carlosnovo@exemplo.com"}
resposta_put = requests.put("https://jsonplaceholder.typicode.com/users/1", json=usuario_atualizado)
print(resposta_put.json())
```
---

## 4️⃣ PATCH → Atualizar parcialmente

Atualiza apenas alguns campos em vez de tudo (parcial).

```python
print("\n=== PATCH ===")
atualizacao_parcial = {"email": "carlospatch@exemplo.com"}
resposta_patch = requests.patch("https://jsonplaceholder.typicode.com/users/1", json=atualizacao_parcial)
print(resposta_patch.json())
```
---

## 5️⃣ DELETE → Apagar dados

Usado para excluir um recurso existente.

```python
print("\n=== DELETE ===")
resposta_delete = requests.delete("https://jsonplaceholder.typicode.com/users/1")
print("Status:", resposta_delete.status_code)  # 200 ou 204 indica sucesso
```
---

## 6️⃣ Resumo rápido

| Verbo   | Ação                | Exemplo prático                   |
|---------|-------------------|----------------------------------|
| GET     | Ler dados          | Buscar lista de usuários         |
| POST    | Criar dados        | Cadastrar novo usuário           |
| PUT     | Atualizar (tudo)   | Alterar todos os dados do usuário |
| PATCH   | Atualizar (parte)  | Alterar apenas o e-mail do usuário |
| DELETE  | Apagar dados       | Excluir usuário do sistema       |

---

## 7️⃣ Dicas importantes

- 🔹 Use **GET** com segurança — nunca deve alterar dados do servidor  
- 🔹 Use **POST, PUT, PATCH e DELETE** com cuidado — eles alteram o banco  
- 🔹 Sempre valide e trate erros de requisição (`status_code`, `timeouts`, etc.)  

---

✍️ **Próxima aula:** [17 – Resumo completo do desenvolvimento web](17_resumo_da_aula_17.md)