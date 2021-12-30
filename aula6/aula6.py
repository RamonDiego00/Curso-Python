"""
Iniciar com letra, pode conter números, separar _, letras minusculas
"""

nome = 'Ramon'
idade = 18
altura = 1.70
e_maior = idade >= 18
data_atual = 2021
peso = 65
imc = peso / (altura**2)

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(e_maior, type(e_maior))

print(nome, 'tem ', idade, 'de idade e seu imc é ',imc)