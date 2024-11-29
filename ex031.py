# custo até 200 km -,50/km e acima disso 0,45/km
distancia = float(input('Qual é a distância do seu destino?'))
if distancia>200:
    print('O valor da sua passagem é R${:.2f}.'.format(distancia*.45))
else:
    print('O valor da sua passagem é R${:.2f}.'.format(distancia*.5))