# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
l = []
# start
print(borda)
print(f'{" ANALIZANDO NÚMEROS I - LISTA ": ^40}')
print(borda)
# loop / input
for i in range(5):
    num = int(input(f'{limpa}Digite um valor para index [{i}]: {vermelho}'))
    l.append(num)
print(borda)
# task 1. show [l] vaules 2. show max item and index 3. show min item and index
# output
print(f'Os valores digitados foram: {amarelo}{l}{limpa}')
print(
    f'O maior valore digitado foi: {negrito}{vermelho}{max(l)}{limpa} no index ', end='')
for c, i in enumerate(l):
    if i == max(l):
        print(f'{vermelho}{c}{limpa}.. ', end='')
print(
    f'\nO menor valore digitado foi: {negrito}{vermelho}{min(l)}{limpa} no index ', end='')
for c, i in enumerate(l):
    if i == min(l):
        print(f'{vermelho}{c}{limpa}.. ', end='')
