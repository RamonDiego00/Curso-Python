nome = 'Ramon'
idade = 18
altura = 1.70
e_maior = idade >= 18
data_atual = 2021
peso = 65
imc = peso / (altura**2)

print(nome, 'tem ', idade, 'de idade e seu imc é ',imc)

print(f'{nome} tem {idade} de idade e seu imc é: {imc:.2f}')
print('{1} {0} {0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))

print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))