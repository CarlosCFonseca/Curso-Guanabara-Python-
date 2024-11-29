soma = 0
ihmv = 0
hmv = 0
cm20 = 0
for c in range(1, 5):
    print('====DADOS DA {}° PESSOA===='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F):')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        ihmv = idade
        hmv = nome
    if sexo in 'Mm' and idade > ihmv:
        ihmv = idade
        hmv = nome
    if sexo in 'Ff' and idade < 20:
        cm20 += 1
media = soma / 4
print('A média de idade do grupo é {:.2f}, o homem mais velho tem {} anos, é o {} e temos {} mulheres com menos de 20 anos.'.format(media, ihmv, hmv, cm20))



