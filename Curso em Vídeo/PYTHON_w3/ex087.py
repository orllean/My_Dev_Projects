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
print(f'{" ANALIZANDO MATRIZ 3X3 - LISTA II ": ^40}')
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
print(borda)
# task 1-soma valores pares 2-soma 3a colula 3-maior valor 2a linha
maior = somaCol = somaPar = 0
for i in range(3):
    for j in range(3):
        if mtz[i][j] % 2 == 0:
            somaPar += mtz[i][j]
        if j == 2:
            somaCol += mtz[i][j]
        if i == 1:
            if j == 0:
                maior = mtz[i][j]
            elif maior < mtz[i][j]:
                maior = mtz[i][j]
print(f'A soma dos valores pares é:{amarelo} {somaPar}{limpa} ')
print(f'A soma dos valores da 3 coluna é:{amarelo} {somaCol}{limpa} ')
print(f'Maior valor da 2 linha é:{amarelo} {maior}{limpa} ')
