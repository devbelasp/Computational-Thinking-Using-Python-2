try:
    n1 = int(input('N1: '))
    n2 = int(input('N2: '))
    resultado = n1/n2

    lista = [1,2,3]

    for n in lista:
        print(f'Elemento: {n}')

    num = int(input('Número: '))
    lista.append(num)

    print(lista[3])
except ValueError:
    print('Entrada inválida - apenas números')
except IndexError:
    print('Erro: índice fora da lista')
except ZeroDivisionError:
    print('Erro: divisão por ZERO')
except Exception as e:
    print(f'Erro genérico! {e}')
else: #opcional
    print('Deu tudo certo!')
finally: #opcional
    print('Encerrando o programa!')