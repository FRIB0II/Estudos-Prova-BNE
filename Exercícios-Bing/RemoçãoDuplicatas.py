listaNumerica = [1, 2, 2, 3, 4, 5, 2, 6, 7, 8, 8,]
listaPalavras = [
    "Nicolas",
    "Lucas", 
    "Gabriel", 
    "Nicolas", 
    "Gabriel", 
    "Nicolas", 
    "Gustavo", 
    "Guilerme", 
    "Marcelo", 
    "Marcelo"]

print(f"Lista númerica original: {listaNumerica}")
print()
print(f"Lista de palavras original: {listaPalavras}")
print()

for numero in listaNumerica:
    cont = 1
    ocorrencias = listaNumerica.count(numero)
    
    if ocorrencias == 1:
        pass
    else:
        while cont < ocorrencias:
            listaNumerica.remove(numero)
            cont += 1

for palavra in listaPalavras:
    cont = 1
    ocorrencias = listaPalavras.count(palavra)

    if ocorrencias == 1:
        pass
    else:
        while cont < ocorrencias:
            listaPalavras.remove(palavra)
            cont += 1 

listaNumericaOrdenada = sorted(listaNumerica)
listaPalavrasOrdenada = sorted(listaPalavras)

listaNumerica.sort()
listaPalavras.sort()

print(f"Lista númerica sem números repetidos (não altera original): {listaNumericaOrdenada}")
print(f"Lista sem palavras repetidas (não altera original): {listaPalavrasOrdenada}")
print()
print(f"Lista númerica sem números repetidos (altera original): {listaNumerica}")
print(f"Lista sem palavras repetidas (altera original): {listaPalavras}")
print()