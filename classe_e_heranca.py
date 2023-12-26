# class PrimeiraClasse:
#     def imprimir_mensagem(self, nome):
#         print(f'Olá {nome}, seja bem vindo!')

# obj1 = PrimeiraClasse()
# obj1.imprimir_mensagem('João')

# class Calculadora:
#     def somar(self, n1, n2):
#         return n1 + n2
#     def subtrair(self, n1, n2):
#         return n1 - n2
#     def multiplicar(self, n1, n2):
#         return n1 * n2
#     def dividir(self, n1, n2):
#         return n1 / n2
#     def dividir_resto(self, n1, n2):
#         return n1 % n2
    
# calc = Calculadora()
# print('Soma:', calc.somar(4, 3))
# print('Subtração:', calc.subtrair(13, 7))
# print('Multiplicação:', calc.multiplicar(5, 5))
# print('Divisão:', calc.dividir(15, 3))
# print('Resto da divisão:', calc.dividir_resto(7, 3))

#! CONSTRUTOR DA CLASSE __INIT__()
# class Televisao:
#     def __init__(self):
#         self.volume = 10
#     def aumentar_volume(self):
#         self.volume += 1
#     def diminuir_volume(self):
#         self.volume -= 1

# tv = Televisao()
# print('Volume ao ligar a tv:', tv.volume)
# tv.aumentar_volume()
# print('Volume atual da tv:', tv.volume)

#* Variáveis e métodos privados - Em linguagens de programação OO, como Java e C#, as classes, os atributos e os métodos são acompanhados de modificadores de acesso, que podem ser: public, private e protected. Em Python, não existem modificadores de acesso e todos os recursos são públicos. Para simbolizar que um atributo ou método é privado, por convenção, usa-se um sublinhado "_"  antes do nome; por exemplo, _cpf, _calcular_desconto() (PSF, 2020a). 

#! HERANÇA
# class Pessoa:
#     def __init__(self):
#         self.cpf = None
#         self.nome = None
#         self.endereco = None

# class Funcionario(Pessoa):
#     def __init__(self):
#         self.matricula = None
#         self.salario = None
#     def bater_ponto(self):
#         self.bater_ponto = True
#     def fazer_login(self):
#         self.fazer_login = True

# class Cliente(Pessoa):
#     def __init__(self):
#         self.codigo = None
#         self.dataCadastro = None
#     def fazer_compra(self):
#         self.fazer_compra = True
#     def pagar_compra(self):
#         self.pagar_compra = True

# f1 = Funcionario()
# f1.nome = 'Funcionario A'
# f1.cpf = '123.456.789.11'
# print(f1.nome)
# print(f1.cpf)
# c1 = Cliente()
# c1.cpf = '111.111.111-11'
# print(c1.cpf)

class int42(int):
    def __init__(self, n):
        int.__init__(n)
    def __add__(a,b):
        return 42
    def __str__(n):
        return '42'

a = int42(7)
b = int42(13)
print(a + b)
print(a)
print(b)

c = int(7)
d = int(13)
print(c + d)
print(c)
print(d)