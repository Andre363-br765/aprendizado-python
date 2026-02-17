# aula_12_resumo.py
# --------------------------
# Aula 12 – Introdução à Programação Orientada a Objetos (OOP) em Python
# --------------------------

# --------------------------
# 12.1 O que é Orientação a Objetos
# --------------------------
# Orientação a Objetos (OOP) é um paradigma de programação
# que organiza o código em **objetos**, cada um contendo **dados** e **comportamentos**.

# Principais vantagens:
# - Modularidade: objetos independentes
# - Reutilização de código: classes podem ser reutilizadas
# - Facilidade de manutenção e expansão
# - Representação natural do mundo real

# --------------------------
# 12.2 Conceitos de Classe e Objeto
# --------------------------
# Classe: molde ou “projeto” de um objeto
# Objeto: instância de uma classe

# Exemplo conceitual:
# Classe Carro → define características (marca, cor, ano) e comportamentos (acelerar, frear)
# Objeto meu_carro = Carro() → instância real com valores específicos

# --------------------------
# 12.3 Criando Orientação a Objetos
# --------------------------
# Definindo uma classe
class Carro:
    """Classe que representa um carro"""
    def __init__(self, marca, cor, ano):
        self.marca = marca  # atributo de instância
        self.cor = cor
        self.ano = ano
    
    # Método da classe
    def acelerar(self):
        print(f"O {self.marca} está acelerando!")

    def frear(self):
        print(f"O {self.marca} está freando!")

# Criando objetos (instâncias da classe)
meu_carro = Carro("Toyota", "Preto", 2020)
outro_carro = Carro("Honda", "Vermelho", 2022)

meu_carro.acelerar()
outro_carro.frear()

# --------------------------
# 12.4 Construtores e Destrutores
# --------------------------
# Construtor: método __init__, chamado ao criar o objeto
# Destrutor: método __del__, chamado quando o objeto é destruído

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Objeto Pessoa criado: {self.nome}, {self.idade} anos")
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
    
    def __del__(self):
        print(f"Objeto Pessoa {self.nome} destruído!")

p1 = Pessoa("Ana", 25)
p1.apresentar()
del p1  # destrói o objeto e chama __del__

# --------------------------
# 12.5 Desafio e Resposta
# --------------------------
# Desafio:
# 1. Criar uma classe Produto com atributos: nome, preço, quantidade
# 2. Criar métodos para calcular valor total (preço * quantidade)
# 3. Criar pelo menos dois objetos da classe
# 4. Exibir resumo dos produtos com valor total

# Resolução
class Produto:
    """Classe que representa um produto"""
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def valor_total(self):
        """Retorna o valor total do produto (preco * quantidade)"""
        return self.preco * self.quantidade

# Criando objetos
p1 = Produto("Caneta", 2.5, 100)
p2 = Produto("Caderno", 15.0, 50)

# Exibindo resumo
produtos = [p1, p2]
print("\n📦 Resumo dos Produtos:")
for p in produtos:
    print(f"- {p.nome}: {p.quantidade} unidades a R$ {p.preco:.2f} cada → Total: R$ {p.valor_total():.2f}")

# --------------------------
# 12.6 Resumo da Aula 12
# --------------------------
# - OOP organiza o código em objetos (dados + comportamentos)
# - Classe = molde / Objeto = instância da classe
# - Construtores (__init__) inicializam objetos
# - Destrutores (__del__) executam limpeza ao destruir objetos
# - Métodos definem comportamentos dos objetos
# - Boas práticas:
#    * Docstrings em classes e métodos
#    * Nomeação clara
#    * Criar funções/métodos para cálculos e ações
# - Desafios ajudam a consolidar o conceito de instâncias e métodos
