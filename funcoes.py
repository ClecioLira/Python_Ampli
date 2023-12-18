# a = 2
# b = 1
# equacao = input('Digite a formula da equação linear (a * x + b): ')
# print(f'A entrada do usuario {equacao} é do tipo {type(equacao)}')
# for x in range(10):
#     y = eval(equacao)
#     print(f'Resultado da equação para x = {x} é {y}')


# def imprimirMensagem(disciplina, curso):
#     return f'Minha primeira função em python desenvolvida na disciplina: {disciplina}, do curso: {curso}.'
# resultado = imprimirMensagem("Python", "ADS")
# print(resultado)


# def converter_mes_para_extenso(data):
#     mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()

#     d,m,a = data.split('/')
#     mes_extenso = mes[int(m)-1]
#     return f'{d} de {mes_extenso} de {a}'
# print (converter_mes_para_extenso('10/05/2021'))


# TIPOS DE PARAMETROS
# parâmetro posicional, obrigatório, sem valor default (padrão).
# def somar(a, b):
#     return a + b
# r = somar(2, 2)
# print(r)

# parâmetro posicional, obrigatório, com valor default (padrão).
# def calcular_desconto(valor, desconto = 0):
#     valor_com_desconto = valor - (valor * desconto)
#     return valor_com_desconto
# valor1 = calcular_desconto(100) # não aplica desconto
# valor2 = calcular_desconto(100, 0.25) # aplica desconto
# print(f'Valor a ser pago = {valor1}')
# print(f'Valor a ser pago = {valor2}')

# parâmetro nominal, obrigatório, sem valor default (padrão).
# def converter_maiuscula(texto, flag_maiuscula):
#     if flag_maiuscula:
#         return texto.upper()
#     else:
#         return texto.lower()
# texto = converter_maiuscula(flag_maiuscula=True, texto="joão") # Passagem nominal de parâmetros
# print(texto)

# parâmetro nominal, obrigatório, com valor default (padrão).
# def converter_minuscula(texto, flag_minuscula=True):
#     if flag_minuscula:
#         return texto.lower()
#     else:
#         return texto.upper()
# texto1 = converter_minuscula(flag_minuscula=False, texto="linguagem DE PROGRAMAÇÃO")
# texto2 = converter_minuscula(texto="linguagem DE PROGRAMAÇÃO")
# print(texto1)
# print(texto2)

# parâmetro posicional e não obrigatório (args).
# def imprimir_parametros(*args):
#     quantidade_parametros = len(args)
#     print(f'Quantidade de parametros = {quantidade_parametros}')
#     for i, valor in enumerate(args):
#         print(f'Posição = {i}, Valor = {valor}')
# print('Chamada 1')
# imprimir_parametros('São Paulo', 10, 23.78, 'Jõao')
# print('Chamada 2')
# imprimir_parametros('São Paulo', 'Jõao')

# parâmetro nominal e não obrigatório (kwargs).
# def imprimir_parametros(**kwargs):
#     print(f'Tipo do objeto recebido = {type(kwargs)}\n')
#     quantidade_parametros = len(kwargs)
#     print(f'Quantidade de parametros = {quantidade_parametros}')

#     for chave, valor in kwargs.items():
#         print(f'variavel = {chave}, valor = {valor}')
# print('Chamada 1')
# imprimir_parametros(cidade = 'São Paulo', nome = 'Clécio', idade = 22)


# FUNÇÃO ANONIMA
# (lambda x: x + 1)(x=3)
# somar = (lambda x, y: x + y)(x=3, y=5)
# print(somar)


# CALCULO DE COMPRA
def calcular_valor(valor_produto, quantidade, moeda='real', desconto=None, acrescimo=None):
    valor_bruto = valor_produto * quantidade

    if desconto:
        valor_liquido = valor_bruto - (valor_bruto * (desconto / 100))
    elif acrescimo:
        valor_liquido = valor_bruto + (valor_bruto * (acrescimo / 100))
    else:
        valor_liquido = valor_bruto

    if moeda == 'real':
        return valor_liquido
    elif moeda == 'dolar':
        return valor_liquido * 5
    elif moeda == 'euro':
        return valor_liquido * 5.7
    else:
        print('Moeda não cadastrada!')
        return 0
    
valor_a_pagar = calcular_valor(valor_produto=20, quantidade=3)
print(valor_a_pagar)