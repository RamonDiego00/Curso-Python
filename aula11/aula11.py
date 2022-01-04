"""
Operadores Lógicos - Aula 4
and, or, not
in e not in
"""
# Verdadeiro E Falso = Falso
# comp1 and comp2

# Verdadeiro ou Falso = Verdadeiro
# comp1 or comp2

a = 2
b =3
c = 0
d = ''

if not b > a:
    print('B é maior que A')
else:
    print('A é maior que B')

if not d:
    print('Coloque um valor dentro de D')

nome = input('Qual o seu nome?')

if 'u' in nome:
    print("Existe a letra U no seu nome")
else:
    print("Não existe a letra U no seu nome")

pokemon = input('Qual o seu nome de pokemon?')

if 'mon' not in pokemon:
    print("Você não é um pokemon")
else:
    print("Belo nome de pokemon")