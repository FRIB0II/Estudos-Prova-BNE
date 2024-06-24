from datetime import datetime

print()

maiorDeIdade = 0
menorDeIdade = 0


for contador in range (1, 8):
    
    anoNascimento= int(input("Digite o ano do seu nascimento: "))
    ano = datetime.now()
    verificaIdade = ano.year - anoNascimento

    if verificaIdade >= 21:
        maiorDeIdade += 1
    else:
        menorDeIdade += 1

print()
print(f"{maiorDeIdade} pessoas são maiores de idade.")
print(f"{menorDeIdade} pessoas são menores de idade.")
print()