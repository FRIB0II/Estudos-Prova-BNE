from random import randint

print()

totalVitoriasJogador = 0
totalVitoriasBot = 0

while totalVitoriasBot == 0:
    
    escolhaJogador = int(input("Escolha um número: "))
    imparParJogador = str(input("Ímpar ou Par [I/P]?: "))
    print()

    imparParJogadorFormatada = imparParJogador.upper()

    escolhaBot = randint(0, escolhaJogador + 100)

    if imparParJogadorFormatada == "I":
        imparParBot = "P"
    elif imparParJogadorFormatada == "P":
        imparParBot = "I"

    soma = escolhaJogador + escolhaBot
    
    if soma % 2 == 0:
        print(f"Você jogou {escolhaJogador} e o bot jogou {escolhaBot}. Total deu {soma}, deu Par.")
        if imparParJogadorFormatada == "P":
            print("Você venceu esta rodada!")
            print()
            totalVitoriasJogador += 1
        else:
            print("Você perdeu!")
            print()
            totalVitoriasBot += 1
            break
    elif soma % 3 == 0:
        print(f"Você jogou {escolhaJogador} e o bot jogou {escolhaBot}. Total deu {soma}, deu Impar.")
        if imparParJogadorFormatada == "I":
            print("Você venceu esta rodada!")
            print()
            totalVitoriasJogador += 1
        else:
            print("Você perdeu!")
            print()
            totalVitoriasBot += 1
            break

print(f"Você venceu do bot {totalVitoriasJogador} vezes!")

print()