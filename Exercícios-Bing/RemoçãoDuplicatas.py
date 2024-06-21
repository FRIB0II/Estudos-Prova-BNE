listaNumerica = [1, 2, 2, 3, 4, 5, 6, 7, 8, 8,]
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

cont = 1
ocorrencias = 0
tamanhoListaNumerica = len(listaNumerica)

print(f"Lista númerica original: {listaNumerica}")
print()
print(f"Lista de palavras original: {listaPalavras}")
print()

for numero in listaNumerica:
    
    ocorrencias = listaNumerica.count(numero)
    
    if ocorrencias == 1:
        continue
    else:
        while cont <= ocorrencias:
            if ocorrencias == 1:
                cont += 1
                
            listaNumerica.remove(numero)
            cont += 1

print(f"Lista númerica sem números repetidos: {listaNumerica}")


