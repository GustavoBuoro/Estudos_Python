n = str(input('Digite seu sexo [M/F] ')).strip().upper()[0]
while n not in 'MmFf':
    n = str(input('Sexo invalido Digitado , Por favor digite o numero certo :  ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(n))
