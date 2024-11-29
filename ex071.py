while True:
    saque = int(input('Valor a ser sacado: R$'))
    if saque//50 >= 1:
        nota50 = saque//50
        resto = saque%50
    else:
        nota50 = 0
        resto = saque
    if resto//20 >= 1:
        nota20 = resto//20
        resto = resto%20
    else:
        nota20 = 0
    if resto//10 >= 1:
        nota10 = resto//10
        resto = resto%10
    else:
        nota10 = 0
    if resto//1 >= 1:
        nota1 = resto//1
    else:
        nota1 = 0
    print(f'Notas de 50:{nota50}, notas de 20: {nota20}, notas de 10: {nota10} e notas de 1: {nota1}.')
    quest= str(input('Gostaria de realiza outro saque? [ S/N ]: '))
    if quest in 'Nn':
        break
print('Obrigado e volte sempre.')
