print()

primeiroTermo = int(input("Informe o primeiro termo da pa: "))
razao = int(input("Informe a razão da pa: "))
contador = 0
proximoTermo = primeiroTermo

while contador < 10:
    print(proximoTermo, end=" -> ")
    proximoTermo += razao
    contador += 1

print("Fim.")
print()