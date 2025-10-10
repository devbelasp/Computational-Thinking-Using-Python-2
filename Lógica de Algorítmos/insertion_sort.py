"""
Algoritmo Insertion Sort - Ordenação por Inserção
- Realiza a comparação elemento por elemento
- Parecido com um deck de cartas
- Percorrer a lista de entrada e, a cada iteração, remove um elemento e o insere na posição correta.

Complexidade: O(n^2) - pior caso | O(n) - melhor caso

"""

import time

def insertion_sort(lista):
    """
    Algoritmo de ordenação por inserção
    """
    n = len(lista)

    for i in range(1, n):
        pivo = lista[i]

        j = i - 1 #j representa o índice do elemento anterior
        while j>=0 and pivo<lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = pivo

#Programa Principal
lista = [12, 11, 13, 5, 6]
print(f'Lista Original: {lista}')
inicio = time.time()
insertion_sort(lista)
fim = time.time()
print(f'Lista Ordenada: {lista}')
print(f'Tempo: {(fim-inicio)}')