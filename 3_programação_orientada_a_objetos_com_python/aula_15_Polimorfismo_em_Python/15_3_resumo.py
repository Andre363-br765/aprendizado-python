# 15_3_resumo.py
# --------------------------
# Aula 15 – Resumo: Polimorfismo em Python
# --------------------------

# 1. O que é Polimorfismo?
# - "Polimorfismo" significa "muitas formas".
# - Permite que diferentes classes tenham métodos com o mesmo nome,
#   mas comportamentos diferentes.
# - Torna o código mais flexível, genérico e reutilizável.

# ---------------------------------------------------------
# 2. Exemplo básico
# ---------------------------------------------------------
# class Animal:
#     def falar(self):
#         pass
#
# class Cachorro(Animal):
#     def falar(self):
#         return "Au Au!"
#
# class Gato(Animal):
#     def falar(self):
#         return "Miau!"
#
# animais = [Cachorro(), Gato()]
# for animal in animais:
#     print(animal.falar())
#
# # Saída:
# # Au Au!
# # Miau!

# ---------------------------------------------------------
# 3. Polimorfismo e Herança
# ---------------------------------------------------------
# - Ocorre quando subclasses herdam um método da classe pai,
#   mas o redefinem de forma personalizada (sobrescrita).
#
# Exemplo:
# class Forma:
#     def area(self):
#         raise NotImplementedError
#
# class Quadrado(Forma):
#     def __init__(self, lado):
#         self.lado = lado
#     def area(self):
#         return self.lado ** 2
#
# class Circulo(Forma):
#     def __init__(self, raio):
#         self.raio = raio
#     def area(self):
#         from math import pi
#         return pi * (self.raio ** 2)

# ---------------------------------------------------------
# 4. Vantagens do Polimorfismo
# ---------------------------------------------------------
# ✅ Facilita a manutenção e expansão do código.
# ✅ Permite trabalhar com objetos de tipos diferentes da mesma forma.
# ✅ Reduz repetição de código.
# ✅ Melhora a legibilidade e a organização em projetos grandes.

# ---------------------------------------------------------
# 5. Boas práticas
# ---------------------------------------------------------
# - Use o mesmo nome de método para comportamentos equivalentes.
# - Utilize herança para aplicar polimorfismo de forma natural.
# - Crie métodos abstratos (com NotImplementedError) em classes base.
# - Combine com encapsulamento e herança para código limpo e seguro.

# ---------------------------------------------------------
# 6. Resumo final
# ---------------------------------------------------------
# Polimorfismo é um dos pilares da Programação Orientada a Objetos (POO).
# Ele permite que diferentes objetos respondam de maneiras únicas
# a uma mesma chamada de método.
#
# Isso torna o código dinâmico, elegante e escalável.
