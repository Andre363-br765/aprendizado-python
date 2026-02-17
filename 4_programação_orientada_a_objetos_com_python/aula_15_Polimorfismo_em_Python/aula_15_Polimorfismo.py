# 15_1_o_que_e_polimorfismo.py
# --------------------------
# Aula 15.1 – O que é Polimorfismo
# --------------------------

# Polimorfismo significa "muitas formas".
# Em Python, ele permite que diferentes classes tenham métodos com o mesmo nome,
# mas comportamentos diferentes.

# Isso torna o código mais flexível e reutilizável.

# Exemplo simples de polimorfismo com método comum:

class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Vaca(Animal):
    def falar(self):
        return "Muuu!"

# Lista de diferentes objetos, mas todos têm o método 'falar'
animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    print(animal.falar())

# Saída:
# Au Au!
# Miau!
# Muuu!

# Explicação:
# - O método falar() é polimórfico: ele existe em várias classes.
# - Cada classe implementa o comportamento de forma diferente.
# - O programa não precisa saber o tipo exato do objeto para chamá-lo.
# - Isso é um dos pilares da Programação Orientada a Objetos.

# ==============================================================================
# ==============================================================================
# ==============================================================================

# 15_2_polimorfismo_basico.py
# --------------------------
# Aula 15.2 – Polimorfismo em Herança
# --------------------------

# O polimorfismo é muito usado em herança:
# Quando uma subclasse sobrescreve (redefine) um método da classe pai,
# mas mantém a mesma interface (mesmo nome de método).

# Exemplo prático:

class Forma:
    def area(self):
        raise NotImplementedError("A subclasse deve implementar este método")

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        from math import pi
        return pi * (self.raio ** 2)

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


# Mesmo método "area()", mas comportamento diferente para cada forma
formas = [
    Quadrado(4),
    Circulo(3),
    Triangulo(6, 4)
]

for forma in formas:
    print(f"{forma.__class__.__name__}: área = {forma.area():.2f}")

# Saída:
# Quadrado: área = 16.00
# Circulo: área = 28.27
# Triangulo: área = 12.00

# Explicação:
# - Todas as subclasses implementam o método "area".
# - A função que usa "forma.area()" não precisa saber o tipo da forma.
# - Cada objeto executa o comportamento correto automaticamente.
# - Isso é o poder do polimorfismo!

# ==============================================================================
# ==============================================================================
# ==============================================================================