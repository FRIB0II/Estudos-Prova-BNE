print()

primeiroTermo = int(input("Informe o primeiro termo da pa: "))
razao = int(input("Informe a razão da pa: "))
contador = 0
proximoTermo = primeiroTermo

print()
while contador < 10:
    print(proximoTermo, end=" -> ")
    proximoTermo += razao
    contador += 1

print()
print()
termosAdicionais = int(input("Quantos termos adicionais deseja ver?: "))
print("-" * 20)

while termosAdicionais != 0:
    contador = 0
    while contador < termosAdicionais:
        proximoTermo += razao
        print(proximoTermo, end=" -> ")
        contador += 1
    
    print()
    print()
    termosAdicionais = int(input("Quantos termos adicionais deseja ver?: "))
    print("-" * 20)
    
print()
print("Fim.")
print()