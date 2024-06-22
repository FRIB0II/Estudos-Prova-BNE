print()
palavra = str(input("Digite uma palavra para verificação: "))
print()

palavraFormatada = palavra.lower()

palavraInvertida = palavraFormatada[::-1]

if palavraFormatada == palavraInvertida:
    print(f"A palavra {palavra}, é um palíndromo.")
else:
    print(f"A palavra {palavra}, Não é um palíndromo.")

print()