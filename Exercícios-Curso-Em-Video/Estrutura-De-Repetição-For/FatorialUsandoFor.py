print()

numero = int(input("Digite um número para descobrir seu fatorial: "))
fatorial = 1

for contador in range(1, numero + 1):
    fatorial = fatorial * contador

print(f"O fatorial do número {numero} é {fatorial}.")

print()