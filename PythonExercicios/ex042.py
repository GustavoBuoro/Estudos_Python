l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))

print('um triangulo com os lados {} , {} e {} é um triangulo :4'.format(l1, l2, l3))

if l1==l2 and l2==l3:
    print('Voce tem um triangulo equilatero')

elif l1!=l2 and l2!=l3:
    print('Voce tem um triangulo escaleno')

else:
    print('voce tem um triangulo isoceles')
