from random import randint

print()

valor1 = randint(1,10)
valor2 = randint(1,10)
valor3 = randint(1,10)
valor4 = randint(1,10)
valor5 = randint(1,10)

maior = 0
menor = 11

tuplaNumerica = (valor1, valor2, valor3, valor4, valor5)

print(tuplaNumerica)
print()

for numero in tuplaNumerica:
    if maior < numero:
        maior = numero
    
    if menor > numero:
        menor = numero

print(f"O maior número da tupla acima é {maior}.")
print(f"O menor número da tupla acima é {menor}.")

print()