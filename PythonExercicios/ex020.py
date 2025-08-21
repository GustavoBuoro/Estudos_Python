import random

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

nomes = [a,b,c,d]

escolhidos = random.sample(nomes, 4)

print('o nome dos escolhidos foram : {} '.format(escolhidos))