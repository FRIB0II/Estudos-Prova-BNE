def soma_vetores(vetor1, vetor2):
    # Verifique se os vetores têm o mesmo tamanho
    if len(vetor1) != len(vetor2):
        return "Os vetores devem ter o mesmo tamanho!"
    # Calcule a soma dos elementos
    # ListComprehension
    resultado = [v1 + v2 for v1, v2 in zip(vetor1, vetor2)]
    return resultado

vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
print(soma_vetores(vetor1, vetor2))  # Deve imprimir [5, 7, 9]
