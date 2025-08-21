import random

res = int(input('Escolha um numero entre 0 e 5: '))

num = random.randint(0,5)

if res == num:print('Voce acertou!! O numero escolhido foi {}'.format(num))

else: print("voce errou! O numero escolhido foi {}".format(num))