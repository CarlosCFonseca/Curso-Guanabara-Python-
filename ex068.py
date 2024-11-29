from random import randint
escjog = 1
res = 2
cont = -1
while True:
    cont +=1
    ini = int(input('quem começa? voce = 1 ou comp =2: '))
    if ini == 1:
        escjog = int(input('escolha: par = 1 ou ímpar = 2: '))
        if escjog == 1:
            esccomp = 2
            print('o jogador escolheu par e o computador escolheu impar')
        else:
            esccomp = 1
            print('o jogador escolheu impar e o computador escolheu par')
    else:
        esccomp = randint(1,2)
        print(f' Computador escolhe: [ {esccomp} ] ', end='')
        if esccomp == 1:
            print('Par')
        else:
            print('Ímpar')
    print('Vamos jogar! 1, 2, 3 e já')
    comp = randint (0, 5)
    print(f'O computador jogou colacando {comp}.')
    jog = int(input('Digite quanto quer colocar: '))
    res = jog + comp
    print(f'Resultado:{res}')
    if res%2 == 0:
        print(f'Escolha do computador foi {esccomp} - 1 (par) ou 2 (ímpar)')
        print(f'REsto da divisão po 2 é {res%2}, sendo 0 = par e !=0 = ímpar')
        if esccomp == 1:
            print(f'O computador jogou {comp} e você jogou {jog}, o reultado foi {res}, logo o computador, que pediu par, venceu')
            break
        else:
            print(f'O computador jogou {comp} e você jogou {jog}, o reultado foi {res}, logo você, que pediu par, venceu')
    else:
        print(f'Escolha do computador foi {esccomp} - 1 (par) ou 2 (ímpar)')
        print(f'REsto da divisão po 2 é {res%2}, sendo 0 = par e !=0 = ímpar')
        if esccomp == 1:
            print(f'O computador jogou {comp} e você jogou {jog}, o reultado foi {res}, logo você, que pediu ´mpar, venceu')
        else:
            print(f'O computador jogou {comp} e você jogou {jog}, o reultado foi {res}, logo o computador, que pediu ímpar, venceu')
            break
print(f'Você perdeu, mas conseguiu vencer o computador {cont} vez(es) consecutivamente.')