nome = str(input("Digite seu nome Completo: ")).strip().upper()

print("Analisando o nome...")

separa = nome.split()

print('Seu primeiro nome é {} '.format(nome[0]))

print('Seu ultimo nome é {} '.format(nome[len(nome)-1]))
