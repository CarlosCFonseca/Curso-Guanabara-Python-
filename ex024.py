# Verificar se a cidade comça com a palavra "Santo"
cid = str(input('Em que cidade vc nasceu? ')).strip()
print(cid[:5])
print(cid[:5].upper() == 'SANTO')