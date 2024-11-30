cont = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove', 
         'dez', 'onze', 'doze', 'treze', 'catorze', 
         'quinze', 'dezasseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
        perg = str(input('Você quer continuar? [S/N]')).strip().upper()[0]        
        if perg == 'S':
            num = int(input('Digite um número entre 0 e 20: '))
        else:
            break
    else:
        print('Tente novamente. ', end='')
        num = int(input('Digite um número entre 0 e 20: '))

