print()

total = 0
acimaDeMil = 0
Produto = 0 
maisBaratoPreco = 0
maisBaratoNome = ""

while True:
    
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: R$"))

    if maisBaratoPreco == 0:
        maisBaratoPreco = preco

    total += preco

    escolha = str(input("Deseja continuar? [S/N]: "))
    print("-="*21)
    print()

    if preco > 1000:
        acimaDeMil += 1

    if maisBaratoPreco >= preco:
        maisBaratoPreco = preco
        maisBaratoNome = produto

    if escolha == "N" or escolha == "n":
        break

print(f"O total da compra é: R${total:.2f}.")
print(f"{acimaDeMil} produtos custam mais de mil reais.")
print(f"O produto mais barato é {maisBaratoNome}, custando R${maisBaratoPreco:.2f} reais.")
print()