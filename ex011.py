l = float(input('Qual a largura da parede? '))
h = float(input('qual a altura da parede? '))
area = l * h
tinta = area / 2
print('Você tem uma parede com {} x {}, a área da parede é {:.2f}m2.\nSera necessário {:.2f}litros de tinta para pinter sua parede.'.format(l, h, area, tinta))