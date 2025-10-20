"""
Algoritmo Merge Sort - Ordenação por intercalação ou fusão
- Algoritmo recursivo
- "Dividir para conquistar"
- Considerado um dos algoritmos mais eficientes de propósito geral

Complexidade: O(n log n) (pior caso ou caso médio) ou O(n), como melhor caso

"""

def merge_sort(lista):
    """
    Algoritmo Merge Sort - Ordenação por intercalação
    """
    if len(lista) > 1:

        meio = len(lista) // 2 #divisão inteira

        #fatiamento
        L = lista[:meio]
        R = lista[meio:]

        #chamada recursiva
        merge_sort(L)

        merge_sort(R)

        #variaveis de controle
        # i - fará o controle da lista L
        # j - fará o controle da lista R
        # k - fará o controle da lista anterior a recursão
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i+=1
            else:
                lista[k] = R[j]
                j+=1
            k+=1

        #verificação dos elementos da lista L
        while i < len(L):
            lista[k] = L[i]
            i+=1
            k+=1

        #verificação dos elementos da lista R
        while j < len(R):
            lista[k] = R[j]
            j+=1
            k+=1

    return lista

#Programa Principal
lista = [38, 27, 43, 3, 9, 82, 10]
print(f'Lista Original: {lista}')
merge_sort(lista)
print(f'Lista Ordenada: {lista}')