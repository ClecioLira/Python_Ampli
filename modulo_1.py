import modulo_0

conta1 = modulo_0.Conta('Felipe', 1)
conta2 = modulo_0.Conta('Maria', 2)

print(conta1.getCliente())
print(conta1.getSaldo())
conta1.depositar(300)
print(conta1.getSaldo())
conta1.Transferencia(conta2, 50)
print(conta1.getSaldo(), "\n")

print(conta2.getCliente())
print(conta2.getSaldo())
