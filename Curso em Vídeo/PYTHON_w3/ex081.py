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
print(f'{" ANALIZANDO NÚMEROS IV - LISTA ": ^40}')
print(borda)
# loop
while True:
    # input number
    n = int(input(f'{limpa}Digite um número: {negrito}'))
    l.append(n)
    opt = str(input(f'{limpa}Quer continuar? [S/N] {amarelo}'))
    if opt in 'Nn':
        break
print(f'{limpa}Ao todo foram digitados {amarelo}{len(l)}{limpa} números')
print(f'{limpa}Números em ordem decescente {amarelo}{sorted(l, reverse=True)}{limpa} números')
if 5 in l:
    print(f'{limpa}Ao todo foram digitados {amarelo}{l.count(5)}{limpa} números 5')
else:
    print('O número 5 não foi digitado')
