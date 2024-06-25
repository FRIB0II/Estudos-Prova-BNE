print()

extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
           "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

numero = int(input("Digite um número entre 0 e 20: "))
print()

while numero < 0 or numero > 20:
    numero = int(input("Digite novamente. Um número entre 0 e 20: "))
    print()

for cont in range(0, len(extenso)):
    if cont == numero:
        print(f"Você digitou o número {extenso[cont]}.")

print()