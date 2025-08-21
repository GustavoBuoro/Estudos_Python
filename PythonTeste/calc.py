def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: divisão por zero"

print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado:", somar(num1, num2))
elif opcao == '2':
    print("Resultado:", subtrair(num1, num2))
elif opcao == '3':
    print("Resultado:", multiplicar(num1, num2))
elif opcao == '4':
    print("Resultado:", dividir(num1, num2))
else:
    print("Opção inválida")



