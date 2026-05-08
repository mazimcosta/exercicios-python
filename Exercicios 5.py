# =============================================================================
# EXERCÍCIO 05 | Loop for com listas
# Nível: Médio | Contexto: Processamento de notas fiscais
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema fiscal que processa uma lista de itens de nota
e calcula os impostos de cada um.

TAREFA:
Crie a função processar_nota_fiscal(itens: list) -> dict que:
- Itere sobre os itens com for
- Calcule o valor total de cada item (qtd * preco)
- Aplique o imposto de acordo com a categoria:
    "Eletrônicos" → 15%
    "Alimentos"   → 7%
    "Vestuário"   → 12%
    Outros        → 10%
- Retorne resumo com total bruto, total impostos e total líquido

ENTRADA:
itens = [
    {"produto": "Notebook", "categoria": "Eletrônicos",
     "qtd": 2, "preco": 3500.00},
    {"produto": "Arroz",    "categoria": "Alimentos",
     "qtd": 10, "preco": 25.90},
    {"produto": "Camiseta", "categoria": "Vestuário",
     "qtd": 3, "preco": 89.90},
]

RESTRIÇÕES:
- for obrigatório
- Calcular imposto dentro do loop
- Arredondar para 2 casas decimais
"""
# SUA SOLUÇÃO:
itens = [
    {"produto": "Notebook", "categoria": "Eletrônicos",
     "qtd": 2, "preco": 3500.00},
    {"produto": "Arroz",    "categoria": "Alimentos",
     "qtd": 10, "preco": 25.90},
    {"produto": "Camiseta", "categoria": "Vestuário",
     "qtd": 3, "preco": 89.90},
]

def processar_nota_fiscal(itens:list):
    resultado=[]
    
    for item in itens:
        try:
            item['qtd']=float(item['qtd'])
            item['preco']=float(item['preco'])
        except ValueError:
            return f' Erro: Valor invalido'

        total_bruto=round(item['qtd']*item['preco'],2)    
        
        if item['categoria'].lower()=='eletronicos':
            total_impostos=round(total_bruto * 0.15,2)

        elif item['categoria'].lower()=='alimentos':
            total_impostos=round(total_bruto *0.07,2)

        elif item['categoria'].lower()=='vestuario':
            total_impostos=round(total_bruto *0.12,2)

        else:
            total_impostos=round(total_bruto * 0.10,2)

        total_liquido=total_bruto - total_impostos

        resultado.append({'categoria':item['categoria'], 
                          'total bruto':total_bruto,
                          'total impostos':total_impostos,
                          'total liquido':total_liquido})


resultado=processar_nota_fiscal(itens)

    