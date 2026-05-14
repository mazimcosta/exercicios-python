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
