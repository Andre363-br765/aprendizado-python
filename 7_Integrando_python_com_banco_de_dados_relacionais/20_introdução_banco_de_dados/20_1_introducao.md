# Aula 20.1 – Introdução a Banco de Dados

## 📘 Introdução ao módulo
A partir desta seção, aprenderemos a integrar o **Python** com **bancos de dados**, entendendo desde os conceitos fundamentais até como manipular dados com **SQL**.

Um **banco de dados** é essencial em praticamente qualquer aplicação moderna, pois é onde ficam armazenadas as informações — como usuários, produtos, transações, registros de login e muito mais.

---

## 🧩 O que é um Banco de Dados?
Um **Banco de Dados (Database)** é um sistema organizado para armazenar, gerenciar e acessar informações de forma estruturada.

Ele permite que programas (como os feitos em Python) possam **salvar e consultar dados de forma eficiente**, sem depender de arquivos manuais.

### Exemplos de bancos de dados populares:
- MySQL  
- PostgreSQL  
- SQLite  
- SQL Server  
- Oracle Database  

No Python, a integração é feita por meio de **conectores ou bibliotecas específicas**, como:
- `sqlite3`
- `psycopg2`
- `pyodbc`
- `sqlalchemy`

---

## 💡 Por que usar um Banco de Dados?
- Para armazenar informações de forma **persistente** (mesmo após fechar o programa)  
- Para **facilitar buscas e filtros de dados**  
- Para manter **segurança e integridade** das informações  
- Para permitir **múltiplos acessos simultâneos**

### Exemplo prático:
Imagine um sistema de cadastro de alunos.  
Com um banco de dados, é possível:
- Cadastrar novos alunos  
- Atualizar informações  
- Pesquisar alunos específicos  
- Remover registros antigos  

---

## 🧱 Tipos de Bancos de Dados

### 1️⃣ Bancos de Dados Relacionais (SQL)
- Armazenam dados em **tabelas** (linhas e colunas)  
- Usam a linguagem **SQL (Structured Query Language)**  
- Exemplos: MySQL, PostgreSQL, SQL Server, SQLite  

### 2️⃣ Bancos de Dados Não Relacionais (NoSQL)
- Armazenam dados de forma **flexível** (documentos, chaves, grafos, etc.)  
- Exemplos: MongoDB, Redis, Cassandra  

> 💬 **Neste módulo**, o foco será em **bancos de dados relacionais**, pois são os mais usados em sistemas de negócios e servem como base para compreender qualquer tipo de banco.

---

## 🧾 Conclusão
- Um banco de dados é o **coração da maioria das aplicações modernas**.  
- Ele permite **armazenar, consultar e manipular dados com segurança**.  
- O **Python** possui diversas ferramentas para trabalhar com bancos de dados.  

✍️ **Próxima aula:** [20 – Próximo Tópico](20_2_banco_de_dados.md)