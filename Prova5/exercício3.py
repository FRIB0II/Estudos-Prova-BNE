def Soma(num, num2):
    resultado = num + num2
    return resultado


def Subtracao(num, num2):
    resultado = num - num2
    return resultado


def Multiplicacao(num, num2):
    resultado = num * num2
    return resultado


def Divisao(num, num2):
    resultado = num / num2
    return resultado


numero = int(input("Digite um número: "))
operacao = input("Informe a operação: ")
numero2 = int(input("Digite outro número: "))

match(operacao):
    case '+':
        retorno = Soma(numero, numero2)
    case '-':
        retorno = Subtracao(numero, numero2)
    case '*':
        retorno = Multiplicacao(numero, numero2)
    case '/':
        retorno = Divisao(numero, numero2)
    
print("____________")
print(f"Resultado: {retorno}")