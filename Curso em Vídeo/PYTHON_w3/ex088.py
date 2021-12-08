from random import randint
from time import sleep
# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
s = f'{negrito}{amarelo}{"-+" * 5}-{limpa}'
jogos = []
# start
print(borda)
print(f'{" NÚMEROS DA MEGA SENA - LISTA COMPOSTA II ": ^40}')
print(borda)
# loop
# input number
nJogos = int(input(f'{limpa}Quantos jogos você quer que eu sortei? {amarelo}'))
print(f'{s} SORTENDO{amarelo} {nJogos}{limpa} JOGOS {s}')
for i in range(nJogos):
    aposta = []
    while len(aposta) < 6:
        num = randint(1, 60)
        if num not in aposta:
            aposta.append(num)
    aposta.sort()
    jogos.append(aposta[:])
for i in range(nJogos):
    print(f'JOGO {i + 1}:{amarelo} {jogos[i]}{limpa} ')
    sleep(1)
