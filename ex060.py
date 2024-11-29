'''from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n , f))'''

n = int(input('Digite um número: '))
c = n
f = 1
while c >0:
    print('{}'.format(c), end=' ')
    print('X ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))