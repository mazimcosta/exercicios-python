#Cadastrando produtos:
from produto import Produto

p1,p2,p3=Produto('124','arroz',5.49,70),Produto('451','macarrao',2.19,100),Produto('147','iogurte',5.79,200)

produtos=[p1,p2,p3]


# Funcionalidades:
def listar_produtos(produtos):
    return [produto.nome for produto in produtos if produto.estoque>0]

def valor_total_estoque(produtos):
    valor=0
    for produto in produtos:
        valor+=round(produto._preco * produto.estoque)
    return valor

def desconto_geral(produtos,percentual):
            desconto=produto._preco * percentual/100
            for produto in produtos:
                  produto._preco=round(produto._preco - desconto,2)

def buscar_produto(produtos,nome):
      for produto in produtos:
            if produto.nome==nome:
                  return produto.__dict__

