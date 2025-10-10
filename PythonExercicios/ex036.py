import time

casa = float(input('Qual o preço da casa?'))
salario = float(input('Qual o seu salario?'))
anos = int(input('Quantos anos de financiamento?'))

prestacao = casa / (anos * 12)

minimo = (salario*30) /100

print('Para pagar uma cada de R${:.2} em {} anos '.format(prestacao, anos), end='')
print("A prestaão sera de R${:.2f} }".format(prestacao))

if prestacao <= minimo:
    print('Empréstimo aprovado')
else:
    print('Emprestimo reprovado')

