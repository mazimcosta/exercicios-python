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
    impostos_total=0
    bruto_total=0
    for item in itens:
        
        try:
            item['qtd']=float(item['qtd'])
            item['preco']=float(item['preco'])
        except ValueError:
            return f' Erro: Valor invalido'

        total_bruto=round(item['qtd']*item['preco'],2)   
        bruto_total+=total_bruto 
        
        if item['categoria'].lower()=='eletrônicos':
            total_impostos=round(total_bruto * 0.15,2)
            impostos_total+=total_impostos
       
        elif item['categoria'].lower()=='alimentos':
            total_impostos=round(total_bruto *0.07,2)
            impostos_total+=total_impostos
        
        elif item['categoria'].lower()=='vestuário':
            total_impostos=round(total_bruto *0.12,2)
            impostos_total+=total_impostos
       
        else:
            total_impostos=round(total_bruto * 0.10,2)
            impostos_total+=total_impostos

        total_liquido=bruto_total - impostos_total

        resultado.append({
            'total bruto':bruto_total,
                          'total impostos':impostos_total,
                          'total liquido':total_liquido})
        return resultado


resultado=processar_nota_fiscal(itens)

#Exercicio resolvido!!