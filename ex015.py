d = int(input('Dias alugados: '))
k = float(input('Kilometragem rodada: '))
p = (d * 60) + (k * 0.15)
print('O valor total da locação é R${:.2f}'.format(p))
