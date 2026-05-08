'''testando'''

dicionario={'arroz':{'quantidade':10,'preco':5.0},
            'feijao':{'quantidade':15,'preco':478}}

for produto,(quantidade, preco)  in dicionario.items():
    if quantidade==10:
        print(f'{produto=},{quantidade=}')
    