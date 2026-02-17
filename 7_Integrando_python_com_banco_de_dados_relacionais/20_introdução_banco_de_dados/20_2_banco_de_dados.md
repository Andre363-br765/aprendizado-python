# Aula 20.2 – Banco de Dados

Nesta aula, vamos entender os **tipos de bancos de dados**, o **conceito de tabelas**, os **tipos de dados**, o que é um **DBMS** e como **instalar o SQL Server**.

---

## 🧠 20.2.1 – Tipos de Banco de Dados

Existem dois grandes grupos de bancos de dados:

### 🔹 Relacionais (SQL)
- Armazenam os dados em **tabelas** (linhas e colunas).  
- Usam a linguagem **SQL (Structured Query Language)**.  
- São ideais quando há **relações claras entre dados**.

**Exemplos:**  
`MySQL`, `PostgreSQL`, `SQLite`, `SQL Server`, `Oracle`.

---

### 🔹 Não Relacionais (NoSQL)
- Não utilizam tabelas.  
- Armazenam dados de forma mais **flexível**, em formatos diferentes:  
  - **Documentos** → *MongoDB*  
  - **Chave-valor** → *Redis*  
  - **Colunas** → *Cassandra*  
  - **Grafos** → *Neo4j*  

Usados em **aplicações modernas** e **escaláveis**, como redes sociais ou sistemas de recomendação.

---

## 🧩 20.2.2 – Entendendo uma Tabela

Em um banco de dados relacional, os dados são armazenados em **tabelas**.

Cada tabela possui:
- **Colunas** → campos ou atributos  
- **Linhas** → registros ou tuplas  

Exemplo de tabela de usuários:

| id_usuario | nome  | idade |
|-------------|-------|-------|
| 1 | Ana | 25 |
| 2 | João | 30 |
| 3 | Carla | 22 |

Cada **coluna** define um **tipo de dado**, e cada **linha** representa um **registro** individual.

---

## 🔢 20.2.3 – Tipos de Dados em Bancos Relacionais

Os tipos de dados mais comuns são:

| Tipo | Descrição |
|------|------------|
| `INT` | Números inteiros |
| `FLOAT / DOUBLE` | Números decimais |
| `CHAR / VARCHAR` | Texto (fixo ou variável) |
| `DATE / DATETIME` | Datas e horários |
| `BOOLEAN` | Verdadeiro ou falso |

**Exemplo de criação de tabela em SQL:**

```sql
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY,
    nome VARCHAR(50),
    idade INT,
    email VARCHAR(100),
    ativo BOOLEAN
);
```
---

## ⚙️ 20.2.4 – Entendendo o DBMS

**DBMS (Database Management System)**  
→ *Sistema de Gerenciamento de Banco de Dados.*

É o software responsável por **criar, gerenciar e permitir o acesso aos dados**.

### 🔹 Principais funções:
- Criar e administrar bancos de dados.  
- Controlar usuários e permissões.  
- Garantir integridade e segurança.  
- Executar comandos SQL.

### 💾 Exemplos de DBMS:
MySQL, PostgreSQL, SQLite, SQL Server, Oracle Database.

---

## 🧰 20.2.5 – Instalando o SQL Server

O **SQL Server** é um dos DBMS mais usados no mercado corporativo.

### 🔧 Etapas de instalação:

1️⃣ Acesse o site oficial da Microsoft:  
👉 [https://www.microsoft.com/pt-br/sql-server/sql-server-downloads](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads)

2️⃣ Baixe a versão **SQL Server Developer (gratuita)**.

3️⃣ Instale também o **SQL Server Management Studio (SSMS)** para gerenciar bancos graficamente.

4️⃣ Após instalar, você poderá:
- Criar bancos de dados.  
- Executar comandos SQL.  
- Inserir, atualizar e consultar dados.
---
## 💻 Exemplo rápido de comandos SQL
```sql
-- Criar um novo banco de dados
CREATE DATABASE escola;

-- Usar o banco
USE escola;

-- Criar tabela alunos
CREATE TABLE alunos (
    id_aluno INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    curso VARCHAR(100)
);

-- Inserir registros
INSERT INTO alunos (id_aluno, nome, idade, curso)
VALUES (1, 'Marcos', 20, 'Engenharia'),
       (2, 'Lívia', 22, 'Direito');

-- Consultar dados
SELECT * FROM alunos;
```
---

# 🧾 Resumo

- **Bancos relacionais** usam **tabelas** e **SQL**.  
- **Bancos não relacionais** usam **estruturas flexíveis**.  
- O **DBMS** é o sistema que **gerencia o banco de dados**.  
- O **SQL Server** é um dos **DBMS mais populares e poderosos**.

✍️ **Próxima aula:** [20 – Próximo Tópico](20_3_banco_de_dados.md)