lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    quest = str(input('Quer continuar? [S/N] '))
    if quest in 'Nn':
        break
print('~' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')  
  