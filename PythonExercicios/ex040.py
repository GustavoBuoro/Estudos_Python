n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2

print('tirando {} e {} sua média é {}'.format(n1, n2, media))

if media >= 7 :
    print('voce foi aprovado!!')

elif media < 5 :
    print('voce foi reprovado!!')

else :
    print('voce ficou de recuperação')