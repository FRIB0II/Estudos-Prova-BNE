from random import randint
from time import sleep

# Essa função faz a validação do número escolhido pelo usuário ->
# Para se certificar que o número está entre o intervalo definido.
def foraDeAlcance(numeroEscolhido):
   
    if numeroEscolhido < 0 or numeroEscolhido > 10:
        while numeroEscolhido < 0 or numeroEscolhido > 10:
            print("Valor incorreto! O número precisa estar entre 0 e 10!")
            sleep(2)
            numeroEscolhido = int(input("Digite novamente: "))
            print()

# Inicio do jogo.
print()
print("Seja bem vindo! este é o jogo da adivinhação.")
sleep(2)
print("Você precisa escolher um número entre 0 e 10.")
sleep(2)
print("Caso o número digitado seja igual ao que o bot escolheu você ganha!.")
sleep(2)
print("Preparado? Vamos começar!")
sleep(2)
print()

# Definição de variáveis.
numeroEscolhidoJogador = int(input("Digite um número: "))
numeroDePalpites = 0
numeroEscolhidoBot = randint(0, 10)
print()

foraDeAlcance(numeroEscolhidoJogador)    

# Lógica do jogo.
# Enquanto o número escolhido pelo jogador for diferente daquele escolhido pelo bot ->
# O usuário terá de informar o número novamente, até acertar.
while numeroEscolhidoJogador != numeroEscolhidoBot:
    
    numeroDePalpites += 1
    print(f"Tentativas = ({numeroDePalpites}).")
    print("Número errado! escolha novamente.")
    foraDeAlcance(numeroEscolhidoJogador)
    sleep(1)
    numeroEscolhidoJogador = int(input("Digite um número: "))
    numeroEscolhidoBot = randint(0, 10)
    print()

# Mensagem escrita ao acertar o número.
print(f"Você acertou! Foram necessários {numeroDePalpites} para ganhar o jogo.")
print()