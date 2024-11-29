valor = float(input('Valor: '))
salario = float(input('Salário: '))
tempo = int(input('Tempo: '))
parcela = valor / ( tempo * 12)
if parcela > (.3 * salario):
      print('Financiamento negado!')
else:
    print('Sua parcela será R${}.'.format(parcela))