from mongoengine import *

class Conta(Document):
    email = StringField(required=True)
    saldo = FloatField()

    def getSaldo(self):
        return self.saldo

    def adicionaSaldo(self, valor):
        self.saldo += valor
        self.save()

    def setSaldo(self, valor):
        self.saldo = valor
        self.save()

    def removeSaldo(self, valor):
        if self.saldo < valor:
            return
        self.saldo -= valor
        self.save()

    def transferir(self, conta, valor):
        if self.saldo < valor:
            return
        self.removeSaldo(valor)
        conta.adicionaSaldo(valor) 
        self.save()
        conta.save()
