from datetime import date

atual = date.today().year

nasc = int(input('Digite o ano de nascimento: '))

idade= abs(nasc - atual)

print('quem nasceu em {} tem {} em 2025'.format(nasc,idade))

if idade < 18:
    print('Voce está novo para se alistar, falta {} anos para voce se alistar'.format(abs(idade-18)))
elif idade == 18:
    print('Voce está no tempo certo para se alistar')

elif idade > 18:
    print('voce já passou do tempo de alistar, voce devia ter se alistado em {}'.format(nasc-18))



