from datetime import date
anoAtual = date.today().year
totalMaior = 0
totalMenor = 0

for pess in range(1, 8):
        nascimento = int(input('Em que ano a {}º pessoa nasceu : ').format(pess))
        idade = anoAtual - nascimento
        if idade >= 21:
            print('maior de idade')
            totalMaior += 1

        else:
            print('menor de idade')
            totalMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalMaior))
print('e {} pessoas menores de idade'.format(totalMenor))