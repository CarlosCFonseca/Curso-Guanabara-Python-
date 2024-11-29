# advinhar o numero de 0 a 5 que o computador pensou
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, quero ver vc advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(5)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei!!! Eu pensei no número {} e não no número {}'.format(computador, jogador))






"""num = [0, 1, 2, 3, 4, 5]
print(random.choice(num))
if numero == random.choice(num):
    print('Acertou!')
else:
    print('Errrrrrooooouuuuuuu!') """
