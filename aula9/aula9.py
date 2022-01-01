"""
Entrada de dados - Aula 23
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade ? ")

ano_nascimento = 2022 - int(idade)

print()
print(f'{nome} tem {idade} anos e nasceu no ano de {ano_nascimento} ')