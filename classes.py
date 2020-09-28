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

class Historico(Document):

    contaEnviou = ReferenceField(Conta)
    contaRecebeu = ReferenceField(Conta)
    valorTransferido = FloatField(required=True)

    def setContaEnviou(self, conta):
        self.contaEnviou = conta
        self.save()
        
    def getContaEnviou(self):
        return self.contaEnviou

    def setcontaRecebeu(self, conta):
        self.contaRecebeu = conta
        self.save()

    def getContaRecebeu(self):
        return self.contaRecebeu

    def setValorTransferido(self, valor):
        self.valorTransferido = valor
        self.save()

    def getValorTransferido(self):
        return self.valorTransferido


