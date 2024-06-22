tamanhoLista = int(input("Informe o tamanho da lista: "))
print()

listaNumerica = []
cont = 0
maiorNumero = 0
menorNumero = 0

while cont < tamanhoLista:

    num = int(input("Digite um número para inserir na lista: "))
    listaNumerica.append(num)
    cont += 1

# Busca o maior número
for numero in listaNumerica:

    if maiorNumero < numero:
        maiorNumero = numero

# Busca o menor número
# Seu valor inicial é o maior número da lista
# Assim ele consegue achar o menor sem retornar zero caso só exista números maiores que 0
menorNumero = maiorNumero
for numero in listaNumerica:
    if menorNumero > numero:
        menorNumero = numero

print()
print(f"O maior número na lista é: {maiorNumero}")
print(f"O menor número na lista é: {menorNumero}")
print()


        