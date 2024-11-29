from datetime import date
ano = int(input('Em que ano você nasceu: '))
atual = date.today().year
if (atual - ano) < 18:
    print('Ainda faltam {} anos para vc se alistar.'.format(ano + 18 - atual))
elif (atual-ano) == 18:
    print('Você deve se alistar esse ano')
elif (atual-ano) > 18:
    print('Você deveria ter se alistado {} anos atrás.'.format(atual - (ano + 18)))




