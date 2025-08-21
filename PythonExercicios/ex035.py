r1 = float(input('\033[32mPrimeiro valor: '))
r2 = float(input('\033[34mSegundo valor: '))
r3 = float(input('\033[35mTerceiro valor: '))

if r1+r2>r3 and r1+r2>r3 and r3+r2>r1 :
    print('\033[0;30;43mVoce consegue formar um triangulo')

else:
    print('\033[0;30;41mVoce nao consegue formar um triangulo')