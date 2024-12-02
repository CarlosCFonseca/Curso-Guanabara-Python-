maior = menor = 0
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[0]
    else:
        if lista[c] > maior:
            maior = lista [c]
        if lista[c] < menor:
            menor = lista [c]
print(f'Os números digitados foram: {lista}.')
print(f'O menor valor foi {menor} e foi digitado nas posições: ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print(f'\nO maior valor foi {maior} e foi digitado nas posições: ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')