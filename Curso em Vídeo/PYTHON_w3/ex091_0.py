from operator import itemgetter
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
separador = f'{negrito}{amarelo}{"-+" * 12}-{limpa}'
fim = (f'{negrito}{vermelho}{">>>" * 5} FINALIZADO {"<<<" * 5}{limpa}')
# start
print(borda)
print(f'{" JOGAR DADOS MAIS RANK II - DICIONÁRIO ": ^40}')
print(borda)
play = {'Player_1': randint(1, 6),
        'Player_2': randint(1, 6),
        'Player_3': randint(1, 6),
        'Player_4': randint(1, 6)}
for k, i in play.items():
    print(f'{k} tirou: {i}')
    sleep(1)
print(separador)
ranking = []
ranking = sorted(play.items(), key=itemgetter(1), reverse=True)
for e, i in enumerate(ranking):
    print(f'{e + 1}º Lugar {i[0]} com {i[1]}')
    sleep(1)
print(fim)
