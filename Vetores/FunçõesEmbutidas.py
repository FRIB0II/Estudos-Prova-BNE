# Map
# Aplica uma função em uma lista para retornar um resultado específico
numeros = [1, 2, 3, 4]
quadrados = map(lambda x: x ** 2, numeros)
print(list(quadrados))  # Deve imprimir [1, 4, 9, 16]


# Filter
# Gera uma lista com elementos que satisfazem uma condição
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Deve imprimir [2, 4, 6]

# Sorted
# Ordena os elementos de uma lista
nomes = ["Alice", "Bob", "Eva", "David"]
nomes_ordenados = sorted(nomes)
print(nomes_ordenados)  # Deve imprimir ['Alice', 'Bob', 'David', 'Eva']

# Sum
# Soma os elementos de uma lista
numeros = [10, 20, 30, 40]
soma_total = sum(numeros)
print(soma_total)  # Deve imprimir 100

# Enumerate
# Atribui a cada valor de uma lista um indíce
frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")