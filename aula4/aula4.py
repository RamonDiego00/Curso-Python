"""
Tipos de dados
str - string
int - inteiro
float - real
bool - booleano/lógico
"""
from builtins import print

print( 'Ramon', type('Ramon'))
print(123, type(123))
print( 25.23, type(25.23))
print( 10 == 10 , type(10 == 10))


print('luiz', type('luiz'), bool('luiz'))

print(10, type(10), type(int('10')))

print('Ramon', float('10.5'))

# print('10' + 10)  # Isso dá erro

print('Ramon',type('Ramon'))

print(18, type(18))

print(1.70, type(1.70))

print('Maior de idade:',18 >= 18,type(18 >= 18))
