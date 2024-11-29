n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
if m >= 7:
    print('Sua média foi {} e vc está {}.'.format(m, 'aprovado'))
elif m < 5:
    print('Sua média foi {} e vc está {}.'.format(m, 'reprovado'))
else:
    print('Sua média foi {} e vc está {}.'.format(m, 'de recuperação'))

