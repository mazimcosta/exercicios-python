
# =============================================================================
# EXERCÍCIO 04 | Loop while com break
# Nível: Médio | Contexto: Sistema de tentativas de pagamento
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema de pagamento que tenta processar a transação
até 3 vezes antes de cancelar.

TAREFA:
Crie a função tentar_pagamento(valor: float,
                                saldo: float) -> dict que:
- Simule 3 tentativas de pagamento
- Em cada tentativa, verifique se saldo >= valor
- Se aprovado: retorna sucesso e tentativa em que aprovou
- Se 3 falhas: retorna cancelado
- A cada tentativa falha, o saldo aumenta 10%
  (simulando recarga automática)
- Use while com break

ENTRADA:
valor = 500.00
saldo = 350.00  (insuficiente na 1ª, mas aumenta 10% a cada falha)

SAÍDA ESPERADA (se aprovar na 2ª tentativa):
{
    "status": "APROVADO",
    "tentativa": 2,
    "saldo_final": 385.00,
    "valor_pago": 500.00
}

RESTRIÇÕES:
- while obrigatório com break para sair ao aprovar
- Não use for
"""
# SUA SOLUÇÃO:


def tentar_pagamento(valor:float,saldo:float):
    tentativas=0
    resultado=dict()
    
    try:
        valor=float(valor)
        saldo=float(saldo)
    except (ValueError,TypeError):
        return {'status':'ERRO','motivo':'Valor invalido'}
    
   

    while tentativas<3:
        if saldo>=valor:
            tentativas+=1
            saldo_final=saldo - valor
            resultado=({'status':'aprovado','tentativas':tentativas,'saldo_final':round(saldo_final,2),'valor_pago':round(valor,2)})
            break


    
        tentativas+=1
        saldo=round(saldo *1.1,2)
        continue
        

        
            
    else:
        resultado=({'status':'reprovado','tentativas':tentativas,'motivo':'saldo insuficiente'})

    return resultado

