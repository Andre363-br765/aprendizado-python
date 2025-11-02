# Aula 7: Dicionários em Python
# --------------------------

# --------------------------
# 7.1 Criando dicionários
# --------------------------
# Sintaxe: {chave: valor, ...}
dicionario_vazio = {}
aluno = {"nome": "Ana", "idade": 20, "curso": "Python"}
print(dicionario_vazio)
print(aluno)

# --------------------------
# 7.2 Acessando valores
# --------------------------
print("Nome:", aluno["nome"])
print("Idade:", aluno.get("idade"))  # forma segura, retorna None se não existir

# --------------------------
# 7.3 Modificando valores
# --------------------------
aluno["idade"] = 21
aluno["curso"] = "Python Avançado"
print(aluno)

# --------------------------
# 7.4 Adicionando e removendo itens
# --------------------------
# Adicionando
aluno["nota"] = 9.5

# Removendo
removido = aluno.pop("curso")  # remove e retorna o valor
print("Removido:", removido)
print(aluno)

# --------------------------
# 7.5 Métodos úteis do dict
# --------------------------
print("Chaves:", aluno.keys())       # lista de chaves
print("Valores:", aluno.values())    # lista de valores
print("Itens:", aluno.items())       # lista de tuplas (chave, valor)

# --------------------------
# 7.6 Iterando sobre dicionários
# --------------------------
for chave in aluno:
    print(f"{chave}: {aluno[chave]}")

# Usando items()
for chave, valor in aluno.items():
    print(f"{chave} -> {valor}")

# --------------------------
# 7.7 Dicionários aninhados
# --------------------------
alunos = {
    "a1": {"nome": "Ana", "idade": 20},
    "a2": {"nome": "Bruno", "idade": 22},
    "a3": {"nome": "Carla", "idade": 21}
}

print(alunos["a2"]["nome"])  # Bruno

# Iterando sobre dicionários aninhados
for id_aluno, info in alunos.items():
    print(f"{id_aluno}: {info['nome']} - {info['idade']} anos")
