def cor(c):
    if c == 0:
        return '\033[0;0;0m'  # limpa - 0
    elif c == 1:
        return '\033[30m'  # preto - 1
    elif c == 2:
        return '\033[33m'  # amarelo - 2
    elif c == 3:
        return '\033[7m'  # invertido - 3
    elif c == 11:
        return '\033[1m'  # negrito - 11


def fundo(f):
    if f == 0:
        return '\033[47m'  # branco - 0
    elif f == 1:
        return '\033[42m'  # verde - 1
    elif f == 2:
        return '\033[44m'  # azul - 2
    elif f == 3:
        return '\033[41m'  # vemelho - 3


def cabeca(txt):
    linha = '-=' * int((len(txt) + 10) / 2)
    espaço = ' ' * int((len(linha) - len(txt)) / 2)
    print(f'{cor(11)}{fundo(1)}{linha}-')
    print(f'{espaço}{txt}')
    print(f'{linha}-{cor(0)}')


def corpo(txt, sit):
    linha = '-=' * int((len(txt) + 10) / 2)
    espaço = ' ' * int((len(linha) - len(txt)) / 2)
    print(f'{cor(11)}{fundo(sit)}{linha}-')
    print(f'{espaço}{txt}')
    print(f'{linha}-{cor(0)}')


def ajuda():
    from time import sleep
    while True:
        f = str(input('Fução ou Biblioteca > ')).lower()
        if f in 'fim':
            corpo('ATÉ LOGO', 3)
            break
        corpo(f'Acessando o manual do comando [{f}]', 2)
        sleep(.5)
        print(f'{cor(1)}{fundo(0)}{str(help(f))}{cor(0)}')


cabeca('SISTEMA DE AJUDA PyHELP')
ajuda()
