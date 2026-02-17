# 1 Introdução ao Flask para APIs RESTful

Este documento apresenta uma visão geral sobre o desenvolvimento de APIs utilizando o **Flask**, abordando sua história, benefícios, limitações, segurança com JWT e práticas de testes com Pytest.

---

## 📌 O que é o Flask?

O **Flask** é um microframework em Python criado para ser simples, minimalista e altamente extensível.  
Originalmente surgiu como uma brincadeira de 1º de abril, mas evoluiu para uma ferramenta poderosa e amplamente adotada no desenvolvimento web.

Por oferecer apenas o essencial, o Flask dá liberdade total ao desenvolvedor para decidir como implementar funcionalidades como:

- Acesso a banco de dados  
- Sistema de autenticação  
- Template engine (se necessário)  
- Estrutura da aplicação  

Isso o torna especialmente eficiente para a criação de **APIs RESTful**, graças à sua leveza e flexibilidade.

---

## ⚖️ Benefícios e Limitações do Flask

### ✅ Benefícios
- **Simplicidade e minimalismo**  
- **Alta flexibilidade e extensibilidade**  
- **Facilidade de integração** com outras ferramentas  
- **Leve e rápido**  
- Dá ao desenvolvedor **total controle arquitetural**

### ❌ Limitações
- Pode não ser ideal para **projetos de grande escala**  
- Recursos avançados exigem **configuração manual**  
- Não oferece tantos recursos “out-of-the-box” quanto frameworks maiores (ex: Django)

---

## 🔐 Autenticação vs Autorização

A segurança de uma API RESTful depende de dois conceitos fundamentais:

### **Autenticação**
Verifica **quem é o usuário**.  
Exemplos:
- Usuário e senha  
- Token de acesso  
- OAuth  
- Biometria  

### **Autorização**
Define **o que o usuário pode fazer** após ser autenticado.  
Exemplos:
- Usuário comum tem acesso limitado  
- Administrador possui permissões ampliadas  

> **Autenticação:** Quem é você?  
> **Autorização:** O que você pode fazer?

---

## 🔑 JWT (JSON Web Tokens)

O **JWT** é um padrão (RFC 7519) para transmissão segura de informações entre duas partes através de um JSON criptografado ou assinado.

### Características do JWT
- **Compacto:** pode ser enviado pelo header HTTP, POST body ou URL  
- **Autocontido:** contém todas as informações necessárias sobre o usuário  
- Ideal para APIs **stateless**, pois elimina a necessidade de sessão no servidor

---

## 🧪 Testes em APIs RESTful com Flask

Garanta qualidade e segurança usando dois tipos principais de testes:

### **Testes Unitários**
- Focam em partes pequenas e isoladas do código  
- Rápidos de criar e executar  
- Ajudam a identificar erros cedo  

### **Testes de Integração**
- Verificam o funcionamento de múltiplos componentes juntos  
- Garantem consistência da API como um todo  

---

## 🧰 Pytest: Framework de Testes em Python

O **Pytest** é amplamente utilizado devido à sua simplicidade e poder.

### Vantagens do Pytest
- Sintaxe simples e intuitiva  
- Suporte a **parametrização de testes**  
- Sistema robusto de **fixtures**  
- Grande ecossistema de plugins  

---

## 📘 Conclusão

O Flask é uma excelente escolha para desenvolver APIs RESTful por ser leve, flexível e fácil de aprender.  
Combinado com boas práticas de autenticação, autorização, JWT e testes com Pytest, é possível construir aplicações robustas, seguras e escaláveis.