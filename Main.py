class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1= Cliente("Murilo ", "114444-2222")
Conta=Conta(c1.get_nome(), 1222)


conta.deposita(100)
conta.saque(50)
conta.extrato()