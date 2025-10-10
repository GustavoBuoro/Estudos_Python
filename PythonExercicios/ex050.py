soma = 0
contador = 0
for c in range(0,6):
    n = int(input('Digite um valor : '))
    if n % 2 == 0:
        print(n)
        soma += n
        contador = contador + 1
print('A soma de todos os valores {} pares escritos é {}'.format(contador,soma))