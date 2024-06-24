print()
numero1 = int(input("Digite um número: "))
numero2 = int(input("Agora digite outro número: "))
print()

def menu():
    print("Você tem as seguintes opções:")
    print("[1] = Somar.")
    print("[2] = Multiplicar.")
    print("[3] = Maior.")
    print("[4] = Novos números.")
    print("[5] = Sair do programa.")
    print()

    escolha = int(input("Qual você deseja escolher?: "))
    print()
    return escolha

escolha = menu()

while escolha != 5:

    if escolha == 1:
        soma = numero1 + numero2
        print(f"A soma é: {soma}.")
        print("-" * 20 )
        print()
        escolha = menu()

    if escolha == 2:
        multiplicacao = numero1 * numero2
        print(f"A multiplicação é: {multiplicacao}.")
        print("-" * 20 )
        print()
        escolha = menu()

    if escolha == 3:
        if numero1 > numero2:
            print(f"O número {numero1} é o maior número!")
            print("-" * 20 )
        else:
            print(f"O número {numero2} é o maior número!")
            print("-" * 20 )
        print()
        escolha = menu()

    if escolha == 4:
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Agora digite outro número: "))
        print()
        escolha = menu()

print("Fim do programa.")
print()