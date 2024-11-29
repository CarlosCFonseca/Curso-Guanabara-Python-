print('                        ')
print('                        ')
print('='*27)
print('     LOJA DO CARLÃO     ')
print('='*27)
print('                        ')
print('                        ')
p = float(input('Valor total da compra: (R$) '))
print('                        ')
print('''Qual será a forma de pagamento:
      
      [ 1 ] à vista: dinheiro / cheque: 10% de desconto
      [ 2 ] à vista no cartão: 5% de desconto
      [ 3 ] em até 2x no cartão: preço normal
      [ 4 ] 3x ou mais: 20% de juros''')
print('                        ')
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    total = p - (p * 10 / 100)
    print('O valor a ser pago será R${:.2f}.'.format(total))
elif opcao == 2:
      total = p - (p * 5 / 100)
      print('O valor a ser pago será R${:.2f}.'.format(total))
elif opcao == 3:
     print('O valor a ser pago será R${:.2f}.'.format(p))
elif opcao == 4:
     total = p + (p * 20 / 100)
     print('O valor a ser pago será R${:.2f}.'.format(total))
