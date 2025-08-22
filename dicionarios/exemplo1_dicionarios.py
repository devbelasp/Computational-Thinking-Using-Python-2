'''
Dicionários

Criar um dicionário com informações sobre uma pessoa

Sintaxe:
Construtor: dict()
nome = {"chave" : valor}
'''

pessoa = {
    'nome' : 'João',
    'idade' : 30,
    'cidade' : 'São Paulo'
}

#imprimindo o dicionário pessoa
print(pessoa)

#acessando um elemento através da chave
print(f'Nome: {pessoa['nome']}')

#adicionando um novo elemento ao dicionário
pessoa['profissão'] = 'Desenvolvedor'
print(pessoa)

#alterando um valor de uma chave
pessoa['idade'] = 40
print(f'Nova idade: {pessoa['idade']}')

print(pessoa)

#removendo um elemento do dicionário
del pessoa['cidade']

print(pessoa)
