def vetor_ordenado(vetor):
    # all verifica se todos as expressões são verdadeiras (dentro de parênteses)
    return all(vetor[i] <= vetor[i + 1] for i in range(len(vetor) - 1))

vetor1 = [1, 2, 3, 4, 5]
vetor2 = [5, 3, 1, 2, 4]
print(vetor_ordenado(vetor1))  # Deve imprimir True
print(vetor_ordenado(vetor2))  # Deve imprimir False
