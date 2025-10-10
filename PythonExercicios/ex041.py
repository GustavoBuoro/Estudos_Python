from datetime import date

nasc = int(input('Digite o ano de nascimento: '))

atual = date.today().year

idade = abs( atual- nasc)

if idade <= 9:
    print('voce é MIRIM')

elif idade <= 14:
    print('voce é de categoria infantil')

elif idade <= 19:
    print('voce é de categoria junior')

elif idade <= 25:
    print('voce é de categoria senior')

else:
    print('voce é de categoria master')