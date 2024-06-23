print()

media = 0
soma = 0
homemMaisVelho = ""
idadeMaisVelho = 0
sub20 = 0


for contador in range(1, 5):
    
    nomeInformado =  str(input("Digite seu nome: "))
    idadeInformada = int(input("Digite sua idade: "))
    genero = str(input("Informe seu gênero: "))
    print()

    soma += idadeInformada

    if genero == "Masculino":
        if idadeMaisVelho < idadeInformada:
            idadeMaisVelho = idadeInformada
            homemMaisVelho = nomeInformado
    elif genero == "Feminino":
        if idadeInformada < 20:
            sub20 += 1

media = soma / 5

print(f"A média de idade do grupo é: {media} anos.")
print(f"O nome do home mais velho é: {homemMaisVelho}.")
print(f"O número de mulheres abaixo de 20 anos é: {sub20}.")

print()