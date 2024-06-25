print()

tuplaPalavras = ("eu", "amo", "a", "programação", "demais", "amigos", "familia", "deus")

vogais = "aeiou"

for palavra in tuplaPalavras:
    contador = 0
    print(f"Na palavra {palavra.upper()}, temos: ", end=" ")
    while contador < len(palavra):
        if palavra[contador] in vogais:
            print(palavra[contador], end=", ")
        contador += 1
    print("\n")
        

print()