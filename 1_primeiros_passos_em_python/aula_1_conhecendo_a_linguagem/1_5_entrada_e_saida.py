# Aula 1.5 – Funções de entrada e saída

def exemplos_saida():
    nome = "Ana"
    idade = 20
    print("Olá, mundo!")
    print(10 + 5)
    print("Nome:", nome, "Idade:", idade)
    print(f"Nome: {nome}, Idade: {idade}")
    print(nome, idade, end="...\n")
    print(nome, idade, sep="#", end="...\n")
    print(nome, idade, sep="#")

def exemplos_entrada():
    # Recebendo dados do usuário (comentado para não travar execução)
    # usuario = input("Digite seu nome: ")
    # print("Olá,", usuario)
    # idade = int(input("Digite sua idade: "))
    # altura = float(input("Digite sua altura: "))
    pass

if __name__ == "__main__":
    exemplos_saida()
    # exemplos_entrada()  # ativar se quiser testar input()
