frase = str(input('Digite uma palavra: ')).strip().upper()
palavras = p1.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('essa palavar é um palindromo')
else:
    print('essa palavra não é um palindromo')



