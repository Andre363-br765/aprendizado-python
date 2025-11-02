# 16_1_variaveis_de_classe_e_variaveis_de_instancia.py
# --------------------------
# Aula 16.1 – Variáveis de Classe e Variáveis de Instância
# --------------------------

# Em Python, os atributos podem ser:
# - Variáveis de instância → pertencem a cada objeto individualmente.
# - Variáveis de classe → pertencem à classe e são compartilhadas por todos os objetos.

class Pessoa:
    especie = "Humano"  # variável de classe (compartilhada)

    def __init__(self, nome, idade):
        self.nome = nome        # variável de instância
        self.idade = idade      # variável de instância

# Criando dois objetos
p1 = Pessoa("Ana", 25)
p2 = Pessoa("Carlos", 30)

# Atributos de instância (diferentes para cada objeto)
print(p1.nome, "-", p1.idade)
print(p2.nome, "-", p2.idade)

# Atributo de classe (igual para todos)
print(p1.especie)
print(p2.especie)

# Alterando o valor de classe
Pessoa.especie = "Ser Humano"

print(p1.especie)
print(p2.especie)

# Podemos também adicionar atributos de instância individualmente
p1.profissao = "Engenheira"
print(p1.profissao)
# print(p2.profissao)  # Erro: p2 não tem esse atributo

# Resumo:
# - Variáveis de instância → exclusivas de cada objeto.
# - Variáveis de classe → compartilhadas por todos.
# - Úteis para valores comuns (como contadores, categorias, tipos, etc).

# =========================================================================
# =========================================================================
# =========================================================================

# --------------------------
# Aula 16.2 – Métodos de Classe e Métodos Estáticos
# --------------------------

# Em Python existem três tipos de métodos:
# - Métodos de instância → usam 'self' e afetam apenas o objeto.
# - Métodos de classe → usam 'cls' e afetam a classe como um todo.
# - Métodos estáticos → não usam nem 'self' nem 'cls'; funcionam como funções dentro da classe.

class Conta:
    taxa_juros = 0.05  # variável de classe

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    # Método de instância (usa self)
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado por {self.titular}. Saldo: R$ {self.saldo:.2f}")

    # Método de classe (usa cls)
    @classmethod
    def alterar_taxa(cls, nova_taxa):
        cls.taxa_juros = nova_taxa
        print(f"Taxa de juros alterada para {cls.taxa_juros * 100:.1f}%")

    # Método estático (não usa self nem cls)
    @staticmethod
    def converter_moeda(valor, cotacao):
        return valor * cotacao


# Usando os métodos:
conta1 = Conta("Ana", 1000)
conta2 = Conta("Bruno", 2000)

conta1.depositar(500)

# Método de classe → afeta todas as instâncias
Conta.alterar_taxa(0.07)
print("Taxa atual:", Conta.taxa_juros)

# Método estático → executa função independente
valor_em_dolar = Conta.converter_moeda(100, 0.18)
print(f"R$100 equivalem a ${valor_em_dolar:.2f}")

# Resumo:
# - @classmethod → atua sobre a classe (acessa atributos de classe).
# - @staticmethod → executa funções auxiliares dentro da classe.
# - Método comum → atua sobre o objeto (usa self).

# =========================================================================
# =========================================================================
# =========================================================================

# --------------------------
# Aula 16.3 – O que são Interfaces
# --------------------------

# Em Programação Orientada a Objetos, uma INTERFACE define um "contrato".
# Ela especifica quais métodos uma classe deve ter, mas não define como eles funcionam.

# Python não tem interfaces formais como Java ou C#, mas podemos simular isso de duas formas:
# 1. Usando classes base abstratas (ABC)
# 2. Usando convenções (criar métodos que as subclasses DEVEM sobrescrever)

# Exemplo 1 – Interface simulada por convenção:

class Forma:
    def area(self):
        raise NotImplementedError("A subclasse deve implementar o método area().")

    def perimetro(self):
        raise NotImplementedError("A subclasse deve implementar o método perimetro().")


# Criando classes que seguem o "contrato" da interface Forma
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        import math
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        import math
        return 2 * math.pi * self.raio


# Testando as classes
formas = [
    Retangulo(10, 5),
    Circulo(7)
]

for f in formas:
    print(f"{f.__class__.__name__}: Área = {f.area():.2f}, Perímetro = {f.perimetro():.2f}")


# Exemplo 2 – Usando ABC (Abstract Base Class)
# Isso veremos em detalhes na aula 16.5 (Classes Abstratas),
# mas aqui vai uma prévia de como ela também representa uma interface:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"


class Gato(Animal):
    def fazer_som(self):
        return "Miau!"


animais = [Cachorro(), Gato()]
for a in animais:
    print(f"{a.__class__.__name__} diz: {a.fazer_som()}")

# --------------------------
# Resumo:
# --------------------------
# - Interfaces definem o que uma classe deve fazer, mas não como.
# - Servem como um "contrato" entre classes.
# - Em Python, usamos:
#   → Convenções (métodos com NotImplementedError)
#   → Ou classes abstratas (com ABC e @abstractmethod)
# - Isso ajuda na padronização e facilita substituição de classes sem quebrar o código.

# =========================================================================
# =========================================================================
# =========================================================================

# --------------------------
# Aula 16.4 – O que é Abstração
# --------------------------

# Abstração é o processo de esconder detalhes complexos e mostrar apenas o que é essencial.
# Em POO, usamos abstração para simplificar o uso de classes e objetos,
# mantendo o foco apenas no comportamento importante.

# Exemplo 1 – Sem abstração (mostrando tudo)
class Motor:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print("Motor ligado.")

    def desligar(self):
        self.ligado = False
        print("Motor desligado.")


class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor()

    # Aqui aplicamos a abstração:
    # O usuário só precisa saber que existe o método "ligar" e "desligar" o carro,
    # sem se preocupar com o funcionamento interno do motor.
    def ligar(self):
        self.motor.ligar()
        print(f"{self.modelo} está pronto para andar.")

    def desligar(self):
        self.motor.desligar()
        print(f"{self.modelo} foi desligado.")


# Testando
carro = Carro("Fusca")
carro.ligar()
carro.desligar()

# O usuário interage com o carro, mas não precisa saber nada sobre a classe Motor.


# Exemplo 2 – Abstraindo comportamentos com herança
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def trabalhar(self):
        raise NotImplementedError("O método trabalhar() deve ser implementado pela subclasse.")


class Engenheiro(Funcionario):
    def trabalhar(self):
        return f"{self.nome} está projetando um sistema."


class Professor(Funcionario):
    def trabalhar(self):
        return f"{self.nome} está dando aula."


# O código abaixo funciona sem precisar saber os detalhes de cada tipo de funcionário
funcionarios = [
    Engenheiro("Ana", 8000),
    Professor("Carlos", 5000)
]

for f in funcionarios:
    print(f.trabalhar())

# --------------------------
# Resumo:
# --------------------------
# - Abstração → esconder detalhes e mostrar apenas o essencial.
# - Permite simplificar o uso de objetos.
# - Em Python, é feita por:
#   → Encapsulamento (ocultar atributos/métodos internos)
#   → Herança e Polimorfismo (reutilizar e generalizar comportamentos)
# - É um dos pilares da POO (junto com encapsulamento, herança e polimorfismo).

# =========================================================================
# =========================================================================
# =========================================================================

# --------------------------
# Aula 16.5 – Classes Abstratas
# --------------------------

# Classes abstratas servem como "modelos" para outras classes.
# Elas não podem ser instanciadas diretamente, apenas suas subclasses.
# Definem métodos que obrigatoriamente devem ser implementados nas subclasses.

from abc import ABC, abstractmethod

# Criando uma classe abstrata
class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


# Tentativa de instanciar gera erro:
# v = Veiculo()  # Erro: não se pode instanciar uma classe abstrata

# Criando subclasses que implementam os métodos abstratos
class Carro(Veiculo):
    def ligar(self):
        print("Carro ligado. Vamos rodar!")

    def desligar(self):
        print("Carro desligado. Até logo!")


class Moto(Veiculo):
    def ligar(self):
        print("Moto ligada. Vamos acelerar!")

    def desligar(self):
        print("Moto desligada. Até a próxima!")


# Testando
veiculos = [Carro(), Moto()]

for v in veiculos:
    v.ligar()
    v.desligar()

# --------------------------
# Resumo:
# --------------------------
# - Classes abstratas → não podem ser instanciadas.
# - Servem como modelo/contrato para subclasses.
# - Forçam a implementação de métodos obrigatórios.
# - Em Python usamos:
#   → ABC (Abstract Base Class)
#   → @abstractmethod para definir métodos que devem ser implementados.
# - Útil para garantir padronização e evitar inconsistências nas subclasses.

# =========================================================================
# =========================================================================
# =========================================================================