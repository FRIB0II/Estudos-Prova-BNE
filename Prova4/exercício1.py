vetorA = []

for numero in range(20):
    if numero % 2 == 0:
        vetorA.append(numero * 2)
    else:
        vetorA.append(numero * 3)

print(vetorA)