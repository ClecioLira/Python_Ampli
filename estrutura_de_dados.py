
#! OBJETOS DO TIPO SEQUÊNCIA: TEXTO, LISTAS E TUPLAS.
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

#! LISTAS
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

#! COMPREENSÃO DE LISTA
# linguagens = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'Swift', 'Go']
# print('Antes da listcomp = ', linguagens)
# linguagens = [item.lower() for item in linguagens]
# print('Depois da listcomp =', linguagens)

# linguagens = '''Python Java JavaScript C C++ C# Swift Go Kotlin'''.split()
# linguagens_java = [item for item in linguagens if 'Java' in item]
# print(linguagens_java)

#! FUNÇÕES MAP() E FILTER()
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

#! TUPLAS
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

#! OBJETOS DO TIPO SET
# vogais_1 = {'aeiou'}
# print(type(vogais_1), vogais_1)

# vogais_2 = set('aeiouaaa')
# print(type(vogais_2), vogais_2)

# vogais_3 = set(['a', 'e', 'i', 'o', 'u'])
# print(type(vogais_3), vogais_3)

# vogais_4 = set(('a', 'e', 'i', 'o', 'u'))
# print(type(vogais_4), vogais_4)

# banana = set('banana')
# print(type(banana), banana)

# def create_report():
#     componentes_verificados = set(['caixa de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub', 'impressora', 'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'])
#     componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])

#     quantidade_componentes_verificados = len(componentes_verificados)
#     quantidade_componentes_com_defeito = len(componentes_com_defeito)

#     componentes_ok = componentes_verificados.difference(componentes_com_defeito)

#     print(f'Foram verificados {quantidade_componentes_verificados} componentes.')
#     print(f'{quantidade_componentes_com_defeito} componentes apresentaram defeitos.')

#     print('Os componentes que podem ser vendidos sao:')
#     for item in componentes_ok:
#         print(item)
#     print('Os componentes que não podem ser vendidos sao:')
#     for item in componentes_com_defeito:
#         print(item)
# create_report()

#! OBJETOS DO TIPO MAPPING / DICTIONARIO
# dici_1 = {}
# dici_1['nome'] = 'João'
# dici_1['idade'] = 12
# print(dici_1)

# dici_2 = {'nome': 'Clécio', 'idade': 22}
# print(dici_2)

# dici_3 = dict([('nome', 'jõao'), ('idade', 30)])
# print(dici_3)

# dici_4 = dict(zip(['nome', 'idade'], ['João', 30]))

# cadastro = {
#     'nome': ['joão', 'maria', 'pedro', 'marcela'],
#     'cidade': ['sao paulo', 'rio de janeiro', 'curitiba', 'belo horizonte'],
#     'idade': [25, 33, 75, 23]
# }
# print('len(cadastro) =', len(cadastro))
# print("cadastro.keys() =", cadastro.keys())
# print("cadastro.values() =", cadastro.values())
# print("cadastro.items() =", cadastro.items())

# print("\n cadastro['nome'] = ", cadastro['nome'])
# print("\n cadastro['nome'][2] = ", cadastro['nome'][2])
# print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])

# print(len(cadastro['nome']))
# print(len(cadastro['idade']))
# print(len(cadastro['cidade']))
# quantidade_de_items = sum([len(cadastro[chave]) for chave in cadastro])
# print(f'Quantidade de elementos no dicionario = {quantidade_de_items}')

dados_1 = {
  'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],

  'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],

  'enviado': [False, False, False, False, False, False, False, True, False, False]
}
dados_2 = {
  'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],

  'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],

  'enviado': [False, False, False, True, True, True, False, True, True, False]
}

def extrair_email(dici1, dici2):
    lista_1 = list(zip(dici1['nome'], dici1['email'], dici1['enviado']))
    # print(f'Mostra da lista 1 = {lista_1[0]}')

    lista_2 = list(zip(dici2['nome'], dici2['email'], dici2['enviado']))
    dados = lista_1 + lista_2
    print(f'Mostra dos dados = {dados[0:20]}\n')

    emails = [item[1] for item in dados if not item[2]]
    return emails

emails = extrair_email(dici1 = dados_1, dici2 = dados_2)
print(f'Emails a serem enviados = {emails}')