# =============================================================================
# EXERCÍCIO 14 | Sistema de Pedidos
# Nível: Médio-Difícil | Contexto: E-commerce
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================

"""
CONTEXTO:
Você precisa modelar um sistema de pedidos de uma loja online.

TAREFA:
Crie as classes e regras para um sistema de pedidos com:

CLASSES:
- Produto
- Cliente
- Pedido

FUNCIONALIDADES:

Produto:
- nome
- preco
- estoque

Cliente:
- nome
- email

Pedido:
- cliente
- lista de produtos
- status (ex: "criado", "pago", "enviado")

REGRAS:

1. adicionar_produto(produto)
- Só adiciona se houver estoque
- Deve diminuir o estoque do produto

2. remover_produto(nome_produto)
- Remove do pedido

3. calcular_total()
- Soma todos os preços dos produtos

4. finalizar_pedido()
- Só pode finalizar se tiver pelo menos 1 produto
- Muda status para "pago"

5. enviar_pedido()
- Só pode enviar se estiver "pago"
- Muda status para "enviado"

6. cancelar_pedido()
- Pode cancelar a qualquer momento
- Deve devolver os produtos ao estoque
- Status: "cancelado"

7. __str__()
- Retorna resumo do pedido:
  Cliente | Quantidade de itens | Total | Status

RESTRIÇÕES:

- Validar todas as operações (raise ValueError)
- Não permitir ações inválidas:
  - enviar sem pagar
  - finalizar sem itens
- Estoque nunca pode ficar negativo

DESAFIO EXTRA (OPCIONAL):

- Criar histórico de status (tipo log)
- Usar datetime
"""
