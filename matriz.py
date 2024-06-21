def criar_matriz(num_linhas, num_colunas):
    matriz = []
    for _ in range(num_linhas):
        linha = []
        for _ in range(num_colunas):
            elemento = int(input(f"Digite o elemento ({_},{_}): "))
            linha.append(elemento)
        matriz.append(linha)
    
    return matriz

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

# Exemplo de uso:
num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))
minha_matriz = criar_matriz(num_linhas, num_colunas)
exibir_matriz(minha_matriz)
