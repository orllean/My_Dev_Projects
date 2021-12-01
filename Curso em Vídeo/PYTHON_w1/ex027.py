nome = input('Digite um nome: ')
print(f'Nome: {nome[:nome.find(" ")]}\
    \nSobrenome: {nome[nome.rfind(" ") + 1:]}')
