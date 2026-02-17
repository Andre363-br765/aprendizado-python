# 13_1_heranca_em_python.py
# --------------------------
# Aula 13.1 – Herança em Python: Conceito Geral
# --------------------------

# Herança é um dos pilares da Orientação a Objetos (OOP)
# Permite que uma classe (classe filha) herde atributos e métodos de outra classe (classe pai)

# Vantagens da herança:
# 1. Reutilização de código: classes filhas reaproveitam funcionalidades da classe pai
# 2. Organização: facilita hierarquia e modularidade
# 3. Extensibilidade: adiciona ou sobrescreve comportamentos sem alterar a classe pai

# Conceito básico:
# class Pai:
#     def metodo(self):
#         print("Método da classe Pai")
#
# class Filho(Pai):
#     pass
#
# objeto = Filho()
# objeto.metodo()  # herdou o método da classe Pai

# Resumo:
# - Herança = mecanismo de derivação de classes
# - Classe pai fornece atributos e métodos
# - Classe filha herda e pode estender ou sobrescrever funcionalidades

# ==============================================================================
# ==============================================================================
# ==============================================================================

# --------------------------
# Aula 13.2 – Herança Simples em Python
# --------------------------

# Classe Pai
class Animal:
    """Classe Pai: Animal"""
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} está emitindo um som genérico!")

# Classe Filha herda da classe Pai
class Cachorro(Animal):
    """Classe Filha: Cachorro"""
    def emitir_som(self):
        print(f"{self.nome} está latindo! Au Au!")

class Gato(Animal):
    """Classe Filha: Gato"""
    def emitir_som(self):
        print(f"{self.nome} está miando! Miau!")

# Criando objetos
a1 = Animal("Animal Genérico")
c1 = Cachorro("Rex")
g1 = Gato("Mimi")

# Chamando métodos
a1.emitir_som()  # Método da classe pai
c1.emitir_som()  # Método sobrescrito na classe filha
g1.emitir_som()  # Método sobrescrito na classe filha

# Resumo:
# - Herança simples = uma classe filha herda de uma classe pai
# - Métodos e atributos da classe pai podem ser usados ou sobrescritos
# - Permite reutilização e especialização de comportamentos


# ==============================================================================
# ==============================================================================
# ==============================================================================

# 13_3_heranca_multiplas.py
# --------------------------
# Aula 13.3 – Herança Múltipla em Python
# --------------------------

# Classe Pai 1
class Voar:
    def habilidade_voar(self):
        print("Esta classe sabe voar!")

# Classe Pai 2
class Nadar:
    def habilidade_nadar(self):
        print("Esta classe sabe nadar!")

# Classe Filha herda de Voar e Nadar
class Pato(Voar, Nadar):
    def emitir_som(self):
        print("Quack! Quack!")

# Criando objeto da classe filha
pato = Pato()

# Chamando métodos herdados das duas classes pai
pato.habilidade_voar()
pato.habilidade_nadar()

# Chamando método próprio da classe filha
pato.emitir_som()

# Resolução de conflitos:
# - Se houver métodos com o mesmo nome em múltiplas classes pai,
#   Python utiliza a ordem da herança (esquerda → direita)
# - Podemos sobrescrever métodos na classe filha para definir comportamento específico

# Exemplo de conflito
class Mamifero:
    def falar(self):
        print("Som de mamífero!")

class Ave:
    def falar(self):
        print("Som de ave!")

class Morcego(Mamifero, Ave):
    pass

morcego = Morcego()
morcego.falar()  # Usa o método da primeira classe na lista de herança (Mamifero)

# Resumo:
# - Herança múltipla = classe filha herda de duas ou mais classes pai
# - Permite combinar funcionalidades de diferentes classes
# - Cuidado com conflitos de métodos → ordem da herança importa

# ==============================================================================
# ==============================================================================
# ==============================================================================