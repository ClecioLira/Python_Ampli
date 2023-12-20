
#! ALGORITMO DE BUSCA
# nomes = 'João Marcela Sonia Daryl Vernon Eder Mechelle Edan Igor Ethan Reed Travis Hoyt'.split()
# print('Marcela' in nomes)
# print('Roberto' in nomes)

#! BUSCA LINEAR / BUSCA SEQUENCIAL
# def executar_busca_linear(lista, valor):
#     for elemento in lista:
#         if valor == elemento:
#             return True
#     return False
# numeros = []
# numeros = list(range(5,50))
# print(numeros)
# busca = executar_busca_linear(numeros, 50)
# print(busca)

# vogais = 'aeiou'
# resultado = vogais.index('e')
# print(resultado)

# def procurar_valor(lista, valor):
#     tamanho_lista = len(lista)
#     for i in range(tamanho_lista):
#         if valor == lista[i]:
#             return i
#     return None
# vogais = 'aeiou'
# resultado = procurar_valor(lista=vogais, valor='u')
# if resultado != None:
#     print(f'Valor encontrado na possição {resultado}')
# else:
#     print('Valor não encontrado')

#! BUSCA BINÁRIA
# def executar_busca_binaria(lista, valor):
#     minimo = 0
#     maximo = len(lista) - 1
#     while minimo < maximo:
#         # Encontra o elemento que divide a lista ao meio
#         meio = (minimo + maximo) // 2
#         # Verifica se o valor procurado está a esqueda ou direita do valor central
#         if valor < lista[meio]:
#             maximo = meio - 1
#         elif valor > lista[meio]:
#             minimo = meio + 1
#         else:
#             return True # Se o valor for encontrado para aqui
#     return False # Se chegar até aqui, significa que o valor nao foi encontrado
# lista = list(range(1,51))
# print(lista)
# print('\n',executar_busca_binaria(lista=lista, valor=10))
# print('\n',executar_busca_binaria(lista=lista, valor=25))

# def procurar_valor(lista, valor):
#     minimo = 0
#     maximo = len(lista) - 1
#     while minimo <= maximo:
#         meio = (minimo + maximo) // 2
#         if valor < lista[meio]:
#             maximo = meio - 1
#         elif valor > lista[meio]:
#             minimo = meio + 1
#         else:
#             return meio
#     return None
# vogais = ['a', 'e', 'i', 'o', 'u']
# resultado = procurar_valor(lista=vogais, valor='e')
# if resultado:
#     print(f'Valor encontrado na posição {resultado}')
# else:
#     print('Valor não encontrado')

# Implementar o algoritmo de busca linear
def executar_busca_linear(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return True
    return False

def criar_lista_dedup(lista):
    lista_dedup = []
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace('-', '').replace('.', '')
        if len(cpf) == 11:
            if not executar_busca_linear(lista_dedup, cpf):
                lista_dedup.append(cpf)
    return lista_dedup

def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup(lista_cpfs)
    print(lista_dedup)

lista_cpfs = ['111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
testar_funcao(lista_cpfs)