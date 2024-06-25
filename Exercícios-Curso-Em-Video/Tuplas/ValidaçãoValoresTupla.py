print()

# Entrada de valores
valor1 = int(input("Informe um número: "))
valor2 = int(input("Informe um número: "))
valor3 = int(input("Informe um número: "))
valor4 = int(input("Informe um número: "))
print()

# Armazenando na tupla
tupla = (valor1, valor2, valor3, valor4)
apareceu = tupla.index(3)

# Mostra a tupla
print("A tupla é:")
print(tupla)
print()

# Verifica se existe o número 3 na tupla.
contador = 0
for numero in tupla:
    if numero == 3:
        contador += 1

# Verifica se existe o número 2 na tupla.
contador = 0
for numero in tupla:
    if numero % 2 == 0:
        contador += 1


# Condicionais e mensagens com base nos números da tupla.
print(f"O 9 apareceu {tupla.count(9)} vezes.")

if contador == 4:
    print("O número 3 aparece na lista inteira!")
else:
    print(f"O número 3 apareceu na {apareceu + 1}º posição.")

if contador >= 1:
    print("Os números pares digitados foram: ", end=" ")
    for numero in tupla:
        if numero % 2 == 0:
            print(numero, end=", ")
else:
    print("Não existem números pares na lista!")

print()