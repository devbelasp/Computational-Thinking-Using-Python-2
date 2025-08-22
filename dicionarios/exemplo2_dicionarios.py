'''
Principais métodos (mais comuns)
- keys(): retorna uma "visão" de todas as chaves do dicionário
- values(): retorna uma "visão" de todos os valores do dicionário
- items(): retorna uma "visão" dos pares de chave-valor do dicionário
- get(): acessa um valor de forma segura (retornando um valor padrão quando não encontrar o elemento)
'''

carro = {
    "marca" : "Jeep",
    "modelo" : "Compass",
    "ano" : 2025
}

#iterando sobre as chaves do dicionário - metodo keys()
for chave in carro.keys():
    print(chave)

#iterando sobre os valores do dicionário - metodo values()
for valor in carro.values():
    print(valor)

#iterando sobre a chave e valor do dicionário - metodo items()
for chave, valor in carro.items():
    print(f'{chave} : {valor}')

#acesso a uma chave inexistente
#print(carro['motor'])

#acesso a uma chave com o metodo get()
motor = carro.get('motor', 'não especificado!')
print(f'motor: {motor}')

print(f'marca: {carro.get('marca')}')

