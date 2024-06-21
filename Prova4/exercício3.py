vetorB = [45, 50, 51, 42, 30, 28, 30, 15, 2, 48]
soma = 0
media = 0

for numero in vetorB:
    soma += numero

media = soma / len(vetorB)
print(vetorB)
print(f"A soma dos números do array é: {soma}, e sua média é: {media:.2f}")
