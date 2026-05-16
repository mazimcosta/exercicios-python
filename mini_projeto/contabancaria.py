# =============================================================================
# EXERCÍCIO 13 | Encapsulamento
# Nível: Médio-Difícil | Contexto: Conta bancária
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema bancário com regras rígidas de acesso aos dados.

TAREFA:
Crie a classe ContaBancaria com encapsulamento real:
- __saldo privado (name mangling)
- __historico privado
- titular e agencia públicos
- @property saldo → só leitura
- depositar(valor) → valida valor positivo
- sacar(valor) → valida saldo suficiente
- transferir(valor, conta_destino: ContaBancaria)
- extrato() → imprime histórico formatado
- __str__() → resumo da conta

FORMATO DO HISTÓRICO:
[2024-03-01 08:22] DEPÓSITO    +R$1.500,00 | Saldo: R$1.500,00
[2024-03-01 08:23] SAQUE       -R$  200,00 | Saldo: R$1.300,00

RESTRIÇÕES:
- __saldo nunca acessível diretamente de fora
- datetime para timestamp
- raise ValueError com mensagem clara em operações inválidas
"""
# SUA SOLUÇÃO:
from datetime import datetime
from servicos import registrar_historico
class ContaBancaria:

    def __init__(self,titular,agencia,saldo,historico):
        self.titular=titular
        self.agencia=agencia
        self.__saldo=saldo
        self._historico=dict(historico)

    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self,valor):
        if valor<=0:
            raise ValueError('Valor invalido')
        self.__saldo+=valor
        return f'deposito efetuado com sucesso.'

    def sacar(self,valor):
        if valor>self.__saldo:
            raise ValueError('Saldo insuficiente')
        elif valor<=0:
            raise ValueError('Valor invalido')
        self.__saldo-=valor
        return f'Saque efetuado com sucesso.'
    
    def registrar_historico(self,saldo,deposito=None,saque=None,transferencia=None):
        hora=datetime.now()
        if deposito:
            return self.historico.update({hora:{'deposito':deposito,'saldo':saldo}})
        if saque:
            return self.historico.update({hora:{'saque':saque,'saldo':saldo}})
        if transferencia:
            return self.historico.update({hora:{'transferencia':transferencia,'saldo':saldo}})
    
    def transferir(self,valor,conta_destino):
        if valor>self.__saldo:
            raise ValueError('Saldo insuficiente')
        if valor<=0:
            raise ValueError('Valor invalido')
        self.sacar(valor)
        self.registrar_historico(transferencia=valor,saldo=self.__saldo)
        conta_destino.depositar(valor)
        conta_destino.registrar_historico(transferencia=valor,saldo=conta_destino.__saldo)
        return f'Transferencia efetuada com sucesso'
    
    def extrato(self):
        for data,dados in self._historico:
            print(f'data:{data} transação:{dados}')

    def __str__(self):
        return f'Conta(titular:{self.titular} agencia:{self.agencia} saldo{self.saldo})'
    
    