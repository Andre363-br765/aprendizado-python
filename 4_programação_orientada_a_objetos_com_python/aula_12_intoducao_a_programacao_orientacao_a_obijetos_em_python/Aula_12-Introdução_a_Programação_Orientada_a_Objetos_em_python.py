# =================================================================================
# =================================================================================
# =================================================================================

# 12_1_o_que_e_orientacao_objeto.py
# --------------------------
# Aula 12.1 – O que é Orientação a Objetos (OOP) em Python
# --------------------------

# Orientação a Objetos é um paradigma de programação
# que organiza o código em objetos. Cada objeto contém:
# - Dados (atributos)
# - Comportamentos (métodos)

# Vantagens da OOP:
# 1. Modularidade: objetos independentes e organizados
# 2. Reutilização: classes podem ser reutilizadas em diferentes projetos
# 3. Manutenção facilitada: alterações em um objeto não afetam outros
# 4. Representação natural do mundo real: modela conceitos do dia a dia

# Exemplo conceitual:

# Classe Carro → define atributos e comportamentos
# Atributos: marca, cor, ano
# Métodos: acelerar(), frear()

# Objeto meu_carro → instância da classe Carro
# Valores específicos: marca="Toyota", cor="Preto", ano=2020

# Resumindo:
# Classe = molde / Objeto = instância real da classe
# OOP permite criar modelos claros, reutilizáveis e próximos da realidade

# =================================================================================
# =================================================================================
# =================================================================================

# 12_2_conceitos_classe_e_objeto.py
# --------------------------
# Aula 12.2 – Conceitos de Classe e Objeto
# --------------------------

# Classe: é um molde ou "projeto" que define características e comportamentos de um objeto
# Objeto: é uma instância da classe, ou seja, um item criado a partir da classe

# Atributos: representam dados/propriedades do objeto
# Métodos: representam comportamentos/funções do objeto

# Exemplo prático de classe
class Carro:
    """Classe que representa um carro"""
    def __init__(self, marca, cor, ano):
        self.marca = marca  # atributo
        self.cor = cor
        self.ano = ano

    def acelerar(self):  # método
        print(f"O {self.marca} está acelerando!")

    def frear(self):
        print(f"O {self.marca} está freando!")

# Criando objetos (instâncias da classe)
meu_carro = Carro("Toyota", "Preto", 2020)
outro_carro = Carro("Honda", "Vermelho", 2022)

# Acessando atributos
print(f"Meu carro: {meu_carro.marca}, {meu_carro.cor}, {meu_carro.ano}")
print(f"Outro carro: {outro_carro.marca}, {outro_carro.cor}, {outro_carro.ano}")

# Chamando métodos
meu_carro.acelerar()
outro_carro.frear()

# Resumo:
# - Classe define o molde
# - Objeto é a instância
# - Atributos armazenam dados
# - Métodos armazenam comportamentos

# =================================================================================
# =================================================================================
# =================================================================================

# 12_3_criando_orientacao_objeto.py
# --------------------------
# Aula 12.3 – Criando Orientação a Objetos em Python
# --------------------------

# Criando uma classe completa com atributos e métodos
class Pessoa:
    """Classe que representa uma pessoa"""
    def __init__(self, nome, idade, profissao):
        self.nome = nome        # atributo
        self.idade = idade      # atributo
        self.profissao = profissao  # atributo

    def apresentar(self):
        """Exibe uma apresentação da pessoa"""
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.")

    def aniversario(self):
        """Aumenta a idade da pessoa em 1 ano"""
        self.idade += 1
        print(f"Feliz aniversário, {self.nome}! Agora você tem {self.idade} anos.")

# Criando objetos da classe Pessoa
p1 = Pessoa("Ana", 25, "Engenheira")
p2 = Pessoa("Bruno", 30, "Professor")

# Chamando métodos
p1.apresentar()
p2.apresentar()

# Chamando método para aniversário
p1.aniversario()
p2.aniversario()

# Acessando atributos diretamente
print(f"{p1.nome} tem {p1.idade} anos.")
print(f"{p2.nome} tem {p2.idade} anos.")

# Resumo:
# - __init__ define os atributos iniciais
# - Métodos definem comportamentos
# - Objetos são instâncias da classe e podem usar os métodos e atributos
# - Podemos modificar atributos diretamente ou via métodos

# =================================================================================
# =================================================================================
# =================================================================================

# 12_4_construtores_e_destrutores.py
# --------------------------
# Aula 12.4 – Construtores e Destrutores em Python
# --------------------------

# Construtor (__init__):
# - É chamado automaticamente quando um objeto é criado
# - Inicializa os atributos do objeto

# Destrutor (__del__):
# - É chamado quando o objeto é destruído ou sai de escopo
# - Pode ser usado para limpeza ou mensagens de confirmação

class Pessoa:
    """Classe que representa uma pessoa"""
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Objeto Pessoa criado: {self.nome}, {self.idade} anos")

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

    def __del__(self):
        print(f"Objeto Pessoa {self.nome} destruído!")

# Criando objetos
p1 = Pessoa("Ana", 25)
p2 = Pessoa("Bruno", 30)

# Chamando métodos
p1.apresentar()
p2.apresentar()

# Deletando objetos manualmente
del p1
del p2

# Observações:
# - O Python destrói automaticamente objetos sem referência
# - O destrutor é útil para liberar recursos externos (arquivos, conexões)

# Resumo:
# - __init__ inicializa o objeto e seus atributos
# - __del__ executa ações de limpeza ao destruir o objeto
# - Construtores e destrutores ajudam no gerenciamento de recursos


# =================================================================================
# =================================================================================
# =================================================================================

# 12_5_desafio_e_resposta.py
# --------------------------
# Aula 12.5 – Desafio e Resposta: Classe Produto
# --------------------------

# Desafio:
# 1. Criar uma classe Produto com atributos: nome, preço e quantidade
# 2. Criar método para calcular valor total (preço * quantidade)
# 3. Criar pelo menos dois objetos da classe
# 4. Exibir resumo dos produtos com valor total

# --------------------------
# Resolução do Desafio
# --------------------------

class Produto:
    """Classe que representa um produto"""
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        """Calcula o valor total do produto (preço * quantidade)"""
        return self.preco * self.quantidade

# Criando objetos da classe Produto
p1 = Produto("Caneta", 2.5, 100)
p2 = Produto("Caderno", 15.0, 50)

# Lista de produtos
produtos = [p1, p2]

# Exibindo resumo dos produtos
print("📦 Resumo dos Produtos:")
for p in produtos:
    print(f"- {p.nome}: {p.quantidade} unidades a R$ {p.preco:.2f} cada → Total: R$ {p.valor_total():.2f}")

# Saída esperada:
# - Caneta: 100 unidade

# =================================================================================
# =================================================================================
# =================================================================================

# 12_6_resumo.py
# --------------------------
# Aula 12.6 – Resumo Completo da Aula 12 (OOP)
# --------------------------

# 1. O que é Orientação a Objetos (OOP)
# - Paradigma de programação que organiza código em objetos
# - Cada objeto possui atributos (dados) e métodos (comportamentos)
# - Vantagens: modularidade, reutilização, manutenção facilitada, representação do mundo real

# 2. Conceitos de Classe e Objeto
# - Classe: molde ou projeto
# - Objeto: instância da classe
# - Atributos: armazenam dados do objeto
# - Métodos: definem comportamentos do objeto

# Exemplo:
# class Carro:
#     def __init__(self, marca, cor):
#         self.marca = marca
#         self.cor = cor
#     def acelerar(self):
#         print(f"O {self.marca} está acelerando!")
# meu_carro = Carro("Toyota", "Preto")
# meu_carro.acelerar()

# 3. Criando Orientação a Objetos
# - Definir classes completas com atributos e métodos
# - Criar objetos e acessar seus métodos e atributos
# - Usar métodos para encapsular ações e cálculos

# Exemplo:
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos")
# p = Pessoa("Ana", 25)
# p.apresentar()

# 4. Construtores e Destrutores
# - __init__(): chamado ao criar objeto, inicializa atributos
# - __del__(): chamado ao destruir objeto, útil para liberar recursos
# - Permite controle do ciclo de vida do objeto

# Exemplo:
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
#         print(f"{self.nome} criado!")
#     def __del__(self):
#         print(f"{self.nome} destruído!")
# p = Pessoa("Bruno")
# del p

# 5. Desafio resolvido: Classe Produto
# - Criar classe com atributos: nome, preço, quantidade
# - Método para calcular valor total
# - Criar objetos e exibir resumo

# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade = quantidade
#     def valor_total(self):
#         return self.preco * self.quantidade
# p1 = Produto("Caneta", 2.5, 100)
# p2 = Produto("Caderno", 15.0, 50)
# produtos = [p1, p2]
# for p in produtos:
#     print(f"{p.nome}: {p.quantidade} unidades → Total: R$ {p.valor_total():.2f}")

# 6. Boas práticas em OOP
# - Nomeação clara de classes e métodos
# - Docstrings em classes e métodos
# - Evitar repetição de código (DRY)
# - Usar métodos para cálculos e ações
# - Criar objetos como instâncias da classe
# - Organizar código em módulos e arquivos separados

# --------------------------
# Aula 12 resumida:
# - OOP facilita a organização do código e a manutenção
# - Classes e objetos permitem modelar conceitos reais
# - Construtores e destrutores controlam o ciclo de vida
# - Métodos encapsulam comportamentos
# - Desafios ajudam a fixar conceitos