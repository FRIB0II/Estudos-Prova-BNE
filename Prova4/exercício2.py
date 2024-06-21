vetorB = [45, 50, 51, 42, 30, 28, 30, 15, 2, 48]
menorNumero = vetorB[0]

for numero in vetorB:
    if menorNumero > numero:
        menorNumero = numero

print(menorNumero)