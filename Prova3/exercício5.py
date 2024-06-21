listaNumeros = [10, 50, 60, 75, 67, 87, 98, 100, 12, 14, 16, 12, 24, 17, 87, 9, 32, 45, 67, 78];
quantidadeNumeros = 0;

for numero in listaNumeros:
    if numero > 50:
        print(numero);
        quantidadeNumeros += 1;

print();
print(f"A quantidade de números acima de 50 é: {quantidadeNumeros}");