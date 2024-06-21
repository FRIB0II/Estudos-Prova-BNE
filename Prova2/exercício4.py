soma = 0;

for numero in range(100):
    numero += 1;
    if numero % 5 == 0:
        soma = soma + numero;

print(f"A soma dos números multiplos de 5 é: {soma}");
    