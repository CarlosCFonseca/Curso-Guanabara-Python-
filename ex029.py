# >80 = msg: foi multado
# multa custa 7,00 por km acima do limite

velocidade = float(input('Qual é a velocidade aferida? '))
if velocidade <= 80:
    print = str(input('Parabéns, {}km/hora está dentro da velocidade permitida na via!\nVocê é um ótimo mortorista!!!!!'.format(velocidade)))
else:
    multa = (velocidade-80)*7
    print = str(input('Você está acima da velocidade permitida da via e está multado em R${:.2f}.'.format(multa)))