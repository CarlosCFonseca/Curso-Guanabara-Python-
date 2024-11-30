listagem = ['Lápis', 1.75, 'Borracha', 2, 'Caneta', 3,'Caderno', 8.56, 'Régua', 28.9, 'Mochila', 167.99]

print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)