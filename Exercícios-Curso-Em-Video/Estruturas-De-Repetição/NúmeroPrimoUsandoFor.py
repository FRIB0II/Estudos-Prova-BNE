print()
numero = int(input("Digite um número: "))
print()
maximoDivisores = 0

for contador in range(1, numero + 1):
    
    if numero % contador == 0:
        primo = True
        maximoDivisores +=1
    elif maximoDivisores > 2:
        primo = False
        break

if primo == True:
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo!")

print()