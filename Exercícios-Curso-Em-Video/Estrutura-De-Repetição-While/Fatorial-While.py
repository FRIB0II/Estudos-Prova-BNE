print()

numero = int(input("Digite um número para descobrir seu fatorial: "))
    
contador = 1
fatorial = 1

while contador <= numero:
    fatorial = fatorial * contador
    contador += 1

print(f"O fatorial do número {numero} é {fatorial}.")
print()