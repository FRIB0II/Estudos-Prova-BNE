tamanhoLista = int(input("Digite o tamanho da lista: "))
print()

listaNumeros = [0] * tamanhoLista
cont = 0
soma = 0
quantidadeNumerosPares = 0
media = 0

while cont < tamanhoLista:
    num = int(input("Insira um número na lista: "))
    listaNumeros[cont] = num
    cont += 1

for numeros in listaNumeros:
    if numeros % 2 == 0:
        soma += numeros
        quantidadeNumerosPares += 1

media = soma / quantidadeNumerosPares

print()
print(f"A média dos elementos pares na lista é: {media}")
print()
