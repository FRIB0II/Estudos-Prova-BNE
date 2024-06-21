listaNumeros = [10, 50, 60, 75, 67, 87, 98, 100, 12, 14, 16, 12, 24, 17, 87, 9, 32, 45, 67, 78];
numeroExiste = False;

numeroRequerido = int(input("Digite um número para buscar no vetor: "));

for numero in listaNumeros:
    if numero == numeroRequerido:
        numeroExiste = True;
        break;

if numeroExiste == False:
    print(f"O número {numeroRequerido} não existe no vetor.");
else:
    print(f"O número {numeroRequerido} existe no vetor.");
