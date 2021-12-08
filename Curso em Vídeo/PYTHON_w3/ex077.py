# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
v = ('a', 'e', 'i', 'o', 'u')
# set tupla
p = ('caderno', 'caneta', 'monitor', 'papel', 'copo', 'cadeira')
# start
print(borda)
print(f'{" LISTAGEM DE VOGAIS - TUPLA ": ^40}')
print(borda)
for i in p:
    print(f'{limpa}\nNa palavra {i.upper()} temos: ', end='')
    for j in i:
        if j in v:
            print(f' {amarelo}{j}', end='')
print(f'\n{borda}')
