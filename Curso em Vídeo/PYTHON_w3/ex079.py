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
print(f'{" ANALIZANDO NÚMEROS II - LISTA ": ^40}')
print(borda)
# loop
while True:
    # input number
    n = int(input(f'Digite um número: {negrito}'))
    # check if number is not in list. and add it
    if n not in l:
        print(f'{limpa}Valor add com {amarelo}sucesso...')
        l.append(n)
    else:
        print(f'{limpa}Valor não add {vermelho}duplicado...')
    # break the loop
    opt = str(input(f'{limpa}Quer continuar? [S/N] ')).lower()
    if opt == 'n':
        break
# output
print(f'{limpa}Os valores add foram; {amarelo}{sorted(l)}')
