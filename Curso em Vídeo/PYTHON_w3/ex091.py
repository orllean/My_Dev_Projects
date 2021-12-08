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
print(f'{" JOGAR DADOS MAIS RANK - DICIONÁRIO ": ^40}')
print(borda)
# set dictionario
play = {}
# set values
play['Player_1'] = randint(1, 6)
play['Player_2'] = randint(1, 6)
play['Player_3'] = randint(1, 6)
play['Player_4'] = randint(1, 6)
# loop dict for output
for k, i in play.items():
    print(f'{k} tirou: {i}')
    sleep(1)
print(separador)
# rank the dict
cnt = 1
while len(play) > 0:
    for k, i in play.items():
        if i == max(play.values()):
            print(f'{cnt}º Lugar: {k} com {i}')
            sleep(1)
            cnt += 1
            del play[k]
            break
print(fim)
