# aula2_6_operadores_associacao_desafio.py
# Aula 2.6 – Operadores de Associação (Desafio divertido!)

# --------------------------
# Situação inicial (com alguns itens trocados de propósito!)
# --------------------------
frutas = ["laranja", "banana", "abacate", "pera"]
verduras = ["alface", "cenoura", "espinafre", "brócolis"]
legumes = ["couve", "batata", "abobrinha", "uva"]

# --------------------------
# Desafio:
# Corrigir as listas SEM APAGAR nem reescrever nada.
# Podemos usar apenas manipulações de lista (pop, insert, append, etc).
# --------------------------

# Etapa 1: Mover a "uva" dos legumes para as frutas 🍇
# A função pop() remove e retorna o último elemento da lista (no caso, "uva").
# A função insert(posição, valor) insere o valor na posição desejada da lista.
frutas.insert(2, legumes.pop())  

# Etapa 2: Mover a "cenoura" das verduras para os legumes 🥕
# Aqui removemos o item na posição 1 (cenoura) de verduras e inserimos no início da lista legumes.
legumes.insert(0, verduras.pop(1))

# Etapa 3: Mover a "couve" dos legumes para as verduras 🥬
# Agora a "couve" está na posição 1 da lista legumes (depois da etapa anterior).
verduras.insert(1, legumes.pop(1))

# --------------------------
# Resultado final – tudo no seu devido lugar!
# --------------------------
print("Frutas:", frutas)
print("Verduras:", verduras)
print("Legumes:", legumes)

# --------------------------
# Saída esperada:
# Frutas: ['laranja', 'banana', 'uva', 'abacate', 'pera']
# Verduras: ['alface', 'couve', 'espinafre', 'brócolis']
# Legumes: ['cenoura', 'batata', 'abobrinha']
# --------------------------

# --------------------------
# Observações de boas práticas
# --------------------------
# 1. Manipular listas com pop(), insert() e append() é útil para reorganizar dados dinamicamente.
# 2. Teste sempre os índices antes de remover ou inserir (para evitar erros de posição).
# 3. Evite reescrever listas inteiras: pequenas operações podem resolver grandes confusões.
# 4. Use nomes de variáveis claros e compatíveis com o conteúdo.
# 5. Desafios como este ajudam a entender como listas funcionam de verdade!
