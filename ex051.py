n = int(input('Primeiro número: '))
r = int(input('Razão: '))
decimo = n + (10 - 1) * r
for c in range(n, decimo + r, r):
    print(c, end=" - ")
print('Acabou')

