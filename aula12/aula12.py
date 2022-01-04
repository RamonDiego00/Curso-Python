usuario = input('Digite seu usuário:')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres')
else:
    print('Voce foi cadastrado no sistema')

# Mais um exemplo de uso do len()

string1 = input('Digite alguma coisa:')
string2 = input('Digite outra coisa:')

print(f'A quantidade total de caracteres digitados foi de: {len(string1) + len(string2)} ')