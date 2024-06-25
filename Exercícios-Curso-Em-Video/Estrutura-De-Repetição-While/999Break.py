print()

numero = 0
soma = 0
contador = 0

while numero != 999:
    numero = int(input("Informe um número: "))
    if numero == 999:
        break
    else:
        soma += numero
        contador += 1

print(f"Foram digitados {contador} números. A soma deles é {soma}.")

print()