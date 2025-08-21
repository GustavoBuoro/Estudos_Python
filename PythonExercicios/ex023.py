num = int(input('Digite um numero : '))
n= str(num)

print('analisando o numero {}'.format(num))

separa = n.split()

print('Unidade : {} '.format(n[0]))
print('Dezena : {} '.format(n[1]))
print('Centena : {} '.format(n[2]))
print('Milhar : {} '.format(n[3]))
