

a = input('Digite algo: ')

print('O tipo primitivo desse vale {}'.format(type(a)))
print('é um numero?', a.isnumeric())
print('é alfabeto?', a.isalpha())
print('tem espacos?', a.isspace())
print('é alphanumeric?', a.isalnum())
print('está em maiusculas?', a.isupper())
print('esta em minusculas?', a.islower())
print('esta capitalizada?', a.istitle())
