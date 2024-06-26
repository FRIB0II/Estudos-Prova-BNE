print()

# Definição das variáveis e listas.
listaNumeros = []
listaMaior = []
listaMenor = []
maior = 0
contador = 0

# Adiciona 5 números na lista.
for numero in range(0,5):
    num = int(input("Digite um número: "))
    listaNumeros.append(num)

# Com base na lista preenchida verifica o maior valor e sua posição.
# Caso exista um valor igual ele pegará sua posição também.
# Foi necessário uma lista auxiliar para colocar as posições, já que elas podem ser várias.
for numero in listaNumeros:
    if maior < numero:
        maior = numero

        listaMaior.clear()

        posicaoMaior = listaNumeros.index(numero)
        listaMaior.append(posicaoMaior + 1)
    
    if maior == numero:
        posicaoMaior = contador
        listaMaior.append(posicaoMaior + 1)

    contador += 1
listaMaior.pop(0)
print()

menor = maior

# Com base no maior valor e na lista fornecida busca o menor valor e sua posição.
# Caso exista um valor igual busca sua posição também.
# Foi necessário uma lista auxiliar para colocar as posições, já que elas podem ser várias.
contador = 0
for numero in listaNumeros:
    if menor > numero:
        menor = numero

        listaMenor.clear()

        posicaoMenor = listaNumeros.index(numero)
        listaMenor.append(posicaoMenor + 1)

    if menor == numero:
        posicaoMenor = contador
        listaMenor.append(posicaoMenor + 1)

    contador += 1
listaMenor.pop(0)

# Mostra a lista.
print("A lista ficou desta forma: ")
print(listaNumeros)
print()

# Mostra o maior número e as posições nas quais ele ocorre.
print(f"O maior número é {maior}, ele está nas posições: ", end="")
for numero in listaMaior:
    print(numero, end="...")

# Mostra o menor número e as posições nas quais ele ocorre.
print()
print(f"O menor número é {menor}, ele está nas posições: ", end="")
for numero in listaMenor:
    print(numero, end="...")

print()