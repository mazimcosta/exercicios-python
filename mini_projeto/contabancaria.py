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

class ContaBancaria:

    def __init__(self,titular,agencia,saldo):
        
        if saldo<0:
            raise ValueError('Saldo inicial não pode ser negativo')
        
        self.titular=titular
        self.agencia=agencia
        self.__saldo=saldo
        self.__historico=[]

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    
    def saldo(self,valor):
        self.__saldo=valor
    

def __registrar_historico(self,tipo,valor):
    self.__historico.append({
        'data':datetime.now(),
        'tipo':tipo,
        'valor':valor,
        'saldo':self.__saldo

    })



    def depositar(self,valor):
        if valor<=0:
            raise ValueError('Valor invalido')
        self.__saldo+=valor
        self.__registrar_historico('deposito',valor)
        return f' Deposito realizado com sucesso'

    def sacar(self,valor):
        if valor>self.__saldo:
            raise ValueError('Saldo insuficiente')
        if valor<=0:
            raise ValueError('Valor invalido')
        self.__saldo-=valor
        self.__registrar_historico('saque',valor)
        return 'Saque efetuado com sucesso'        