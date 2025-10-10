from random import randint
from time import sleep

print('Suas opcçoes: \n'
      '[0]Pedra \n'
      '[1]Papel \n'
      '[2] Tesoura \n')

jogador = int(input('Qual a sua jogada? '))

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
print('+ '*10)
print("O computador escolheu :{}".format(itens[computador]))
print("O jogo escolheu :{}".format(itens[jogador]))
print("+ "*10)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")


if computador == 0:
    if jogador == 0:
        print('\033[0;31m EMPATOU !!')
    if jogador == 1:
        print('\033[0;31m JOGADOR VENCEU !!')
    if jogador == 2:
        print('\033[0;31m COMPUTADOR VENCEU !!')
elif computador == 1:
    if jogador == 0:
        print('\033[0;31m JOGADOR VENCEU !!')
    if jogador == 1:
        print('\033[0;31m COMPUTADOR VENCEU !!')
    if jogador == 2:
        print('\033[0;31m JOGADOR VENCEU !!')
elif computador == 2:
    if jogador == 0:
        print('\033[0;31m JOGADOR VENCEU !!')
    if jogador == 1:
        print('\033[0;31m COMPUTADOR VENCEU !!')
    if jogador == 2:
        print('\033[0;31m JOGADOR VENCEU !!')
else:
    print("\033 [4;31m OPÇÂO INVALIDA !!")
