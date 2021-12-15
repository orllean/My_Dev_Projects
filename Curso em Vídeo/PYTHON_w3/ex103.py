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


def ficha(j='', g=''):
    j = '<desconhecido>' if j.strip() == '' else j
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    print(f'O jogador {j.capitalize()} fez {g} gols no campeonato ')


cabeca('FICHA DO JOGADOR')
jogador = str(input('Nome: '))
gols = str(input('Nº de Gols: '))
linha()
ficha(g=gols)
linha()
ficha(jogador, gols)
