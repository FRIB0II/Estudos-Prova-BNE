print()

numero = float(input("Digite um número: "))

quantidadeNumeros = 1
soma = numero
media = 0
maiorNumero = numero
menorNumero = numero

escolha = str(input("Deseja continuar? [S/N]: "))
escolhaFormatada = escolha.upper()
print()

while escolhaFormatada != "S" and escolhaFormatada != "N":
    print("Valor inválido!")
    escolha = str(input("Digite novamente [S/N]: "))
    escolhaFormatada = escolha.upper()
    print()
    
while escolhaFormatada == "S":
    
    numero = float(input("Digite um número: "))
    quantidadeNumeros += 1
    soma += numero
    
    if maiorNumero < numero:
        maiorNumero = numero
    
    if menorNumero > numero:
        menorNumero = numero
    
    escolha = str(input("Deseja continuar? [S/N]: "))
    escolhaFormatada = escolha.upper()
    print()
    
    while escolhaFormatada != "S" and escolhaFormatada != "N":
        print("Valor inválido!")
        escolha = str(input("Digite novamente [S/N]: "))
        escolhaFormatada = escolha.upper()
        print()

media = soma / quantidadeNumeros

print(f"A média de todos é {media:.2f}.")
print(f"O maior número é: {maiorNumero:.2f} e o menor é: {menorNumero:.2f}.")
print()