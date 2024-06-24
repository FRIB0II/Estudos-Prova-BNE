# Primeiro termo da progressão.
print()
primeiroTermo = int(input("Informe o primero termo da p.a: "))

# Quantas casas a partir do primeiro número ele pula até chegar ao próximo.
razao = int(input("Informe a razão da pa: "))
print()

# TermoN = termo na posição N que eu quero encontrar.
for contador in range(1, 11):
    termoN = contador
    termoN = primeiroTermo + razao * (termoN - 1)
    print(f"Na {contador}º posição o termo é: {termoN}.")

print()