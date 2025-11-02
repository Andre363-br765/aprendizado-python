# --------------------------
# Aula 16.6 – Resumo Completo da Aula 16
# --------------------------

# Aula 16: POO Avançada – Conceitos principais
# Inclui:
# - Variáveis de instância e de classe
# - Métodos de instância, classe e estático
# - Interfaces
# - Abstração
# - Classes abstratas

# --------------------------
# 1. Variáveis de instância vs variáveis de classe
# --------------------------
class Pessoa:
    especie = "Humano"  # variável de classe

    def __init__(self, nome, idade):
        self.nome = nome    # variável de instância
        self.idade = idade  # variável de instância


# --------------------------
# 2. Métodos de instância, classe e estático
# --------------------------
class Conta:
    taxa_juros = 0.05  # variável de classe

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):  # método de instância
        self.saldo += valor
        print(f"{self.titular} depositou R${valor}. Saldo: R${self.saldo}")

    @classmethod
    def alterar_taxa(cls, nova_taxa):  # método de classe
        cls.taxa_juros = nova_taxa

    @staticmethod
    def converter_moeda(valor, cotacao):  # método estático
        return valor * cotacao


# --------------------------
# 3. Interfaces (contratos)
# --------------------------
class Forma:
    def area(self):
        raise NotImplementedError("Subclasse deve implementar area()")

    def perimetro(self):
        raise NotImplementedError("Subclasse deve implementar perimetro()")


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


# --------------------------
# 4. Abstração
# --------------------------
class Motor:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False


class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor()

    def ligar(self):
        self.motor.ligar()
        print(f"{self.modelo} ligado!")

    def desligar(self):
        self.motor.desligar()
        print(f"{self.modelo} desligado!")


# --------------------------
# 5. Classes abstratas
# --------------------------
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Moto(Veiculo):
    def ligar(self):
        print("Moto ligada!")

    def desligar(self):
        print("Moto desligada!")


# --------------------------
# Resumo final:
# --------------------------
# - Variáveis de instância → exclusivas de cada objeto
# - Variáveis de classe → compartilhadas por todos os objetos
# - Métodos de instância → agem sobre o objeto (self)
# - Métodos de classe → agem sobre a classe (cls)
# - Métodos estáticos → funções internas da classe, sem self nem cls
# - Interfaces → definem contrato de métodos obrigatórios
# - Abstração → esconde detalhes complexos, mostra só o essencial
# - Classes abstratas → modelo que obriga implementação de métodos nas subclasses
