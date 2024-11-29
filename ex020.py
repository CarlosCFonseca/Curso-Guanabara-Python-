import random
a = input('Nome do aluno 1: ')
b = input('Nome do aluno 2: ')
c = input('Nome do aluno 3: ')
d = input('Nome do aluno 4: ')
lista = [a, b, c, d]
random.shuffle(lista)
print(lista)