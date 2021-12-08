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
print(f'{" ANALIZANDO NÚMEROS III - LISTA ": ^40}')
print(borda)
# loop / input
for i in range(5):
    num = int(input(f'{limpa}Digite um valor: {negrito}'))
    # check if num is first or max [l] and append it
    if len(l) == 0 or num > max(l):
        l.append(num)
        print(f'{vermelho}add ao final da lista{limpa}')
    else:
        # loop in [l]
        for c, j in enumerate(l):
            # check if num is less then index[l] and append it
            if num < j:
                l.insert(c, num)
                print(f'{limpa}add ao index: {amarelo}[{c}]{limpa}')
                break
print(borda)
# output
print(f'Valores em ordem crescente {amarelo}{l}')
