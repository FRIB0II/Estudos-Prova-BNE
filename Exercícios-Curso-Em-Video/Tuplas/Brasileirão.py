print()

timesBrasileirao = ('Flamengo', 'Palmeiras', 'Bahia', 'Botafogo', 'Athletico-PR', 'Bragantino', 'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético-MG',
'Fortaleza', 'Juventude', 'Criciúma', 'Cuiabá', 'Vasco', 'Atlético-GO', 'Vitória', 'Corinthians', 'Grêmio', 'Fluminense')

print("Top 20 do Brasileirão: ")
contador = 1
for posicao in range(0, 20):
    print(f"{contador}º{timesBrasileirao[posicao]}.")
    contador += 1
print()


print("Os 5 primeiros times do brasileirão são: ")
for time in range(0 , 5):
    print(f"{time+1}º{timesBrasileirao[time]}")
print()

print(f"Os 4 últimos times do top vinte são:")
for posicao in range(1, 5):
    print(f"{21 - posicao}º{timesBrasileirao[-posicao]}")
print()

print("O time chapecoense não se encontra no top 20 )=")
print()

print(f"O vasco de encontra na {timesBrasileirao.index("Vasco")}º posição!")
print()