# 20_3 - Explorando Banco de Dados Relacionais com Python DB API

## 20_3_1 - Introdução aos Bancos de Dados Relacionais

Bancos de dados relacionais armazenam informações de forma estruturada, usando **tabelas** compostas por **linhas (registros)** e **colunas (atributos)**.

### Conceitos principais
- **Tabela**: representa uma entidade (ex: alunos, produtos).
- **Linha (row)**: cada registro da tabela.
- **Coluna (column)**: cada atributo do registro.
- **Chave primária (Primary Key)**: identifica unicamente cada registro.
- **Chave estrangeira (Foreign Key)**: relaciona tabelas diferentes.
- **Integridade referencial**: garante consistência entre tabelas relacionadas.

### Exemplos de SGBDs
- **SQLite**
- **MySQL / MariaDB**
- **PostgreSQL**
- **SQL Server**

---

## 20_3_2 - Conectando com o Banco de Dados

### Criando uma Conexão
```python
import sqlite3

conn = sqlite3.connect("academia.db")
cursor = conn.cursor()
```
### Criando uma Tabela
```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
)
""")
conn.commit()
```

### Inserindo Registros
```python
cursor.execute(
    "INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)",
    ("Ana", 22, "Python")
)
conn.commit()
```
## 20_3_3 - Manipulação de Registros

### Atualizando Registros
```python
cursor.execute(
    "UPDATE alunos SET idade = ? WHERE nome = ?",
    (23, "Ana")
)
conn.commit()
```
### Removendo Registros
```python
cursor.execute(
    "DELETE FROM alunos WHERE nome = ?",
    ("Ana",)
)
conn.commit()
```
### Inserindo Registros em Lote
```python
dados = [
    ("João", 21, "Java"),
    ("Maria", 20, "C#"),
    ("Pedro", 25, "Python")
]

cursor.executemany(
    "INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)",
    dados
)
conn.commit()
```
### Consultando os Registros
```python
cursor.execute("SELECT * FROM alunos")
for row in cursor.fetchall():
    print(row)
```
### Consultando com Filtro
```python
cursor.execute("SELECT * FROM alunos WHERE idade > ?", (21,))
for aluno in cursor.fetchall():
    print(aluno)
```

### Alterando o `row_factory`

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM alunos")
for row in cursor.fetchall():
    print(row["nome"], row["curso"])
```

## 20_3_4 - Boas Práticas

- Sempre fechar **cursor** e **conexão**:
```python
cursor.close()
conn.close()
```

- Use placeholders (?) para evitar SQL Injection

- Nomeie tabelas e colunas de forma clara

- Evite duplicidade de dados

- Documente seu código

### Gerenciando Transações

```python
try:
    cursor.execute(
        "INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)",
        ("Lucas", 24, "Go")
    )
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Erro ao inserir:", e)
```

✍️ **Próxima aula:** [20 – Próximo Tópico](20_4_banco_de_dados.md)