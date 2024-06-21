#Exercício 5

nome = input("Digite seu nome: ");
endereco = input("Digite seu endereço: ");
dataNascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ");
uf = input("Digite sua unidade federativa: ");
sexo = input("Digite seu gênero: ");
idade = int(input("Digite sua idade: "));

aluno = {
    "nome": nome,
    "endereco": endereco,
    "dataNascimento": dataNascimento,
    "uf": uf,
    "sexo": sexo,
    "idade": idade
}

print();

print(f"Seu nome é: {aluno['nome']}");
print(f"Seu endereco é: {aluno['endereco']}");
print(f"Sua data de nascimento é: {aluno['dataNascimento']}");
print(f"Sua unidade federativa é: {aluno['uf']}");
print(f"Seu gênero é: {aluno['sexo']}");
print(f"Sua idade é: {aluno['idade']} anos");