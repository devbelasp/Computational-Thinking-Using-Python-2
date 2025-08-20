'''
Exemplo com múltiplas exceções
'''

while True:
    try:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))
        result = n1/n2
        print(f'Resultado: {result}')
    except ZeroDivisionError:
        print('Erro: não é possível dividir por ZERO')
    except ValueError:
        print('Erro: caractere inválido')