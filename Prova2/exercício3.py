num = int(input("Digite um número: "));

cont = 1;
aux = 1;

while cont <= num:
    aux = aux * cont;
    cont += 1;

print();
print(f"O fatorial é: {aux}");