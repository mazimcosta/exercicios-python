#Construindo o sistema:
from produto import  *
from servicos import *
while True:
    print('MENU','[1].Listar Produtos','[2].Vender Produto','[3].Aplicar desconto','[4]Sair',sep='\n')

    entrada=int(input('Escolha uma opção:'))
    if entrada==1:
        listar_produtos(produtos)
    
    elif entrada==2:
        codigo=input('Digite o codigo do produto:')
        quantidade=int(input('Digite  a quantidade:'))
        vender_produto(produtos,codigo,quantidade)

    elif entrada==3:
        codigo=input('Digite o codigo do produto:')
        for produto in produtos:
            if produto.codigo==codigo:
                produto.aplicar_desconto()
            else:
                print('Erro: produto não encontrado')

    elif entrada==4:
        break        

    