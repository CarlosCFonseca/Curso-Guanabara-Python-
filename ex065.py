q = 's'
soma = cont = maior = menor =0
while q in 'Ss':
    n = int(input('Digite um número: '))
    q = str(input('Você quer continuar? (S / N): ')).upper().strip()[0]
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n <menor:
            menor = n
media = soma / cont
print('A média dos {} digitados é {}, e a soma é {}. '.format(cont, media, soma))
print('O maior valor é {} e o menor é {}.'.format(maior, menor))


