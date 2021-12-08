# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
pessoas = []
# start
print(borda)
print(f'{" ANALIZANDO CADASTROS - LISTA COMPOSTA I ": ^40}')
print(borda)
# loop record
while True:
    # set ampty list cad
    cad = []
    # input number
    nome = str(input(f'{limpa}Nome: {vermelho}'))
    cad.append(nome)
    peso = float(input(f'{limpa}Peso: {vermelho}'))
    cad.append(peso)
    # add 1 cad to pessoas
    pessoas.append(cad[:])
    # test opt
    opt = str(input(f'{limpa}Quer continuar? [S/N] {vermelho}'))
    if opt in 'Nn':
        break
# task 1 tot cad 2 lista pessoas mais pesadas 3 lista pessoas mais leves
print(borda)
print(f'{limpa}Total de cadastros:{amarelo} {len(pessoas)}')
pesos = []
for i in pessoas:
    pesos.append(i[1])
maxPeso = max(pesos)
minPeso = min(pesos)
print(f'{limpa}O maior peso foi:{amarelo} {maxPeso}{limpa} Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == maxPeso:
        print(f'{amarelo}{i[0]} ', end='')
print(f'\n{limpa}O menor peso foi:{amarelo} {minPeso}{limpa} Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == minPeso:
        print(f'{amarelo}{i[0]} ', end='')
