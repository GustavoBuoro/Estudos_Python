n1 = int(input('Digite o numero que deseja saber a tabuada: '))

for c in range(1,11):
    print('{} x {} = {}'.format(n1, c, n1*c))