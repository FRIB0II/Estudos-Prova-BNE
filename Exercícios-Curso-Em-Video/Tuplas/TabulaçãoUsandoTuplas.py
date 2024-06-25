print()

produtos = ("Pão Francês", 12.00, "Margarina", 6.90, "Leite", 4.50, "Pão de queijo X 6", 7.20)

print("-" * 40)
print("Listagem de preços")
print("-" * 40)

contador = 0
for produto in range(0, len(produtos)):
    if contador % 2 == 0:
        print(f"{produtos[produto]}", end="." * 20)
        print(f" R${produtos[produto + 1]:.2f}")
    contador += 1

print("-" * 40)
print()