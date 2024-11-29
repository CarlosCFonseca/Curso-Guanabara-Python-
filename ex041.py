from datetime import date
atual = date.today().year
n = int(input('Ano de nascimento? '))
idade = atual - n
print('Idade: {}.'.format(idade))
if idade < 9:
    print('Categoria mirim')
elif idade > 8 and idade < 14:
    print('Categoria infantil')
elif 14 <= idade < 19:
    print('Categoria junior')
elif 19 <= idade < 25:
    print('Categoria senior')
elif 25 <= idade:
    print('Categoria Master')


