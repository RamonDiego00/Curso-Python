horas = input("Que horas são?: ")

try:
    horas = int(horas)

    if horas <= 11 and horas >= 0:
        print("Obrigado tenha um bom dia! ")
    elif horas >= 12 and horas <= 17 :
        print("Obrigado tenha uma boa tarde! ")
    elif horas >=18 and horas <= 24:
        print("Obrigado tenha uma boa noite! ")
    else :
        print("Esse horário não existe ")
except:
    print(f'{horas} não é um número inteiro')