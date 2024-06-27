print()

numeros = []

while True:
    num = int(input("Digite um número: "))
    if num in numeros:
        print(f"O número {num} já existe na lista!")
    else:
        print("Adicionando o número na lista...")
        numeros.append(num)
        
    escolha = str(input("Deseja coninuar? [S/N]: "))
    escolhaFormatada = escolha.upper()
    print()

    if escolhaFormatada == "N":
        break

numeros.sort()

print("A lista ficou dessa forma: ")
print(numeros)

print()