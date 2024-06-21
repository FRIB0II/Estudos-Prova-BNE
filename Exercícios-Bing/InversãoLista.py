# Inverte as posições dos elementos da lista
def InverteItens():

    cont = 0
    aux = 1

    while cont < tamanhoLista:
        listaInversa[cont] = listaPalavras[tamanhoLista-aux]
        cont += 1
        aux += 1

    return listaInversa

# Inverte as palavras da lista
def InvertePalavras(listaInvertida, booleano):

    cont = 0

    if booleano == True:
        for palavra in listaPalavras:
    
            palavraInvertida = palavra[::-1]
            listaInvertida[cont] = palavraInvertida
            cont += 1

        return listaInvertida
    
    elif booleano == False:
        for palavra in listaPalavras:
    
            palavraInvertida = palavra[::-1]
            listaInversa[cont] = palavraInvertida
            cont += 1

        return listaInversa   

# Inverte a ordem e as própias palavras da lista
def InvertePalavrasEOrdem(booleano):

    retornoInverteItens = InverteItens()
    retornoInvertePalavras = InvertePalavras(retornoInverteItens, booleano)
    
    return retornoInvertePalavras


tamanhoLista = int(input("Insira o tamanho da lista: "))
print()

listaPalavras = [0] * tamanhoLista
listaInversa = [0] * tamanhoLista
palavraInvertida = ""
cont = 0

# Recebe valores na lista
while cont < tamanhoLista:

    palavra = input("Digite uma palavra: ")
    listaPalavras[cont] = palavra

    cont += 1

print()

print(f"Lista normal: {listaPalavras}")
print()
print(f"Lista invertida: {InverteItens()}")
print()
inverterTudo = False
print(f"Lista de palavras invertidas: {InvertePalavras(inverterTudo, inverterTudo)}")
print()
inverterTudo = True
print(f"Lista de ordem e palavras invertidas: {InvertePalavrasEOrdem(inverterTudo)}")
print()