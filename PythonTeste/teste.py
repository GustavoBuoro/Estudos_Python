n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


numeros = [n1, n2, n3]


for num in numeros:
    print(f'\nTabuada do {num}:')
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')