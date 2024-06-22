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

tamanhoListaPalavras = len(listaPalavras)
listaPalavraRemovida = []
cont = 0

print()
print(f"Lista de palavras: {listaPalavras}")
print()

palavraASubstituir = input("Digite uma palavra para substituir na lista: ")
novaPalava = input("Digite a palavra que irá substitui-la: ")
print()

while cont < tamanhoListaPalavras:
    if listaPalavras[cont] == palavraASubstituir:
        listaPalavraRemovida.append(novaPalava)
    elif listaPalavras[cont] != palavraASubstituir:
        listaPalavraRemovida.append(listaPalavras[cont])
    
    cont += 1

print(f"A lista ficou dessa forma após a substituição da palavra: {listaPalavraRemovida}")
print()