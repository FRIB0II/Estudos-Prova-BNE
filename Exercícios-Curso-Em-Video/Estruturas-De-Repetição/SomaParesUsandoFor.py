print()

soma = 0

for contador in range(0, 6):
    num = int(input("Insira um número: "))
    if num % 2 == 0:
        soma += num
    
print()
print(f"A soma dos números pares é: {soma}.")
print()