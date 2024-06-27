print()

# Definindo a lista.
numeros = []

# Lógica principal.
for c in range(0, 5):
    contador = 0 
    num = int(input("Digite um número: "))
    
    # Verifica se o número já existe na lista.
    # Caso exista ele coloca o número lido na frente dele e passa para ->
    # a próxima iteração.
    if num in numeros:
        posicao = numeros.index(num)
        numeros.insert(posicao + 1, num)
        print(f"Número inserido na posição {posicao + 1}.")
        print()
        continue
    
    # Verifica se o número digitado é maior que o número lido na lista.
    # Caso seja ele itera 1 no contador e passa para o próximo valor.
    # Se ele não for maior ele para a repetição e insere o número na posição ->
    # Correta. Nessa caso na posição contador, que é referente ao número que ele é maior.
    for numero in numeros:
        if num >= numero:
            contador +=1
        else: 
            break

    numeros.insert(contador, num)

    if contador == 0:
        print("Número inserido na posição 1º posição.")
    elif contador == 5 or contador+1 == 5:
        print("Número inserido na última posição.")
    else:
        print(f"Número inserido na {contador + 1}º posição.")
    print()

# Mostra a lista com a ordenação feita.
print("Lista ordenada: ")
print(numeros)

print()