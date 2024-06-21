def vermaior(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
        
numero = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

resposta = vermaior(numero, numero2, numero3)
print(f"O maior número é o {resposta}.")