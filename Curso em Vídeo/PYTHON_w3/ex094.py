# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
linha = f'{negrito}{amarelo}{"-+" * 12}-{limpa}'
fim = (f'{negrito}{vermelho}{">>>" * 5} FINALIZADO {"<<<" * 5}{limpa}')
pessoas = list()
# start
print(borda)
print(f'{" ANALIZANDO CADASTRO II - DICIONÁRIO ": ^40}')
print(borda)
# loop get data
while True:
    pessoa = dict()
    # input data into the dictionario
    pessoa['Nome'] = str(input(f'{limpa}Nome:{amarelo} ')).capitalize()
    pessoa['Idade'] = int(input(f'{limpa}Idade:{amarelo} '))
    pessoa['Sexo'] = str(input(f'{limpa}Sexo [M/F]{amarelo} : ')).capitalize()
    # append the dictionario into the list
    pessoas.append(pessoa.copy())
    # test opt
    opt = str(
        input(f'{limpa}Quer continuar? [S/N]{amarelo}').upper())
    if opt in 'Nn':
        break
# tasks
# 1. tot pessoas cadastradas
# 2. média de idade
# 3. mulheres cadastradas
# 4. lista: pessoas acima da média de idade
print(linha)
print(f'{limpa}Total de cadastros: {len(pessoas)}')
# task 2.
totIdade = 0
for i in pessoas:
    for j in i.items():
        if j[0] == 'Idade':
            totIdade += j[1]
mIdade = totIdade / len(pessoas)
print(f'{limpa}Média de idade: {mIdade:.2f}')
print(linha)
# task 3.
print(f'{limpa}Mulheres cadastradas:')
for i in pessoas:
    for k, j in i.items():
        if k == 'Sexo' and j == 'F':
            print(f'{i["Nome"]}')
print(linha)
# task 4.
print(f'{limpa}Acima da média de idade:')
for k, j in i.items():
    print(f'{k.upper():<8}', end=' ')
print()
for i in pessoas:
    if i['Idade'] > mIdade:
        for k, j in i.items():
            if k != 'Idade':
                print(f'{j.upper():.<8}', end=' ')
            else:
                print(f'{j:.<8}', end=' ')
        print()
print(f'{fim}')
