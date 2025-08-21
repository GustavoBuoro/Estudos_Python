frase = str(input('Digite uma frase: ')).strip().upper()
pontos = frase.count('A')

print('A letra "A" aparece {} vezes'.format(pontos))

print('A primeira letra "A" aparece na posicaço {}'.format(frase.find('A')+1))
print('A ultima letra "A" aparece na posicaço {}'.format(frase.rfind('A')+1))
