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
print(f'{" ANALIZANDO NÚMEROS V - LISTA ": ^40}')
print(borda)
# loop
while True:
    # input number
    n = int(input(f'{limpa}Digite um número: {negrito}'))
    l.append(n)
    opt = str(input(f'{limpa}Quer continuar? [S/N] {amarelo}'))
    if opt in 'Nn':
        break
par = []
impar = []
for i in l:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'{limpa}Lista completa {amarelo}{l}{limpa}')
print(f'{limpa}Lista pares {amarelo}{impar}{limpa}')
print(f'{limpa}Lista ímpares {amarelo}{par}{limpa}')
