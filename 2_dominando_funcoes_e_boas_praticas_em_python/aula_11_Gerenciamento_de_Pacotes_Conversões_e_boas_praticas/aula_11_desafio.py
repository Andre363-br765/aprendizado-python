# aula_11_desafio.py
# Aula 11: Desafio – Gerenciamento de Pacotes, Conversões e Boas Práticas
# --------------------------

# Desafio:
# 1. Criar um arquivo CSV com produtos: nome, preço e quantidade.
# 2. Ler o CSV e converter os valores de preço e quantidade para float/int.
# 3. Calcular o valor total do estoque (preço * quantidade).
# 4. Exibir um resumo do estoque.
# 5. Aplicar boas práticas de programação: funções, docstrings, tratamento de erros.
# 6. (Opcional) Usar algum pacote externo instalado via pip, como prettytable para exibir tabela.

# --------------------------
# Resolução do Desafio
# --------------------------
import csv

try:
    # 1. Criar CSV
    with open("produtos_desafio.csv", "w", newline="", encoding="utf-8") as arq_csv:
        escritor = csv.writer(arq_csv)
        escritor.writerow(["Nome", "Preco", "Quantidade"])
        escritor.writerow(["Caneta", 2.5, 100])
        escritor.writerow(["Lápis", 1.2, 200])
        escritor.writerow(["Caderno", 15.0, 50])
        escritor.writerow(["Borracha", 0.8, 80])
    print("Arquivo 'produtos_desafio.csv' criado com sucesso!\n")

    # 2. Ler CSV e converter tipos
    produtos = []
    with open("produtos_desafio.csv", "r", encoding="utf-8") as arq_csv:
        leitor = csv.DictReader(arq_csv)
        for linha in leitor:
            produto = {
                "Nome": linha["Nome"],
                "Preco": float(linha["Preco"]),
                "Quantidade": int(linha["Quantidade"])
            }
            produtos.append(produto)

    # 3. Função para calcular valor total do estoque
    def calcular_valor_estoque(produtos):
        """
        Recebe uma lista de produtos e calcula o valor total do estoque.
        """
        total = 0
        for p in produtos:
            total += p["Preco"] * p["Quantidade"]
        return total

    # 4. Exibir resumo
    total_estoque = calcular_valor_estoque(produtos)
    print("📦 Resumo do Estoque:")
    print(f"Total de produtos cadastrados: {len(produtos)}")
    print(f"Valor total do estoque: R$ {total_estoque:.2f}\n")

    print("📋 Produtos cadastrados:")
    for p in produtos:
        print(f"- {p['Nome']}: {p['Quantidade']} unidades a R$ {p['Preco']:.2f} cada")

    # 5. Boas práticas
    # - Funções usadas
    # - Docstrings explicando
    # - Tratamento de erros com try/except
    # - Conversões de tipos corretas
    # - Código organizado e legível

    # 6. (Opcional) Mostrar tabela formatada usando prettytable
    try:
        from prettytable import PrettyTable

        tabela = PrettyTable()
        tabela.field_names = ["Nome", "Preço (R$)", "Quantidade", "Subtotal (R$)"]
        for p in produtos:
            tabela.add_row([p["Nome"], f"{p['Preco']:.2f}", p["Quantidade"], f"{p['Preco']*p['Quantidade']:.2f}"])

        print("\n📊 Tabela formatada com PrettyTable:")
        print(tabela)

    except ImportError:
        print("\nPrettyTable não instalado. Para instalar: pip install prettytable")

except Exception as e:
    print("Ocorreu um erro:", e)