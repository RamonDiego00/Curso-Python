"""
Formatando valores

:s - Textos
:d - Inteiros
:f - Numeros de ponto flutuante :.2f
:. - Quantidade de casas decimais
: - Caractere, quantidade, tipo

> Esquerda
< Direita
^ Centro

"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print(f'{divisao:.2f}')

nome = 'Ramon'
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10.2f}')

print(len('############'))
print(f'{nome:#^50}')
sobrenome = 'Diego'
nome_formatado = '{0:@>6} {1:%^10}'.format(nome, sobrenome)
print(nome_formatado)

nome = nome.ljust(10, '#')
print(nome)
