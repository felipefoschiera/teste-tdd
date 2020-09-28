from classes import *
from mongoengine import *

def insereConta(enderecoEmail):
    return Conta(email=enderecoEmail, saldo=0.0).save()

def getConta(enderecoEmail):
    contas = list(Conta.objects(email=enderecoEmail))
    if len(contas) == 0:
        return False
    return contas[0]

def insereHistorico(conta1, conta2, valor):
    return Historico(contaEnviou=conta1, contaRecebeu=conta2, valorTransferido=valor).save()

def existeHistorico(id):
    objs = list(Historico.objects(id=id))
    if len(objs) == 0:
        return False
    return True

def findValorHistorico(id):
    objs = list(Historico.objects(id=id))
    if len(objs) == 0:
        return False
    return objs[0].valorTransferido