nome = input('Digite um nome: ').strip().lower()
print(f'Nome: {nome.split()[0]}\
    \nSobrenome: {nome.split()[len(nome.split()) - 1]}')
