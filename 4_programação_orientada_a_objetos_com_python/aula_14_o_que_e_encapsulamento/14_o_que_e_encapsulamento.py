# 14_1_o_que_e_encapsulamento.py
# --------------------------
# Aula 14.1 – O que é Encapsulamento em Python
# --------------------------

# Encapsulamento é um princípio da OOP que visa **proteger os dados do objeto**
# e controlar o acesso a atributos e métodos

# Objetivos do encapsulamento:
# 1. Proteger dados internos de alterações indevidas
# 2. Controlar acesso aos atributos e métodos
# 3. Manter a integridade do objeto

# Conceito:
# - Atributos/métodos públicos: acessíveis fora da classe
# - Atributos/métodos privados: acessíveis apenas dentro da classe
# - Atributos protegidos: acessíveis na classe e subclasses (convenção _nome)

# Exemplo conceitual:
# class Conta:
#     def __init__(self, saldo):
#         self.__saldo = saldo  # atributo privado
#     def depositar(self, valor):
#         self.__saldo += valor
#     def consultar_saldo(self):
#         return self.__saldo

# Resumo:
# - Encapsulamento protege o estado interno do objeto
# - Permite acesso controlado através de métodos (getters/setters)
# - Mantém integridade e segurança do código

# ============================================================================
# ============================================================================
# ============================================================================

# --------------------------
# Aula 14.2 – Recursos Públicos, Privados e Protegidos em Python
# --------------------------

# Atributos/Métodos Públicos
# - Acessíveis de qualquer lugar (dentro e fora da classe)
# Exemplo:
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # público

p = Pessoa("Ana")
print(p.nome)  # acesso permitido

# Atributos/Métodos Privados
# - Acessíveis apenas dentro da própria classe
# - Convenção: __nome (dois underscores)
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo  # privado

    def depositar(self, valor):
        self.__saldo += valor

    def consultar_saldo(self):
        return self.__saldo

c = Conta(1000)
c.depositar(500)
print(c.consultar_saldo())  # 1500
# print(c.__saldo)  # ERRO: atributo privado

# Atributos/Métodos Protegidos
# - Acessíveis dentro da classe e subclasses
# - Convenção: _nome (um underscore)
class Veiculo:
    def __init__(self, modelo):
        self._modelo = modelo  # protegido

class Carro(Veiculo):
    def mostrar_modelo(self):
        print(f"Modelo do carro: {self._modelo}")

carro = Carro("Toyota")
carro.mostrar_modelo()  # acesso permitido na subclasse

# Resumo:
# - Público: livre acesso
# - Privado (__): restrito à classe
# - Protegido (_): restrito à classe e subclasses
# - Encapsulamento ajuda a proteger dados e manter integridade

# ============================================================================
# ============================================================================
# ============================================================================

# 14_3_propriedades.py
# --------------------------
# Aula 14.3 – Propriedades em Python
# --------------------------

# Propriedades permitem acessar e alterar atributos privados de forma controlada
# usando métodos "getter" e "setter"

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    # Getter para saldo
    @property
    def saldo(self):
        return self.__saldo

    # Setter para saldo
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo!")

# Criando objeto
c = Conta("Ana", 1000)

# Acessando saldo com getter
print(f"Saldo inicial: R$ {c.saldo}")

# Alterando saldo com setter
c.saldo = 1500
print(f"Saldo atualizado: R$ {c.saldo}")

# Tentando colocar saldo negativo
c.saldo = -500  # Mensagem de erro

# Resumo:
# - @property cria getter para acessar atributo privado
# - @setter cria método para alterar valor de forma controlada
# - Encapsulamento + propriedades garantem segurança e integridade

# ============================================================================
# ============================================================================
# ============================================================================