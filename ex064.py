n = int(input('Digite um número: '))
soma = 0
cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print('Você digitou {} números e a soma deles foi {}.'.format(cont, soma))
