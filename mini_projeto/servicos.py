#Cadastrando produtos:
from datetime import datetime
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
            for produto in produtos:
                  produto.aplicar_desconto(percentual)
            return produtos

def buscar_produto(produtos,nome):
      for produto in produtos:
            if produto.nome==nome:
                  return produto.__dict__

def vender_produto(produtos,codigo,quantidade):
      for produto in produtos:
           if produto.codigo==codigo and quantidade<0:
                 raise ValueError('Erro: quantidade não pode ser negativa.')
           elif produto.codigo==codigo and quantidade>produto.estoque:
                 raise ValueError('Erro: Estoque insuficiente')
           else:
                 raise ValueError('Erro: codigo inexistente')
           


def registrar_historico(historico:dict,data,deposito=None,saque=None,transferencia=None,saldo=None):
      historico={}
      if deposito:
            historico.update({data:{'deposito':deposito,'saldo':saldo}})
            return historico
      if saque:
            historico.update({data:{'saque':saque,'saldo':saldo}})
            return historico
      if transferencia:
            historico.update({data:{'transferencia':transferencia,'saldo':saldo}})
