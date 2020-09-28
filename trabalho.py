# Execução: python -m unittest trabalho.py
from unittest import TestCase
from mongoengine import *
from classes import *
from funcoes import *

connect('trabalho1')

Conta.objects.delete()

insereConta('joao@gmail.com')
insereConta('artur@gmail.com')

class ContaTest(TestCase):

    # Testa se adiciona o saldo corretamente

    def test_adicionaSaldo(self):
        adicionar = 5

        c = getConta('joao@gmail.com')
        antes = c.getSaldo()
        depois = antes + adicionar

        c.adicionaSaldo(adicionar)

        self.assertEqual(c.getSaldo(), depois) # verifica se o saldo adicionado foi correto

    # Testa se pode remover tendo saldo suficiente
    def test_removeComSaldo(self):

        remover = 5

        c = getConta('joao@gmail.com')
        c.setSaldo(7)

        antes = c.getSaldo()
        depois = antes - remover # depois deve ter 2
        c.removeSaldo(remover)

        self.assertEqual(c.getSaldo(), depois) # verifica se removeu corretamente o saldo

    # Testa se pode remover sem saldo suficiente
    def test_removeSemSaldo(self):

        remover = 5
        
        c = getConta('joao@gmail.com')
        c.setSaldo(2)
        
        antes = c.getSaldo()
        depois = antes  # depois deve continuar em 2
        
        c.removeSaldo(remover)

        self.assertEqual(c.getSaldo(), depois) # verifica se não permitiu remover pois não havia saldo suficiente

    # Testa se há saldo suficiente para transferir (tendo saldo)
    def test_transferenciaComSaldo(self):
        
        quant_transferir = 5
        
        joao = getConta('joao@gmail.com')
        joao.setSaldo(10)

        email_destino = 'artur@gmail.com'

        artur = getConta(email_destino)

        self.assertTrue(artur) # verifica se a conta existe - se não existe é False

        antesJoao = joao.getSaldo()
        antesArtur = artur.getSaldo()
        depoisJoao = antesJoao - quant_transferir
        depoisArtur = antesArtur + quant_transferir

        joao.transferir(artur, quant_transferir) # Transfere 5 para Artur
        
        self.assertEqual(joao.getSaldo(), depoisJoao) # verifica se o saldo ficou correto após a transferência
        self.assertEqual(artur.getSaldo(), depoisArtur) # verifica se o saldo ficou correto após a transferência


    # Testa se há saldo suficiente para transferir (sem saldo)
    def test_TransferenciaSemSaldo(self):

        quant_transferir = 5
        
        joao = getConta('joao@gmail.com')
        joao.setSaldo(3)

        artur = getConta('artur@gmail.com')

        self.assertTrue(artur) # verifica se a conta existe - se não existe é False

        antesJoao = joao.getSaldo()
        antesArtur = artur.getSaldo()
        depoisJoao = antesJoao
        depoisArtur = antesArtur

        joao.transferir(artur, quant_transferir) 
         
        self.assertEqual(joao.getSaldo(), depoisJoao) # verifica se o saldo ficou igual
        self.assertEqual(artur.getSaldo(), depoisArtur) # verifica se o saldo ficou igual

class HistoricoTest(TestCase):

    def test_historicoCriado(self):
        
        quant_transferir = 5
        joao = getConta('joao@gmail.com')
        joao.setSaldo(10)

        email_destino = 'artur@gmail.com'
        artur = getConta(email_destino)
        
        joao.transferir(artur, quant_transferir);

        historico = insereHistorico(joao, artur, quant_transferir)
        
        id_hist = historico.id

        self.assertTrue(existeHistorico(id_hist))
        

if __name__ == '__main__':
    unittest.main()