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
        self._ContaBancaria__saldo=saldo
        self._historico=dict(historico)

    @property
    def saldo(self):
        return self._ContaBancaria__saldo
    
    def depositar(self,valor):
        if valor<0:
            return f'Deposito invalido'
        elif valor==0:
            return f'Deposito invalido'
        else:
            self._ContaBancaria__saldo+=valor
            hora=datetime.now() # Obtendo hora e ata com datetime
            self._historico=registrar_historico(hora=hora,deposito=valor,saldo=self._ContaBancaria__saldo)# Usando função que esta em servicos.py
            return f'deposito efetuado com sucesso'
        

    def sacar(self,valor):
        if valor> self._ContaBancaria__saldo:
            return f'Saldo insuficiente'

        elif valor<0:
            return f' Valor invalido'

        self._ContaBancaria__saldo-=valor
        hora=datetime.now()
        self._historico=registrar_historico(hora=hora,saque=valor,saldo=self._ContaBancaria__saldo)
        return  f'Saque efetuado com sucesso'
    
    def transferir(self,valor,conta_origem,conta_destino):
        if valor>conta_origem._ContaBancaria__saldo:
            return f' Saldo insuficiente'
        elif valor==0:
            return f' Valor invalido'
        elif valor<0:
            return f' Valor invalido'
        
        conta_origem._ContaBancaria__saldo-=valor
        hora=datetime.now()
        conta_origem._historico=registrar_historico(hora=hora,transferencia=valor,saldo=conta_origem._ContaBancaria__saldo)
        conta_destino._ContaBancaria__saldo+=valor
        hora=datetime.now()
        conta_destino._historico=registrar_historico(hora=hora,transferencia=valor,saldo=conta_destino._ContaBancaria__saldo)
        return f' Transferencia efetuada com sucesso'
    
    def extrato(self):
        return self._historico
    
    def __str__(self):
        return f' titular:{self.titular} agencia:{self.agencia} saldo:{self.saldo} historico:{self._historico}'