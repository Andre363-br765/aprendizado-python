# Aula 1.4 – Conversão de tipos (casting)

def exemplos_conversao():
    # Para inteiro
    x = int(3.14)
    y = int("10")
    print(x, y)

    # Para float
    a = float(10)
    b = float("10.10")
    print(a, b)

    # Para string
    valor = 10
    valor_str = str(valor)
    preco = 3.14
    preco_str = str(preco)
    print(type(valor), type(valor_str))
    print(preco_str)

    # Para booleano
    v1, v2, v3, v4 = bool(1), bool(0), bool(""), bool("Python")
    print(v1, v2, v3, v4)

    # Diferenças de divisão
    print(100 / 2)   # float
    print(100 // 2)  # inteiro

if __name__ == "__main__":
    exemplos_conversao()
