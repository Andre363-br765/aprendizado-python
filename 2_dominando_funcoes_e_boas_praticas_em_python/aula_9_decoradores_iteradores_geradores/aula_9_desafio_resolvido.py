# aula_9_desafio.py
# Aula 9.4 e 9.5: Desafio e Desafio Resolvido – Decoradores, Iteradores e Geradores

# --------------------------
# Aula 9.4: Desafio
# --------------------------
# Crie um programa que combine:
# 1. Um decorador que mostre a execução de uma função.
# 2. Um gerador que gere números pares até um limite informado.
# 3. Um iterador personalizado que conte quantas vezes a função foi chamada.

# Escreva o código para implementar essas funcionalidades.

# --------------------------
# Aula 9.5: Desafio Resolvido
# --------------------------

# Decorador que mostra execução
def mostrar_execucao(funcao):
    def wrapper(*args, **kwargs):
        print(f"Iniciando '{funcao.__name__}'...")
        resultado = funcao(*args, **kwargs)
        print(f"'{funcao.__name__}' finalizada.")
        return resultado
    return wrapper

# Iterador personalizado para contar chamadas
class ContadorChamadas:
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1
        return self.contador

contador = ContadorChamadas()

# Gerador que produz números pares até um limite
def gerar_pares(limite):
    for i in range(limite + 1):
        if i % 2 == 0:
            yield i

# Função que combina tudo
@mostrar_execucao
def processar_pares(limite):
    print(f"Chamada número: {contador.incrementar()}")
    for n in gerar_pares(limite):
        print(n, end=" ")
    print()  # nova linha

# Chamadas de teste
processar_pares(10)
processar_pares(6)
processar_pares(8)

# --------------------------
# Resumo do desafio
# --------------------------
# - Decoradores: adiciona comportamento extra (mostrar início/fim da função)
# - Iteradores personalizados: contador de chamadas
# - Geradores: números pares gerados sob demanda
# - Combinação de conceitos da Aula 9 para prática