print()

deMaior = 0
quantidadeHomens = 0
mulheresSub20 = 0

while True:
    
    idade = int(input("Informe sua idade: "))
    genero = str(input("Informe seu gênero [M/F]: "))

    generoFormatado = genero.upper()

    while generoFormatado != "M" and generoFormatado != "F":
        genero = str(input("Informe seu gênero [M/F]: "))

    if idade > 18:
        deMaior += 1

    if generoFormatado == "M":
        quantidadeHomens += 1
    elif generoFormatado == "F":
        if idade < 20:
            mulheresSub20 += 1

    escolha = str(input("Deseja continuar? [S/N]: "))
    print()
    print("-="*21)
    escolhaFormata = escolha.upper()

    while escolhaFormata != "S" and escolhaFormata != "N":
            escolha = str(input("Deseja continuar? [S/N]: "))
            print()
            print("-="*21)
            escolhaFormata = escolha.upper()

    if escolhaFormata == "N":
        break

print()
print(f"Existem {deMaior} pessoas com mais de 18 anos.")
print(f"Foram cadastrados {quantidadeHomens} homens.")
print(f"Existe {mulheresSub20} mulheres com menos de 20 anos.")
print()