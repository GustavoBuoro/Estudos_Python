import time

n1 = int(input('Digite um numero inteiro :'))

binario = bin(n1)
octal = oct(n1)
hexadecimal = hex(n1)

escolha = int(input('Escolha uma das bases para conversão \n '
                    '[1] converter para binario \n '
                    '[2] converter para octal \n '
                    '[3] converter para hexadecimal \n '
                    '[4] sair do programa \n '
                    'Digite sua opcao: '))

if escolha == 1:
    print('{}\033[0;33m convertido é {}'.format(n1, binario))

elif escolha == 2:
    print(' {}\033[0;34m convertido para octal {}'.format(n1, octal))

elif escolha == 3:
    print('{}\033[0;32m convertido para hexadecimal {}'.format(n1, hexadecimal))

elif escolha == 4:
    print('\033[4;35m FECHANDO PROGRAMA!')
    time.sleep(2)