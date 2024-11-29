sexo = str(input('SEXO: [M/F]:')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos. Por favor informe seus dados: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
