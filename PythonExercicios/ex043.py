peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

print('o seu imc é {}'.format(imc))

if imc < 18.5:
    print('voce está abaixo do peso')

elif imc >= 18.5 and imc <= 25:
    print('voce está com peso ideal')

elif imc >= 25 and imc <= 30:
    print('voce está com sobrepeso')

elif imc >= 30 and imc <= 40:
    print('voce está com obesidade')

else:
    print('voce está com obesidade morbida')