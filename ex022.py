    # nome completo
    #maiusculo
    #minusculo
    #quantas letras ao todo sem contar os espaços
    #quantas letras tem o primeiro nome
nome = str(input('Nome completo: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
letras = len(nome)-nome.count(' ')
primeiro = nome.find(' ')
prime = nome.split()
prim = len(prime[0])
print(maiusculo)
print(minusculo)
print(letras)
print(primeiro)
print(prime)
print(prim)
