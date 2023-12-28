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

#* HERANÇA E SOBRESCRITA
# class int42(int):
#     def __init__(self, n):
#         int.__init__(n)
#     def __add__(a,b):
#         return 42
#     def __str__(n):
#         return '42'

# a = int42(7)
# b = int42(13)
# print(a + b)
# print(a)
# print(b)

# c = int(7)
# d = int(13)
# print(c + d)
# print(c)
# print(d)

#* HERANÇA MULTIPLA
# class Ethernet():
#     def __init__(self, name, mac_adress):
#         self.name = name
#         self.mac_adress = mac_adress

# class PCI():
#     def __init__(self, bus, vendor):
#         self.bus = bus
#         self.vendor = vendor

# class USB():
#     def __init__(self, device):
#         self.device = device

# class Wireless(Ethernet):
#     def __init__(self, name, mac_adress):
#         Ethernet.__init__(self, name, mac_adress)

# class PCIEthernet(PCI, Ethernet):
#     def __init__(self, bus, vendor, name, mac_adress):
#         PCI.__init__(self, bus, vendor)
#         Ethernet.__init__(self, name, mac_adress)

# class USBWireless(USB, Wireless):
#     def __init__(self, device, name, mac_adress):
#         USB.__init__(self, device)
#         Wireless.__init__(self, name, mac_adress)

# eth0 = PCIEthernet('pci :0:0:1', 'realtek', 'eth0', '00:11:22:33:44')
# wlan0 = USBWireless('usb0', 'wlan0', '00:33:44:55:66')
# print('PCIEthernet é uma PCI?', isinstance(eth0, PCI))
# print('PCIEthernet é uma Ethernet?', isinstance(eth0, Ethernet))
# print('PCIEthernet é uma USB?', isinstance(eth0, USB))
# print('\nUSBWireless é uma USB?', isinstance(wlan0, USB))
# print('USBWireless é uma Wireless?', isinstance(wlan0, Wireless))
# print('USBWireless é uma Ethernet?', isinstance(wlan0, Ethernet))
# print('USBWireless é uma PCI?', isinstance(wlan0, PCI))

# class ContaCorrente:
#     def __init__(self, nome):
#         self.nome = nome 
#         self.email = None
#         self.telefone = None
#         self._saldo = 0
#     def _checar_saldo(self, valor):
#         return self._saldo >= valor
#     def depositar(self, valor):
#         self._saldo += valor
#     def sacar(self, valor):
#         if self._checar_saldo(valor):
#             self._saldo -= valor
#             return True
#         else:
#             return False
#     def obter_saldo(self):
#         return self._saldo
    
# class ContaPF(ContaCorrente):
#     def __init__(self, nome, cpf):
#         super().__init__(nome)
#         self.cpf = cpf
#     def solicitar_emprestimo(self, valor):
#         return self.obter_saldo() >= 500
    
# class ContaPJ(ContaCorrente):
#     def __init__(self, nome, cnpj):
#         super().__init__(nome)
#         self.cnpj = cnpj
#     def sacar_emprestimo(self, valor):
#         return valor <= 5000
    
# conta_pf1 = ContaPF('João', '111.111.111-11')
# conta_pf1.depositar(1000)
# print('Saldo atual é', conta_pf1.obter_saldo())
# print('Receberá empréstimo = ', conta_pf1.solicitar_emprestimo(2000))
# conta_pf1.sacar(800)
# print('Saldo atual é', conta_pf1.obter_saldo())
# print('Receberá empréstimo = ', conta_pf1.solicitar_emprestimo(2000))

# conta_pj1 = ContaPJ('Empresa A', '11.111.111/1111-11')
# print('Saldo atual é', conta_pj1.obter_saldo())
# print('Receberá empréstimo = ', conta_pj1.sacar_emprestimo(3000))

#! DESAFIO
# class Cliente:
#     def __init__(self):
#         self.nome = None
#         self.email = None
#         self.telefone = None
#         self._cupom_desconto = 0
    
#     def get_cupom_desconto(self):
#         return self._cupom_desconto
    
# class ClienteVipPF(Cliente):
#     def __init__(self):
#         super().__init__()
#         self._cupom_desconto = 0.2

#     def realizar_compras(self, lista_itens):
#         print(f'Quantidade total de itens comprados = {len(lista_itens)}')

# class ClientePF(Cliente):
#     def __init__(self):
#         super().__init__()
#         self._cupom_desconto = 0.05
    
#     def realizar_compras(self, lista_itens):
#         if len(lista_itens) <= 20:
#             return f'Quantidade total de itens comprados = {len(lista_itens)}'
#         else:
#             return 'Quantidade de itens superior ao limite permitido'

# class ClientePJ(Cliente):
#     def __init__(self):
#         super().__init__()
#         self._cupom_desconto = 0.1

#     def realizar_compras(self, lista_itens):
#         if len(lista_itens) <= 50:
#             return f'Quantidade total de itens comprados = {len(lista_itens)}'
#         else:
#             return 'Quantidade de itens superior ao limite permitido'
        
# cli1 = ClienteVipPF()
# cli1.nome = 'Maria'
# print(cli1.get_cupom_desconto())
# cli1.realizar_compras(['item1', 'item2', 'item3', 'item4']) 