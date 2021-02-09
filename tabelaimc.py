altura = float (input('ALTURA:'))
peso = float (input('PESO: '))
imc = peso / (altura**2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
  print('Peso normal')
elif 25 <= imc < 30:
  print('Sobrepeso')
elif 30 <= imc < 40:
  print('Obesidade')
elif 40 >= 40:
  print('Obesidade Morbida')
