# a = 10
# b = 5
# if a < b:
#     print ('a é menor que b')
#     r = a + b
#     print(r)
# else:
#     print('a é maior que b')
#     r = a - b
#     print(r)


# codigo_compra = 5333
# if codigo_compra == 5222:
#     print('Compra a vista')
# elif codigo_compra == 5333:
#     print('Compra no boleto')
# elif codigo_compra == 5444:
#     print('Compra no cartao')
# else:
#     print('Codigo nao cadastrado')


# faltas = int(input('Digite a quantidade de faltas: '))
# media = float(input('Digite a media final: '))

# if faltas <= 5 and media >= 7:
#     print('Aluno aprovado')
# else:
#     print('Aluno reprovado')


# a = 15
# b = 9
# c = 
# print(b == c or a < b and a < c)
# print((b == c or a < b) and a < c)


# x = 0
# while x <= 3:
#     print(x)
#     x += 1


# nome = 'Guido'
# for i, c in enumerate(nome):
#     print(f'Posição = {i}, valor = {c}')


# for x in range(0, 10, 2):
#     print(x)


# USANDO O BREAK
# disciplina = 'Linguagem Python'
# for c in disciplina:
#     if c == 'a':
#         continue
#     else:
#         print(c)


# CAÇA AS VOGAIS A
# texto = "A inserção de comentários no código do programa é uma prática normal. Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas. O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado"
# for i, c in enumerate(texto):
#     if c == 'a' or c == 'e':
#         print(f'Vogal "{c}" encontrada, na posição "{i}"')
#     else:
#         continue

imposto1 = 142.80
imposto2 = 354.80
imposto3 = 636.13
imposto4 = 869.36

salario = 0
salario = float(input('Digite o salário do colaborador: '))
if salario <= 1903.98:
    print('O colaborador será isento de imposto')
    print(f'Salario a receber: {salario}')
elif salario <= 2826.65:
    print('O colaborador deve pagar R$142,80 de imposto')
    print(f'Salario a receber: {salario - imposto1}')
elif salario <= 3751.05:
    print('O colaborador deve pagar R$354,80 de imposto')
    print(f'Salario a receber: {salario - imposto2}')
elif salario <= 4664.68:
    print('O colaborador deve pagar R$636,13 de imposto')
    print(f'Salario a receber: {salario - imposto3}')
else:
    print('O colaborador deve pagar R$869,36 de imposto')
    print(f'Salario a receber: {salario - imposto4}')