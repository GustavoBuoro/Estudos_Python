somaidade = 0
homenvelho = ""
idademaisvelho = 0
mulheres20 = 0

    for i in range(1, 5):
    idade = int(input("Digite a sua idade: "))
    sex = str(input('Digite o sexo [M/F]: ')).upper().strip()
    nome = str(input('Digite o nome: ')).strip()

    somaidade += idade

    if sexo == 'M':
        if idade > idademaisvelho:
            idademaisvelho = idade
            homenvelho = nome

        if sexo == 'F' and idade < 20:
            mulheres20 += 1

    media = somaidade / 4

    print('a media do grupo é de {}'.format(media))
    if homenvelho :
      print('o homen mais velho é {}'.format(homenvelho))
    else:
      print('não há homens no grupo')
    print('ao todo são {} mulheres com menos de 20 anos'.format(mulheres20))