import math
import random

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

nomes = [a,b,c,d]

print('o nome escolhido foi : ' + random.choice(nomes))