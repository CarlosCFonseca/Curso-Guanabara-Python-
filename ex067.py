m = n = 0
n = int(input(' Quer ver a tabuada de qual valor? '))
while n >= 0:
    for m in range(0, 11):
        t = n * m 
        print(f' {n} x {m:2} = {t:2}')
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
print('O programa foi interrompido.')