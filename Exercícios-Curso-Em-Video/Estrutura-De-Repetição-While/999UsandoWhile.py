print()

numero = int(input("Digite um número: "))
print()
contadorNumeros = 0
soma = 0

while numero != 999:
    soma += numero
    contadorNumeros += 1
    numero = int(input("Digite um número: "))
    print()
    

print(f"Foram digitados {contadorNumeros} números. A soma deles é {soma}.")
print()