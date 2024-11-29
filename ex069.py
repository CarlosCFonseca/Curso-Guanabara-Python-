""" sexo e idade
Quantos + 18
Quantos homens
Mulheres <20"""
mais18 = homens = mulher20 = 0
while True:
   idade = int(input('idade: '))
   if idade > 18:
      mais18 += 1
   sexo = ' '
   while sexo not in 'MF':
      sexo = str(input('Sexo [ M / F ]: ')).strip().upper()[0]
   if sexo in 'Ff' and idade < 20:
      mulher20 += 1
   if sexo in 'Mm':
      homens += 1
   perg = ''
   while perg not in 'SN':
      perg = str(input('Quer continuar? [ S / N ]: ')).strip().upper()[0]
   if perg in 'Nn':
      break
print(f'Maiores de 18: {mais18}, homens: {homens} e mulheres menores de 20 anos: {mulher20}')