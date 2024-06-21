def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Troca os elementos de posição
    return lista

# Exemplo de uso:
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
print(alist)
