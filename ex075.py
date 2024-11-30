num = [int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite ultimo numero: '))]
print(f'Você digitou os números: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado')
print('OS valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')