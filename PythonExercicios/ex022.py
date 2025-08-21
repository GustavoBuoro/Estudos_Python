nome = str(input("Digite seu nome Completo: ")).strip()
print("Analisando o nome...")

print("seu nome em maiusculo é :"+nome.upper())
print("Seu nome em minusculo é :"+nome.lower())
#print("Seu nome tem ao todo {} : ".format(len(nome) - nome.count (' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
print('Seu primeiro nome tem  {} letras'.format(nome.find (' ')))


