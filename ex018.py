import math
a = float(input('Digite o angulo: '))
print('Para o angulo {}, temos Seno: {:.2f}, cosseno: {:.2f} e tangente: {:.2f}.'.format(a, math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))
