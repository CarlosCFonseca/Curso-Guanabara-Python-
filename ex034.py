salario = float(input('Qual é o seu salário? '))
if salario > 1250:
    aumento = 1.1*salario
else:
    aumento = 1.15*salario
print('Seu novo salário será: R${:.2f}.'.format(aumento))