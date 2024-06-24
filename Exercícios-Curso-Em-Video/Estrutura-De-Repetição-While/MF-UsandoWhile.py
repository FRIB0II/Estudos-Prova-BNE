print()
genero = str(input("Qual o seu gênero? [M/F]: "))
generoFormatado = genero.upper()
print()

while generoFormatado != "M" and generoFormatado != "F":
    print("Valor inválido!")
    genero = str(input("Digite [M/F]: "))
    generoFormatado = genero.upper()
    print()

print("Fim.")