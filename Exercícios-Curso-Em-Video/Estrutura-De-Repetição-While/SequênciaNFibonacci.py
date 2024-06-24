print()

# Recebe a quantidade de números a ser mostrado.
quantidadeSequencia = int(input("Quantos números você deseja ver?: "))
print()

# Definição de variáveis.
contador = 0
aux = 0

numeroAnterior = 0
numeroAtual = 0
proximoNumero = 0


# Comentando sobre a lógica do código.
# Eu decidi tratar os 2 primeiros valores como exceção na hora de realizar as contas ->
# Eu decidi que os dois primeiros valores a serem mostrados seriam os dois primeiros valores do contador.
# Além disso o número atual, anterior e próximo recebem o último valor do contador ao sair da exceção, nesse caso 1.

# O resto da lógica fica da seguinte forma:
# Quando a exceção for tratada ele irá iterar 1 ao contador e mostrar o próximo número, nesse caso 1.
# Após isso ele irá verificar qual será o próximo número, usando a seguinte fórmula -> proximoNumero = numeroAtual(1) + numeroAnterior(1).
# Em seguida todos os valores recebem o valor do seu correspondente ->
# Sendo eles -> numeroAnterior(1 -> 1) = numeroAtual(1) e numeroAtual(1 -> 2) = proximoNumero(2). Dessa forma eu consigo calcular o próximo número da ->
# Sequência. 

# Enquanto o contador for menor que a quantidade de números ->
# A serem mostrados ele irá realizar as contas.
while contador < quantidadeSequencia:
    
    if aux == 0 or aux == 1:
        numeroAtual = contador
        proximoNumero = numeroAtual
        numeroAnterior = numeroAtual
        print(contador, end=" -> ")
        aux += 1
    else:
        print(proximoNumero, end=' -> ')
        proximoNumero = numeroAtual + numeroAnterior
        numeroAnterior = numeroAtual
        numeroAtual = proximoNumero
        
    contador +=1

print()