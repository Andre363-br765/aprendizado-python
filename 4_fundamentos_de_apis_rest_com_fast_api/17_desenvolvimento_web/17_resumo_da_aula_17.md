# Aula 17 – Introdução ao Desenvolvimento Web
**Resumo completo das aulas 17.1 a 17.6**

---

## 1️⃣ O que é Desenvolvimento Web
- Processo de criar sites, sistemas e aplicativos que funcionam na internet.  
- Dois lados principais:  
  - **FRONT-END** → o que o usuário vê (HTML, CSS, JS)  
  - **BACK-END** → o que acontece no servidor (Python, Node.js, PHP, Java, etc.)  
- Tipos de aplicações:
  - Sites estáticos
  - Aplicações dinâmicas
  - Web Apps
  - APIs

---

## 2️⃣ Como a Web Funciona
- Modelo **CLIENTE ↔ SERVIDOR**  
- CLIENTE (navegador) envia **REQUISIÇÕES** → SERVIDOR responde  
- Comunicação via HTTP ou HTTPS  
- **URL:** endereço do recurso (ex: `https://meusite.com/produtos?id=10`)  

**Processo básico:**
1. O usuário acessa um site  
2. O navegador envia uma requisição  
3. O servidor processa e responde  
4. O navegador exibe o resultado

---

## 3️⃣ Tecnologias Front-end e Back-end
**FRONT-END → interface visual**
- HTML → estrutura  
- CSS → estilo  
- JS → interatividade  
- Frameworks: React, Vue, Angular, Tailwind

**BACK-END → lógica, regras e banco de dados**
- Linguagens: Python, Node.js, PHP, Java, C#  
- Frameworks: Flask, Django, Express, Laravel, Spring Boot  
- Banco de Dados: MySQL, PostgreSQL, MongoDB, Firebase  

**Fluxo de comunicação:**
- FRONT-END faz o pedido → BACK-END processa → devolve resposta

---

## 4️⃣ APIs e Conceitos Fundamentais
- **API** = Interface de Programação de Aplicações  
- Permite que sistemas diferentes conversem entre si  
- Exemplo: app do clima busca dados de um servidor via API  

**Estrutura básica:**

CLIENTE → requisição HTTP → SERVIDOR → resposta JSON


**Importância:**
- Reutilização de dados  
- Integração entre plataformas  
- Comunicação entre apps

---

## 5️⃣ Tipos de APIs
- **RESTful** → mais comum, usa HTTP e JSON, simples e rápido  
- **SOAP** → mais formal, baseado em XML, usado em sistemas corporativos  
- **GraphQL** → moderno e flexível, consulta apenas os dados necessários  

**Comparativo rápido:**

| Tipo     | Formato | Simplicidade | Flexibilidade | Segurança | Popularidade |
|----------|---------|--------------|---------------|-----------|--------------|
| REST     | JSON    | Alta         | Média         | Boa       | Muito Alta   |
| SOAP     | XML     | Baixa        | Baixa         | Muito Alta| Média        |
| GraphQL  | JSON    | Alta         | Muito Alta    | Boa       | Crescendo    |

---

## 6️⃣ Verbos HTTP
Definem o tipo de ação no servidor:

| Verbo   | Função                  | Exemplo                         |
|---------|-------------------------|---------------------------------|
| GET     | Ler dados               | Buscar lista de usuários        |
| POST    | Criar dados             | Cadastrar novo usuário          |
| PUT     | Atualizar tudo          | Substituir informações          |
| PATCH   | Atualizar parcialmente  | Alterar só um campo             |
| DELETE  | Apagar dados            | Remover um registro             |

**Dicas:**
- GET é seguro (não altera dados)  
- POST, PUT, PATCH e DELETE alteram o servidor  
- Sempre conferir `status_code` da resposta (200 = sucesso, 404 = não encontrado)

---

## 7️⃣ Conclusão Geral
- ✅ Desenvolvimento Web é a base de qualquer sistema moderno conectado à internet  
- ✅ FRONT-END cuida da aparência, BACK-END cuida da lógica  
- ✅ APIs fazem a ponte entre eles  
- ✅ REST é o padrão mais usado hoje  
- ✅ Verbos HTTP controlam o fluxo de comunicação

---

## 8️⃣ Exemplo final de ciclo completo
1. Usuário acessa o site e clica em "Cadastrar"  
2. Front-end envia **POST** com os dados do formulário  
3. Back-end recebe, valida e grava no banco  
4. Servidor responde com mensagem JSON (`"Usuário criado com sucesso!"`)  
5. Front-end exibe o resultado na tela  

> Esse é o ciclo básico de toda aplicação web moderna 🌐🚀

---

✍️ **Próxima aula:** [18 – Próximo Tópico](../18_boas_praticas_em_apis_restful/18_1_introducao_e_contextualizacao.md)