# 20_4 - Integrando Python com Banco de Dados Relacionais Utilizando SQLAlchemy

O **SQLAlchemy** é uma biblioteca Python poderosa para trabalhar com bancos de dados relacionais, permitindo abstrair operações SQL e integrar com Python de forma mais limpa e segura.

## 20_4_1 - Introdução ao SQLAlchemy
- Dois principais modos de uso:
  1. **Core**: mais próximo do SQL, mas ainda com abstração.
  2. **ORM (Object Relational Mapper)**: manipula tabelas como classes e objetos Python.
- Vantagens:
  - Evita SQL Injection.
  - Facilita manutenção e leitura do código.
  - Permite transações automáticas e mapeamento de relações complexas.

## 20_4_2 - Criando a Conexão com o Banco
- Criação de engine:
```python
from sqlalchemy import create_engine
engine = create_engine("sqlite:///academia.db", echo=True)
```

## 20_4_3 - Definindo Classes ORM

- Cada tabela é representada como uma `classe Python`:

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    curso = Column(String)
```

- Criar as tabelas no banco:

```python
Base.metadata.create_all(engine)
```

2## 20_4_4 - Manipulando Dados com ORM

### Criando Sessão
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```
Inserindo Registros:
```python
novo_aluno = Aluno(nome="Ana", idade=22, curso="Python")
session.add(novo_aluno)
session.commit()
```
### Consultando Registros:
```python

alunos = session.query(Aluno).all()
for aluno in alunos:
    print(aluno.nome, aluno.curso)
```
### Atualizando Registros:
```python

aluno = session.query(Aluno).filter_by(nome="Ana").first()
aluno.idade = 23
session.commit()
```
### Removendo Registros:
```python
aluno = session.query(Aluno).filter_by(nome="Ana").first()
session.delete(aluno)
session.commit()
```
## 20_4_5 - Boas Práticas com SQLAlchemy

- Sempre fechar a sessão: `session.close()`.
- Use transações (`commit` / `rollback`) para evitar inconsistências.
- Nomeie classes e colunas de forma clara.
- Use filtros (`filter`, `filter_by`) para melhorar performance.
- Separe **modelos**, **engine** e **operações** em arquivos diferentes para organização.

---

Este resumo cobre os pontos essenciais da integração Python + SQLAlchemy, incluindo:

- Core x ORM  
- Conexão com o banco  
- Definição de tabelas via classes  
- Operações CRUD básicas  
- Boas práticas de uso  

Ele é suficiente para começar a usar SQLAlchemy sem se perder em detalhes avançados.

✍️ **Próxima aula:** [21 – Próximo Tópico](../../6_evoluindo_com_apis_assíncronas_com_fast_api/22_Manipulacao_Dados_FastAPI_Assincrono/1_Conexao_Banco_Assincrono.md)