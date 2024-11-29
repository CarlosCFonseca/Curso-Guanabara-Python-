# quem é maior?
# maior tem que ser menor que a soma dos outros 2
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
if (a + b + c - maior) > maior:
    print('As medidas: {}, {}, e {} formam um triângulo.'. format(a, b, c))
else:
    print('As medidas: {}, {}, e {} não formam um triângulo.'. format(a, b, c))