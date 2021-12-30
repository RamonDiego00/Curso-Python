"""
*Criar varaiveis para nome (str),idade (int)
*altura(float) e peso(float) de uma pessoa
*Craiar variável com o ano atual(int)
*Obter o ano de nasciemnto da pessoa(baseado na idade e no ano atual)
*Obter o Imc da pessoa com 2 casas decimais
*Exibir um texto com todos os valores na tela usando F-Strings (com as chavez)
"""
import datetime

nome = 'Ramon'
idade = 18
altura = 1.70
peso= 65.0
date = datetime.date.today()
ano_atual = date.strftime("%Y")
nascimento = int(ano_atual) - idade
imc = peso / (altura**2)

print(nome, 'tem',idade, 'anos,',altura ,'de altura e pesa',int(peso),'kg')
print(ano_atual)
print(f'Você nasceu no ano de:{nascimento}')
print(f'{nome} tem  {idade} de idade e seu imc é {imc:.2f}')

