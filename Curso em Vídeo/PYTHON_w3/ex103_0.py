def cor(c):
    if c == 0:
        return '\033[0;0;0m'
    elif c == 1:
        return '\033[31m'
    elif c == 2:
        return '\033[33m'
    elif c == 3:
        return '\033[37m'
    elif c == 11:
        return '\033[1m'


def linha():
    print(f'{cor(2)}{"-=" * 20}-{cor(0)}')


def cabeca(txt):
    linha = '-=' * int((len(txt) + 10) / 2)
    espaço = ' ' * int((len(linha) - len(txt)) / 2)
    print(f'{cor(2)}{linha}-{cor(0)}')
    print(f'{espaço}{txt}')
    print(f'{cor(2)}{linha}-{cor(0)}')


def valida(j='', gol=0):
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    if j.strip() == '':
        ficha(g=gol)
    else:
        ficha(j, gol)


def ficha(j='<desconhecido>', g=0):
    print(f'O jogador {j.capitalize()} fez {g} gols no campeonato ')


cabeca('FICHA DO JOGADOR')
jogador = str(input('Nome: '))
gols = str(input('Nº de Gols: '))
linha()
valida(jogador, gols)
