import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print('O valor da hipotenusa do triângulo retângulo com cateto oposto medindo {}, cateto adjascente medindo {} é {}.'.format(co, ca, math.hypot(co, ca)))
      