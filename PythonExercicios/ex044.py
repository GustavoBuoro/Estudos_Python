import time
from time import sleep

valor = float(input('Digite o valor do produto: '))

avistacheque =  (valor *10)/100

avistacartao =  valor *0.05

cartao2x = valor /2

cartao3x = valor *20/100

escolha = int(input('Escolha uma das formas de pagamento \n '
                    '[1] avista dinheiro ou cheque = 10% \n '
                    '[2] avista cartão = 5% \n '
                    '[3] 2x no cartão = preço formal \n '
                    '[4] 3x ou mais = 20% \n '
                    'Digite sua opcao: '))

print('CALCULANDO...')
time.sleep(3)

if escolha == 1:
    print('voce tera que pagar {}'.format(avistacheque))

elif escolha == 2:
    print('voce tera que pagar {}'.format(avistacartao))

elif escolha == 3:
    print('voce tera que pagar duas parcelas de {}'.format(cartao2x))

elif escolha == 4:
  print('voce tera que pagar {}'.format(cartao3x))

else:
    print('\033[0;31m ESCOLHA INVALIDA !!')

