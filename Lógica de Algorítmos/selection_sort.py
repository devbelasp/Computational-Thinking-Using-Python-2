"""
Algoritmos de ordenação
Selection Sort (Ordenação por Seleção)

Trabalha em passes (iterações) - elemento por elemento
Troca o elemento, se ele for maior (ou menor)
- aumentando a parte ordenada e diminuindo a desordenada

Complexidade: 0(n^2)
"""

import time

def selection_sort(lista):
    """
    Ordena uma lista de números usando o algoritmo Selection Sort
    """

    tam = len(lista) #obter o tamanho da lista

    for i in range(tam):
        indice_minimo = i

        for j in range(i+1, tam):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        #realiza a troca (atribuição paralela)
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

def tempo():
    print('Início...')
    start = time.time()
    for i in range(10):
        print('.')
        time.sleep(1)
    end = time.time()
    print('Fim...')
    print(f'Tempo: {end-start}')


#Programa principal
lista_original = [64, 25, 12, 22, 11]
print(f'Lista original: {lista_original}')

inicio = time.time()
selection_sort(lista_original)
fim = time.time()

print(f'Lista Ordenada: {lista_original}')
print(f'Tempo: {fim-inicio}')

tempo()