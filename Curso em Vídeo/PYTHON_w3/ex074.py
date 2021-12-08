from random import randint
# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
num = ' '
# start
print(borda)
print(f'{" NÚMEROS ALEATÓRIOS - TUPLA ": ^40}')
print(borda)
# loop / random num
for i in range(5):
    s = str(randint(0, 100))
    num = num + ' ' + s
# set tupla
t = tuple(int(i) for i in num.strip().split(' '))
# output
print(f'{negrito}{vermelho}Os números sorteados foram:\n{limpa}{amarelo}{t}')
print(f'{negrito}{vermelho}O menor número é:{limpa}{amarelo} {min(t)}')
print(f'{negrito}{vermelho}O maior número é:{limpa}{amarelo} {max(t)}')
