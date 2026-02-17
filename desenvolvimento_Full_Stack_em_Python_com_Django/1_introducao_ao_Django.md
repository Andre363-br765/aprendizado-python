# 📘 1 – Introdução ao Django

## 🏛️ História e Propósito do Django

O **Django** é um framework web de alto nível escrito em Python, criado para facilitar e acelerar o desenvolvimento de aplicações web completas, escaláveis e seguras.

Ele foi desenvolvido por **Adrian Holovaty** e **Simon Willison** durante seu trabalho no jornal *Lawrence Journal-World*. O framework foi lançado oficialmente em **2005** pela **Django Software Foundation (DSF)**.

A motivação original do Django era permitir que desenvolvedores focassem na **lógica de negócio** enquanto o framework cuidava das partes repetitivas e estruturais.

O nome *Django* homenageia o músico de jazz **Django Reinhardt**, representando a proposta do framework de ser rápido, elegante e eficiente.

---

## ✅ Benefícios do Django

### **Produtividade elevada**

O Django oferece vários recursos prontos, como:

* Sistema de autenticação
* Painel administrativo automático
* Validação e geração de formulários
* ORM integrado
* Ferramentas de segurança
* Estrutura organizada baseada em boas práticas

Isso acelera o desenvolvimento e reduz tarefas repetitivas.

### **Forte foco em segurança**

O framework implementa proteções padrão contra:

* SQL Injection
* CSRF (Cross-Site Request Forgery)
* XSS (Cross-Site Scripting)
* Clickjacking

Assim, aplicativos web podem ser mais seguros desde o início.

### **Comunidade ativa**

A comunidade Django é grande, experiente e contribui com:

* Documentação extensa
* Tutoriais
* Pacotes externos
* Suporte e atualizações constantes

---

## ⚠️ Limitações do Django

### **Curva de aprendizado inicial**

O Django segue uma estrutura própria, que pode ser desafiadora para iniciantes, especialmente ao lidar com:

* ORM
* Templates
* Arquitetura MTV
* Convenções internas

### **Pode ser exagerado para projetos pequenos**

Sistemas muito simples podem ficar mais complexos do que o necessário devido:

* ao tamanho do framework
* à estrutura obrigatória
* às camadas internas

### **Menos flexível**

Como segue a filosofia *“Django Way”*, o framework funciona muito bem dentro de sua proposta, mas limita escolhas para projetos que precisam de arquiteturas altamente personalizadas.

### **Não é ideal para aplicações em tempo real**

Por ser **síncrono** por padrão, não é a melhor escolha para:

* chats
* sistemas multiplayer
* plataformas de streaming

(Django Channels existe, mas ainda não é tão leve quanto alternativas como FastAPI ou Node.js.)