tamanhoLista = int(input("Digite o tamanho da lista: "))
print()

listaNumeros = [0] * tamanhoLista
cont = 0
soma = 0

while cont < tamanhoLista:
    numeroInserido = int(input("Insira um número: "))
    soma += numeroInserido
    listaNumeros[cont] = numeroInserido
    cont += 1

print()
print(listaNumeros)
print(f"A soma de todos os números da lista acima é {soma}.")
print()