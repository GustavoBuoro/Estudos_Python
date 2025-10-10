n1 = int(input('Digite um numero: '))

for c in range(0,n1+1):
    if n1 % c == 0 :
        print('/033[34m',end='')
    else:
        print('/033[33m',end='')
    print('{} '.format(c),end='')
