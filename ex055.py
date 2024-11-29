pesado = 0
leve = 0
for pess in range(1, 6):
    peso = float(input('Diga o peso da {}° pessoa: '.format(pess)))
    if pess == 1:
        pesado = peso
        leve = peso    
    if peso > pesado:
        pesado = peso
    if peso < leve:
        leve = peso
print('O peso medido mais leve foi {} e o peso mais pesado foi {}'. format(leve, pesado))