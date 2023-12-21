# Quase todos os dados são mais úteis quando estão ordenados.
#! ORDENAR UMA SEQUENCIA
# lista = [10, 4, 1, 15, -3]
# lista_ordenada = sorted(lista)
# lista_ordenada2 = lista.sort()
# print(lista)
# print(f'Lista ordenada 1 = {lista_ordenada}')
# print(f'Lista ordenada 2 = {lista_ordenada2}')

#! ALGORITMO DE ORDENAÇÃO
# lista = [7, 4]
# if lista[0] > lista[1]:
#     aux = lista[1]
#     lista[1] = lista[0]
#     lista[0] = aux
# print(lista)

# lista = [5, -1]
# if lista[0] > lista[1]:
#     lista[0], lista[1] = lista[1], lista[0]
# print(lista)

#* SELECTION SORT
# def executar_selection_sort(lista):
#     n = len(lista)

#     for i in range(0, n):
#         index_menor = i
#         for j in range(i+1, n):
#             if lista[j] < lista[index_menor]:
#                 index_menor = j
#         lista[i], lista[index_menor] = lista[index_menor], lista[i]
#     return lista

# lista = [10, 9, 5, 8, 11, -1, 3]
# print(executar_selection_sort(lista))

# def executar_selection_sort2(lista):
#     lista_ordenada = []
#     while lista:
#         minimo = min(lista)
#         lista_ordenada.append(minimo)
#         lista.remove(minimo)
#     return lista_ordenada
# lista = [10, 9, 5, 8, 11, -1, 3]
# print(executar_selection_sort2(lista))

#* BUBBLE SORT
# def executar_bubble_sort(lista):
#     n = len(lista)
#     for i in range(n - 1):
#         for j in range(n - 1):
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#     return lista
# lista = [10, 9, 5, 8, 11, -1, 3]
# print(executar_bubble_sort(lista))

#* INSERTION SORT
# def executar_insertion_sort(lista):
#     n = len(lista)
#     for i in range(1, n):
#         valor_inserir = lista[i]
#         j = i - 1
    
#         while j >= 0 and lista[j] > valor_inserir:
#             lista[j + 1] = lista[j]
#             j -= 1
#             lista[j + 1] = valor_inserir
#     return lista
# lista = [10, 9, 5, 8, 11, -1, 3]
# print(executar_insertion_sort(lista))

#* MERGE SORT