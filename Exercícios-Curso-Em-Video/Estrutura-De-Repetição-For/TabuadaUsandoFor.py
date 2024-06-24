print()
numeroTabuada = int(input("Digite um número para mostrar a sua tabuada: "))
print()

for contador in range(0, 11):
    multiplicacao = numeroTabuada * contador
    print(f"{numeroTabuada} X {contador} = {multiplicacao}.")
print()