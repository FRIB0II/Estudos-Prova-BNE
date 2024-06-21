def cabecalho(data, nome):
    print("+--------------------+")
    print(f"|Data: {data}       |")
    print(f"|Nome: {nome}    |")
    print("+--------------------+")

    
nome = input("Digite seu nome: ")
data = input("Digite a data (dd/mm/aaaa): ")
cabecalho(nome, data)
