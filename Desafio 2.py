# EXERCICIO 14 | Sistema de Pedidos
# Nivel: Medio-Dificil | Contexto: E-commerce

"""
CLASSES:
- Produto
- Cliente
- Pedido

Produto:
- nome
- preco
- estoque
- baixar_estoque()
- devolver_estoque()

Cliente:
- nome
- email

Pedido:
- cliente
- produtos
- status: "criado", "pago", "enviado", "cancelado"

REGRAS:

1. adicionar_produto(produto)
- So permite se status == "criado"
- So adiciona se houver estoque
- Deve diminuir o estoque do produto
- Estoque nunca pode ficar negativo

2. remover_produto(nome_produto)
- So permite se status == "criado"
- Remove 1 produto pelo nome
- Deve devolver o produto ao estoque
- Se produto nao estiver no pedido, raise ValueError

3. calcular_total()
- Soma todos os precos dos produtos

4. finalizar_pedido()
- So pode finalizar se tiver pelo menos 1 produto
- So pode finalizar se status == "criado"
- Muda status para "pago"

5. enviar_pedido()
- So pode enviar se status == "pago"
- Muda status para "enviado"

6. cancelar_pedido()
- Pode cancelar se status for "criado" ou "pago"
- Nao pode cancelar se ja estiver "enviado"
- Deve devolver todos os produtos ao estoque
- Muda status para "cancelado"

7. __str__()
- Retorna:
  Cliente | Quantidade de itens | Total | Status

RESTRICOES:
- Validar todas as operacoes com raise ValueError
- Nao permitir estoque negativo
- Nao permitir alterar pedido pago, enviado ou cancelado
- Nao acessar atributos privados de Produto diretamente
- Usar metodos do Produto para alterar estoque

DESAFIO EXTRA:
- Criar historico de status
- Usar datetime
"""

