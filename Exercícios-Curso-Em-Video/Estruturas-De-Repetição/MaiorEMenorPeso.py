print()

maiorPeso = 0
menorPeso = 1000

for contador in range(1, 6):

    peso = float(input("Insira seu peso: "))

    if maiorPeso < peso:
        maiorPeso = peso
    elif menorPeso > peso:
        menorPeso = peso
    
print()
print(f"O maior peso é {maiorPeso}Kg.")
print(f"O menor peso é {menorPeso}Kg.")
print()