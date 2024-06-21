# Inicializar um vetor
vetor = [0] * 10

# O cont sempre será 0 caso se use vetores.
cont = 0

while cont < 10:
    num = int(input("Insira um número: "))
    vetor[cont] = num
    cont += 1

print(vetor)
