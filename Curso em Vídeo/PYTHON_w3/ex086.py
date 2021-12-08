# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
mtz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# start
print(borda)
print(f'{" MATRIZ 3X3 - LISTA II ": ^40}')
print(borda)
# loop  matriz 3 x 3 INPUT
for i in range(3):
    for j in range(3):
        # input number
        mtz[i][j] = int(
            input(f'{limpa}Digite um valor na posição [{i}, {j}]: {amarelo}'))
print(borda)
# loop  matriz 3 x 3 OUTPUT
for i in range(3):
    for j in range(3):
        print(f'[{mtz[i][j]:^6}]', end='')
    print()
