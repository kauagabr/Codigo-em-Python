listagem = ('Lápis.........................R$   1.75',
            'Borracha......................R$   2.00',
            'Caderno.......................R$  15.90',
            'Estojo........................R$  25.00',
            'Transferidor..................R$   4.20',
            'Compasso......................R$   9.99',
            'Mochila.......................R$ 120.32',
            'Canetas.......................R$  22.30',
            'Livro.........................R$  34.90',)
print('_'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_'*40)
for item in listagem:
    print(item)
print('_'*40)
