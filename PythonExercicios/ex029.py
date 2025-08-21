
velocidade = int(input('Qual a sua velocidade? '))
multa = (velocidade - 80) * 7

if velocidade > 80:    print("MULTADO!! Voce excedeu o limite de velocidade que é 80km/h "
                              "Voce deve pagar uma multa de {}".format(multa))

else : print("Voce está numa velocidade segura abaxio 80km/h Aproveite seu dia!! ")