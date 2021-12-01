nome = str(input('Digite seu nome completo: ')).strip() # remove carctres brancos no input

print(f'UPPER: {nome.upper()}\
    \nlower: {nome.lower()}\
    \nCaptalize: {nome.capitalize()}\
    \nTitle: {nome.title()}\
    \ntotal de nomes: {len(nome.split())}\
    \ntotal carc s/ espaços: {len(nome) - nome.count(" ")}\
    \ntotal de caracteres do primeiro nome: {len(nome.split()[0])}')
