km = int(input("Qual a quantidade de km? "))

viagem = km * 0.50

viagem2 = (km * 0.45)

print('voce esta fazendo uma viagem de {} km'.format(km))

if km <= 200 : print('Voce está fazendo uma viagem de {} km e tera que pagar {}R$'.format(km,viagem))

elif km > 200 : print('Voce está fazendo uma viagem Longa de {} km e tera que pagar {}R$'.format(km,viagem2))