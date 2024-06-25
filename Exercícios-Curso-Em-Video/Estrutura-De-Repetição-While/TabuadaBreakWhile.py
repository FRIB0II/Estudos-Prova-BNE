print()

numero = 1
multiplicacao = 0

while numero != 0:
    contador = 0
    numero = int(input("Digite um número para ver sua tabuada até 10: "))
    if numero <= 0:
        break
    else:
        while contador <= 10:
            multiplicacao = numero * contador
            print(f"{numero} X {contador} = {multiplicacao}.")
            contador += 1
        print()

print()
print("Fim.")
print()