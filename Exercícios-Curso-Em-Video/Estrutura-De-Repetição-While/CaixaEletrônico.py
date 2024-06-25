print()

banco = "Banco do Brasil"
print("=" * 30)
print(" " * 7 + f"{banco}")
print("=" * 30)

valor = int(input("Que valor você deseja sacar?: "))

total = 0
total50 = 0
total20 = 0
total10 = 0
total1 = 0

total50 = valor / 50
print(f"Você vai receber {total50:.0f} notas de 50.")

total20 = valor
print()

print("=" * 30)
print(f"Volte semprea ao {banco}! Tenha um bom dia!")
print()