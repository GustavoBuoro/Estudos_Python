import math

angulo = float( input('Digite um angulo : '))



seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo de {} tem o seno de : {:.3}'.format(angulo, seno))
print('O angulo de {} tem o coseno de : {:.3}'.format(angulo, coseno))
print('O angulo de {} tem a tangente de : {:.3}'.format(angulo, tangente))