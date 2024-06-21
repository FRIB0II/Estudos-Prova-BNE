listaNumeros = [];
cont = 1;
soma = 0;
media = 0;

while cont <= 10:
    num = int(input("Digite um número: "));
    listaNumeros.append(num);
    soma += num;
    cont += 1;

media = soma / (cont-1);

print();

print(f"A soma de todos os números é {soma}. E a média é {media}");