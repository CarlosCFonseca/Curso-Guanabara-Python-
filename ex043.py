p = float(input('Qual é o seu peso? (Kg)'))
h = float(input('Qual a sua altura? (m)'))
imc = p / (h ** 2)
if imc < 18.5:
   print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
   print('normal')
elif 25 <= imc < 30:
   print('sobrepeso')
elif 30 <= imc < 40:
   print('Obesidade')
elif imc >= 40:
   print('Obesidade mórbida')
