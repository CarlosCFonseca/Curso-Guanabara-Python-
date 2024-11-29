# verificar se o ano é bissexto (tem que ser divisivel por 4 exceto multiplos de 100 que não são multiplos de 400)
ano = int(input('Ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Bissexto')
else:
    print('Não é bissexto')