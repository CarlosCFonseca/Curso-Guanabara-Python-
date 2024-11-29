n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
opcao = 1
soma = 0
mult = 0
while opcao != 5:
    opcao = int(input('''Escolha no menu abaixo:
                  [ 1 ] SOMAR
                  [ 2 ] MULTIPLICAR
                  [ 3 ] MAIOR
                  [ 4 ] NOVOS NUMEROS
                  [ 5 ] SAIR DO PROGRAMA
                  '''))
    if opcao == 1:
        soma = n1 + n2
        print('A soma é {}.'.format(soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação é {}'. format(mult))
    elif opcao == 3:
        if n1 > n2:
            print('O maior é o {}.'.format(n1))
        else:
            print('O maior é o {}.'.format(n2))
    elif opcao == 4:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite um numero: '))
    elif opcao == 5:
        print('Você saiu do programa.')
    else:
        print('Opção inválida, tente novamente')