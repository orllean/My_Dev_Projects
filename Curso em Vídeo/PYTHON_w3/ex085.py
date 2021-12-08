# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
l = [[], []]
# start
print(borda)
print(f'{" ANALIZANDO NÚMEROS (PAR / ÍMPAR) - LISTA II ": ^40}')
print(borda)
# loop
for i in range(7):
    # input number
    n = int(input(f'{limpa}Digite um número: {amarelo}'))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
print(borda)
print(f'Lista dos pares{amarelo}{sorted(l[0])}{limpa}')
print(f'Lista dos ímpares{amarelo}{sorted(l[1])}{limpa}')
