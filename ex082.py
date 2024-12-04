lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    perg = str(input('Quer continuar? ')).strip().upper()[0]
    if perg == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Lista total: {lista}')
print(f'Pares: {par}')
print(f'Impares: {impar}')
