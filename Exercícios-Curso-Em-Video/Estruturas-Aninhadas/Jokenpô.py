from random import choice
from time import sleep

# Lista de opções do jogador e do bot.
# A lista do bot é maior para ter menos chances de empate
listaDeOpcoes = ["Pedra", "Papel", "Tesoura"]
listaDeOpcoesBot = ["Pedra", "Papel", "Tesoura", "Pedra", "Papel", "Tesoura"]

# Lista de jogadas possíveis, sendo o primeiro elemento referente a escolha do jogador ->
# E o segundo elemento a jogada do bot.
listaJogadaPedra = ["Pedra", "Tesoura"]

listaJogadaPapel = ["Papel", "Pedra"]

listaJogadaTesoura = ["Tesoura", "Papel"]

# Pontos de cada um.
pontosUsuario = 0
pontosBot = 0

# Tela de inicio.
print()
print("Olá! Este é o famoso jogo de jokenpô! Escolha uma opção: ")
print("Pedra = 0")
print("Papel = 1")
print("Tesoura = 2")
print("-" * 20)

# Lógica do jogo.
# O jogo continua até que um jogador ganhe 3 pontos.
while pontosUsuario <= 3 or pontosBot <= 3:

    # Escolha do jogador.
    # Com base no número escolhido será selecionada um dos elementos da lista de opções.
    numeroEscolhido = int(input("Qual opção? : "))
    print("Jo")
    sleep(0.5)
    print("Ken")
    sleep(0.5)
    print("Pô!!!")
    sleep(0.5)
    escolhaUsuario = listaDeOpcoes[numeroEscolhido]
    print()

    # Escolha do bot.
    # É feito de forma aleatória com base na lista de opções.
    escolhaBot = choice(listaDeOpcoes)

    # Lista da jogada.
    # Armazena numa lista as escolhas do bot e do jogador.
    listaJogada = [escolhaUsuario, escolhaBot]

    # Mosta na tela o que cada jogador escolheu.
    print(f"Você escolheu: {escolhaUsuario}.")
    print(f"O bot escolheu: {escolhaBot}.")
    print()

    # Resultado do jogo.
    # Com base nas escolhas do jogador decide quem ganha a rodada.
    # Compara a lista com a jogada dos jogadores com a lista da jogada feita ->
    # Onde o jogador ganha.
    if escolhaUsuario == escolhaBot:
        print("Empate!")
        print()
    elif listaJogada == listaJogadaPedra or listaJogada == listaJogadaPapel or listaJogada == listaJogadaTesoura:
        print("Ponto para você!")
        pontosUsuario += 1
        print(f"Seus pontos: {pontosUsuario}. Pontos do bot: {pontosBot}.")
        print("-" * 20)
        print()
    else:
        print("Ponto para o bot!")
        pontosBot += 1
        print(f"Seus pontos: {pontosUsuario}. Pontos do bot: {pontosBot}.")
        print("-" * 20)
        print()

    # Verifica quem ganhou o jogo.
    if pontosUsuario == 3:
        print("Você ganhou!")
        print()
        break
    elif pontosBot == 3:
        print("O bot ganhou!")
        print()
        break
