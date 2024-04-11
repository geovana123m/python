class ContaBancaria:

    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Número da Conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")

#aqui estou criando uma instancia do objeto ContaBancaria
#com o nome conta_da_geo
numero_conta = input("Digite o numero da conta")
titular_conta = input("Digite o titular da conta")
saldo_inicial = float(input("Digite o saldo inicial da conta").replace(",","."))

conta_da_geo = ContaBancaria(numero_conta, titular_conta, saldo_inicial)
valor_deposito = float(input("Digite o valor a ser depositado").replace(",","."))
valor_saque = float(input("Digite o valor a ser sacado").replace(",","."))

conta_da_geo.depositar(valor_deposito)
conta_da_geo.sacar(valor_saque)
conta_da_geo.exibir_detalhes()

