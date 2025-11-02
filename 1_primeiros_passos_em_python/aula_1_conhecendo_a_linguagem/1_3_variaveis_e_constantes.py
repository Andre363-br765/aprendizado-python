# Aula 1.3 – Variáveis e Constantes

def exemplos_variaveis():
    nome = "Ana"
    idade = 20
    altura = 1.65
    ligado = True
    saldo = 1500.50
    ativo = False

    # Alterando valores
    idade = 21
    nome = "Leo"
    print(nome, idade)

    limite_saque = 1000
    BRAZILIAN_STATES = ["RS", "SP", "RJ", "SC"]
    print(BRAZILIAN_STATES)

    total = saldo + limite_saque
    print("Total disponível:", total)

    # Constantes
    PI = 3.14159
    TAXA = 0.05
    MAX_USUARIOS = 1000
    DIAS_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

    print("PI:", PI)
    print("Taxa:", TAXA)
    print("Máximo de usuários:", MAX_USUARIOS)
    print("Dias da semana:", DIAS_SEMANA)

if __name__ == "__main__":
    exemplos_variaveis()
