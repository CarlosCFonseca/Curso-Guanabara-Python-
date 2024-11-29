# quantas letras "a" tem, onde é a primeira e onde é a ultima
frase = str(input('Escreva uma frase: ')).strip().upper()
print('Na frase "{}",temos um total de letras "a" de {}, sendo a primeira na posição {} e a ultima na posçaõ {}.'.format(frase, frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))