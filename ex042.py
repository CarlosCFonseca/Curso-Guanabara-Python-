a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
if (a + b + c - maior) > maior:
    print('As medidas formam um triângulo ',end='')
    if a == b == c:
        print('equilatero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('As medidas: {}, {}, e {} não formam um triângulo.'. format(a, b, c))
