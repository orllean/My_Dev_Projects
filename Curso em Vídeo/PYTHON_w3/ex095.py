# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
linha = f'{negrito}{amarelo}{"-+" * 20}-{limpa}'
fim = (f'{negrito}{vermelho}{">>>" * 5} FINALIZADO {"<<<" * 5}{limpa}')
# start
print(borda)
print(f'{" ANALIZANDO DESEMPENHO II - DICIONÁRIO ": ^40}')
print(borda)
time = []
cod = 0
# get data
while True:
    jogador = {}
    gol = []
    jogador['cod'] = cod
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(p):
        gol.append(int(input(f'Quantos gols na partida [{i}]: ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    time.append(jogador.copy())
    cod += 1
    # test opt
    opt = str(
        input(f'{limpa}Quer continuar? [S/N]').upper())
    if opt in 'Nn':
        break
print(borda)
# output acbeçalho
for i in time[0].keys():
    if i == 'cod':
        print(f'{str(i):>5} ', end='')
    else:
        print(f'{str(i):<15}', end='')
print(f'\n{linha}')
# output dados
for i in time:
    for k, i in i.items():
        if k == 'cod':
            print(f'{vermelho}{str(i):>5} ', end='')
        else:
            print(f'{limpa}{str(i):<15}', end='')
    print()
print(f'{linha}')
while True:
    j = int(input(f'Mostra dados de qual jogador [cod]? '))
    if j == 999:
        print(fim)
        break
    elif j > (len(time) - 1):
        print(f'{amarelo}Jogador não cadastrado{limpa} ')
    else:
        print(f'Detalhamento do jogador {time[j]["nome"]} ')
        for e, i in enumerate(time[j]["gols"]):
            print(f'Na partida [{e}], marcou {i} gols. ')
        print(linha)
