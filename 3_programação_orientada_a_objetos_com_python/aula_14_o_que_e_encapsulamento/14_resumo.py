# 14_4_resumo.py
# --------------------------
# Aula 14.4 – Resumo Completo da Aula 14 (Encapsulamento em Python)
# --------------------------

# 1. Conceito de Encapsulamento
# - Encapsulamento protege os dados internos do objeto
# - Permite controlar o acesso a atributos e métodos
# - Mantém integridade e segurança do código

# 2. Atributos e Métodos Públicos
# - Acessíveis de qualquer lugar
# Exemplo:
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
# p = Pessoa("Ana")
# print(p.nome)  # acesso permitido

# 3. Atributos e Métodos Privados
# - Acessíveis apenas dentro da classe
# - Convenção: __nome
# Exemplo:
# class Conta:
#     def __init__(self, saldo):
#         self.__saldo = saldo
#     def consultar_saldo(self):
#         return self.__saldo

# 4. Atributos e Métodos Protegidos
# - Acessíveis na classe e subclasses
# - Convenção: _nome
# Exemplo:
# class Veiculo:
#     def __init__(self, modelo):
#         self._modelo = modelo
# class Carro(Veiculo):
#     def mostrar_modelo(self):
#         print(self._modelo)

# 5. Propriedades (@property e @setter)
# - Permitem acessar e alterar atributos privados de forma controlada
# - Garantem integridade do objeto
# Exemplo:
# class Conta:
#     def __init__(self, saldo):
#         self.__saldo = saldo
#     @property
#     def saldo(self):
#         return self.__saldo
#     @saldo.setter
#     def saldo(self, valor):
#         if valor >= 0:
#             self.__saldo = valor

# 6. Boas práticas em Encapsulamento
# - Use atributos privados para dados sensíveis
# - Forneça métodos públicos ou propriedades para acessar/modificar
# - Evite acesso direto a atributos privados fora da classe
# - Documente bem os getters e setters
# - Combine encapsulamento com boas práticas de OOP (modularidade, reutilização)

# Resumo final:
# - Encapsulamento = proteção de dados internos
# - Público, privado, protegido = níveis de acesso
# - @property/@setter = acesso controlado
# - Mantém código seguro, modular e fácil de manter
