class Conta:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Você depositou R${valor}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f'Você sacou R${valor}'
        else:
            return 'Saldo insuficiente.'
        
    def getSaldo(self):
        return f'Você tem R${self.saldo} em sua conta.'
    
    def getCliente(self):
        return f'Olá {self.nome}, seja bem vindo.'
    
    def Transferencia(self, conta, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            conta.saldo += valor
            print(f'Transferencia de R${valor} para {conta.nome} realizada com sucesso.')
        else:
            print('Saldo insuficiente para transferencia.')