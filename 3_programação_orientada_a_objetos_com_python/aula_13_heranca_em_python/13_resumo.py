# --------------------------
# Aula 13.4 – Resumo Completo da Aula 13 (Herança em Python)
# --------------------------

# 1. Conceito de Herança
# - Permite que uma classe (filha) herde atributos e métodos de outra classe (pai)
# - Vantagens: reutilização de código, organização, extensibilidade

# 2. Herança Simples
# - Uma classe filha herda de uma classe pai
# - Pode usar ou sobrescrever métodos da classe pai
# Exemplo:
# class Animal:
#     def emitir_som(self):
#         print("Som genérico")
# class Cachorro(Animal):
#     def emitir_som(self):
#         print("Au Au")
# c = Cachorro()
# c.emitir_som()  # Saída: Au Au

# 3. Herança Múltipla
# - Classe filha herda de duas ou mais classes pai
# - Combina funcionalidades de diferentes classes
# - Atenção a conflitos de métodos → Python segue a ordem da lista de herança (esquerda → direita)
# Exemplo:
# class Voar:
#     def habilidade_voar(self): print("Voando")
# class Nadar:
#     def habilidade_nadar(self): print("Nadando")
# class Pato(Voar, Nadar):
#     pass
# pato = Pato()
# pato.habilidade_voar()  # Saída: Voando
# pato.habilidade_nadar() # Saída: Nadando

# 4. Sobrescrita de Métodos
# - Classe filha pode redefinir métodos da classe pai para comportamento específico
# - Permite especializar funcionalidades sem alterar a classe pai

# 5. Boas práticas em herança
# - Usar herança quando há relação “é um” (ex: Cachorro é um Animal)
# - Evitar herança excessiva desnecessária
# - Manter classes pai genéricas e reutilizáveis
# - Sobrescrever métodos apenas quando necessário
# - Documentar bem as classes e métodos

# Resumo final:
# - Herança simples → reutilização e especialização
# - Herança múltipla → combina funcionalidades de múltiplas classes
# - Sobrescrita → adapta métodos herdados
# - Boa prática → manter hierarquia clara, evitar conflitos e documentar