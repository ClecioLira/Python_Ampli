import modulo_0

conta1 = modulo_0.Conta('Felipe', 1)
print(conta1.getCliente())
print(conta1.getSaldo())
conta1.depositar(300)
print(conta1.getSaldo())

conta2 = modulo_0.Conta('Maria', 2)

conta1.Transferencia(conta2, 100)
print(conta1.getSaldo())
print(conta2.getCliente())
print(conta2.getSaldo())
