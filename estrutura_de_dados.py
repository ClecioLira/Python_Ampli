# OBJETOS DO TIPO SEQUÊNCIA: TEXTO, LISTAS E TUPLAS.
# texto = "Aprendendo Python na disciplina de linguagem de programação."
# print(f'Tamanho do texto = {len(texto)}')
# print(f'Python in texto = {'Python' in texto}')
# print(f'Quantidade de y no texto = {texto.count('y')}')
# print(f'As 5 primeiras letras do texto são = {texto[0:6]}')
# print(texto.upper())
# print(texto.replace('i', 'XX'))
# palavras = texto.split()
# print(f'Palavras = {palavras}')
# print(f'Quantidade de palavras = {len(palavras)}')

# LISTAS
# vogais = ['a', 'e', 'i', 'o', 'u']
# for vogal in vogais:
#     print(f'Posição = {vogais.index(vogal),} Valor = {vogal}')

# vogais = []
# print(f'Tipo do objeto vogais = {type(vogais)}')
# vogais.append('a')
# vogais.append('e')
# vogais.append('i')
# vogais.append('o')
# vogais.append('u')
# print(vogais)

# frutas = ['maça', 'banana', 'uva', 'mamaõ', 'maça', 'abacaxi']
# notas = [8.7, 5.2, 10, 3.5]
# print('maça' in frutas)
# print('abacate' in frutas)
# print('abacate' not in frutas)
# print(min(frutas))
# print(max(notas))
# print(frutas.count('maça'))
# print(frutas + notas)
# print(2 * frutas)

# lista = ['Python', 30.61, 'Java', 51, ['a' , 'b', 20], 'maça']
# print(f'Tamanho da lista = {len(lista)}')
# for i, item in enumerate(lista):
#     print(f'Posição = {i}, \t valor = {item}, \t tipo individual = {type(item)}')
# print('\nEXEMPLOS DE SLICE:\n')
# print("lista[1] = ", lista[1])
# print("lista[0:2] = ", lista[0:2])
# print("lista[:2] = ", lista[:2])
# print("lista[3:5] = ", lista[3:5])
# print("lista[3:6] = ", lista[3:6])
# print("lista[3:] = ", lista[3:])
# print("lista[-2] = ", lista[-2])
# print("lista[-1] = ", lista[-1])
# print("lista[4][1] = ", lista[4][1])

# COMPREENSÃO DE LISTA
# linguagens = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'Swift', 'Go']
# print('Antes da listcomp = ', linguagens)
# linguagens = [item.lower() for item in linguagens]
# print('Depois da listcomp =', linguagens)

# linguagens = '''Python Java JavaScript C C++ C# Swift Go Kotlin'''.split()
# linguagens_java = [item for item in linguagens if 'Java' in item]
# print(linguagens_java)

# FUNÇÕES MAP() E FILTER()
# print("Exemplo 1")
# linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
# nova_lista = map(lambda x: x.lower(), linguagens)
# print(f'A nova lista é = {nova_lista}')
# nova_lista = list(nova_lista)
# print(f'Agora sim é a nova lista = {nova_lista}')

# print("\n\nExemplo 2")
# numeros = [0, 1, 2, 3, 4, 5]
# quadrados = list(map(lambda x: x*x, numeros))
# print(f'Lista com o numero elevado a ele mesmo = {quadrados}')

# numeros = list(range(0, 21))
# numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
# numeros_impares = list(filter(lambda x: x % 2 == 1, numeros))
# print(numeros_pares)
# print(numeros_impares)

# TUPLAS
# vogais = ('a', 'e', 'i', 'o', 'u')
# print(f"Tipo do objeto vogais = {type(vogais)}")
# for i, item in enumerate(vogais):
#     print(f'Posição = {i}, valor = {item}')

# vogais = ()
# vogais.append('a')

# vogais = ('a', 'e', 'i', 'o', 'u')
# for item in enumerate(vogais):
#     print(item)
# print(tuple(enumerate(vogais)))
# print(list(enumerate(vogais)))