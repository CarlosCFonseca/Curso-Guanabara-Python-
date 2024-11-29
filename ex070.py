""" nome, preço e se quer continuar 

Mostrar total da compra, quantos produtos acima de 1000 e nome e preço do produto mais barato"""
total = p1000 = npb = pb = cont = 0
while True:
  produto = str(input('Produto: '))
  custo = float(input('Custo: R$'))
  total += custo
  cont += 1
  if custo>1000:
    p1000 += 1
  if cont == 1:
    pb = custo
    npb = produto
  else:
    if custo < pb:
      pb = custo
      npb = produto
  quest = ' '
  while quest not in 'SN':
    quest = str(input('Quer comprar mais? [ S ]/[ N ]: ')).strip().upper()[0]
  if quest in 'Nn':
    break
print(f'Total compra {total:.2f}, produtos acima de R$ 1.000,00: {p1000}')
print(f'Produto mais barato: {npb} com o custo de R$ {pb:.2f}')