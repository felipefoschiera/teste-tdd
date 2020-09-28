from classes import *
from mongoengine import *

def insereConta(enderecoEmail):
    return Conta(email=enderecoEmail, saldo=0.0).save()

def getConta(enderecoEmail):
    contas = list(Conta.objects(email=enderecoEmail))
    if len(contas) == 0:
        return False
    return contas[0]
