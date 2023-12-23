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
# (i) dividir o problema em vários subproblemas
# (ii) conquistar os subproblemas, resolvendo-os recursivamente – se os tamanhos dos subproblemas forem pequenos o suficiente, apenas resolva os subproblemas de maneira direta
# (iii) combine as soluções dos subproblemas na solução do problema original.

# def executar_merge_sort(lista):
#     if len(lista) <= 1: 
#         return lista
#     else:
#         meio = len(lista) // 2
#         esquerda = executar_merge_sort(lista[:meio])
#         direita = executar_merge_sort(lista[meio:])
#         return executar_merge(esquerda, direita)
    
# def executar_merge(esquerda, direita):
#     sub_lista_ordenada = []
#     topo_esquerda, topo_direita = 0, 0
#     while topo_esquerda < len(esquerda) and topo_direita < len(direita):
#         if esquerda[topo_esquerda ] <= direita[topo_direita]:
#             sub_lista_ordenada.append(esquerda[topo_esquerda])
#             topo_esquerda += 1
#         else:
#             sub_lista_ordenada.append(direita[topo_direita])
#             topo_direita += 1
#     sub_lista_ordenada += esquerda[topo_esquerda:]
#     sub_lista_ordenada += direita[topo_direita:]
#     return sub_lista_ordenada

# lista = [10, 9, 5, 8, 11, -1, 3]
# print(executar_merge_sort(lista))

#* QUICKSORT
# def executar_quicksort(lista, inicio, fim):
#     if inicio < fim:
#         pivo = executar_particao(lista, inicio, fim)
#         executar_quicksort(lista, inicio, pivo-1)
#         executar_quicksort(lista, pivo+1, fim)
#     return lista

# def executar_particao(lista, inicio, fim):
#     pivo = lista[fim]
#     esquerda = inicio
#     for direita in range(inicio, fim):
#         if lista[direita] <= pivo:
#             lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
#             esquerda += 1
#     lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
#     return esquerda

# lista = [10, 9, 5, 8, 11, -1, 3]
# print(executar_quicksort(lista, inicio=0, fim=len(lista)-1))

# def executar_quicksort_2(lista):
#     if len(lista) <= 1:
#         return lista
#     pivo = lista[0]
#     iguais = [valor for valor in lista if valor == pivo]
#     menores = [valor for valor in lista if valor < pivo]
#     maiores = [valor for valor in lista if valor > pivo]
#     return executar_quicksort_2(menores) + iguais + executar_quicksort_2(maiores)

# lista = [10, 9, 5, 8, 11, -1, 3]
# print(executar_quicksort_2(lista))

# def executar_merge_sort(lista, inicio = 0, fim = None):
#     if not fim:
#         fim = len(lista)

#     if fim - inicio > 1:
#         meio = (inicio + fim) // 2
#         executar_merge_sort(lista, inicio, meio)
#         executar_merge_sort(lista, meio, fim)
#         executar_merge(lista, inicio, meio, fim)
#     return lista

# def executar_merge(lista, inicio, meio, fim):
#     esquerda = lista[inicio:meio]
#     direita = lista[meio:fim]
#     topo_esquerda = topo_direita = 0
#     for p in range(inicio, fim):
#         if topo_esquerda >= len(esquerda):
#             lista[p] = direita[topo_direita]
#             topo_direita += 1
#         elif topo_direita >= len(direita):
#             lista[p] = esquerda[topo_esquerda]
#             topo_esquerda += 1
#         elif esquerda[topo_esquerda] < direita[topo_direita]:
#             lista[p] = esquerda[topo_esquerda]
#             topo_esquerda += 1
#         else:
#             lista[p] = direita[topo_direita]
#             topo_direita += 1

# def executar_busca_binaria(lista, valor):
#     minimo = 0
#     maximo = len(lista) - 1
#     while minimo <= maximo:
#         meio = (minimo + maximo) // 2
#         if valor < lista[meio]:
#             maximo = meio - 1
#         elif valor > lista[meio]:
#             minimo = meio + 1
#         else:
#             return True
#     return False

# def criar_lista_dedup_ordenada(lista):
#     lista = [str(cpf).replace('.', '').replace('-', '') for cpf in lista]
#     lista = [cpf for cpf in lista if len(cpf) == 11]
#     lista = executar_merge_sort(lista)

#     lista_dedup = []
#     for cpf in lista:
#         if not executar_busca_binaria(lista_dedup, cpf):
#             lista_dedup.append(cpf)
#     return lista_dedup

# def testar_funcao(lista_cpfs):
#     lista_dedup = criar_lista_dedup_ordenada(lista_cpfs)
#     print(lista_dedup)

# lista_cpfs = ['44444444444', '111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']

# print(testar_funcao(lista_cpfs))

# def valor_lista():
#     for i in range(1, 5):
#         lista.append(int(input(f'Digite o valor da {i}° prova: ')))

# def media():
#     s = 0
#     for i in range(len(lista)):
#         s += lista[i]
#     m = s / len(lista)
#     return m

# lista = []
# valor_lista()
# print(f'Sua média é: {media()}')

def busca_binaria(lista, item):
    prim = 0
    ult = len(lista)
    found = False

    while prim <= ult and not found:
        meio = (prim + ult) // 2
        if lista[meio] == item:
            found = True
        else:
            if item < lista[meio]:
                ult = meio - 1
            else:
                prim = meio + 1
    return found

lista = [1, 2, 4, 5, 6, 7, 8, 9, 10]
print(busca_binaria(lista, 3))