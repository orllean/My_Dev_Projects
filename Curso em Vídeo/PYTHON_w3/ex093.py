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
print(f'{" ANALIZANDO DESEMPENHO - DICIONÁRIO ": ^40}')
print(borda)
jogador = {}
gol = []
# get data
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(p):
    gol.append(int(input(f'Quantos gols na partida [{i}]: ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print(borda)
print(jogador)
print(separador)
for k, i in jogador.items():
    print(f'{k:.<15}{i} ')
print(separador)
print(f'O jogador {jogador["nome"]} fez {len(jogador["gols"])} partidas.')
for k, i in jogador.items():
    if k == 'gols':
        for e, j in enumerate(i):
            print(f'Na partida [{e}], marcou {j} gols. ')
print(separador)
print(f'Total de gols marcados: {jogador["total"]}')
print(fim)
