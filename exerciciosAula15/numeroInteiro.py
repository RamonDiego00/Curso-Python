numero = input("Digite um número inteiro: ")

try:
    numero = int(numero)

    if numero % 2 == 0:
        print(f"O {numero} é par ")
    else:
        print(f"O {numero}  é impar ")

except:
    print(f'{numero} não é um número inteiro')