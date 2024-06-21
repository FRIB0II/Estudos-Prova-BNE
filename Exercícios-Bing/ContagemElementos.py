import random

tamanhoLista = int(input("Informe o tamanho da lista: "))
print()

listaNumeros = [0] * tamanhoLista
cont = 0
ocorrencias = 0

while cont < tamanhoLista:
    listaNumeros[cont] = random.randint(1, 100)
    cont += 1

numeroABuscar = int(input("Digite o número que você deseja buscar: "))

for numero in listaNumeros:
    if numero == numeroABuscar:
        ocorrencias += 1

print(f"O número aparece {ocorrencias} vezes na lista.")
print()