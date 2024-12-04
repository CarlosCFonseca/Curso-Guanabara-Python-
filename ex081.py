lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    quest = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if quest == 'N':
        break
if 5 in lista:
    perg = 'sim'
else:
    perg = 'não'
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números, a lista decresente é {lista} e o valor "5" está na lista? {perg}')
