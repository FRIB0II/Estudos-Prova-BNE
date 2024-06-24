print()

frase = str(input("Digite uma frase: "))
fraseFormatada = frase.lower()
fraseFormatada = fraseFormatada.replace(" ", "")

fraseReversa = fraseFormatada[::-1]

if fraseFormatada == fraseReversa:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")

print()