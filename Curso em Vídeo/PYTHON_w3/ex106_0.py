cor = (
    '\033[0;0;0m',           # 0 sem cor
    '\033[1;37;41m',      # 1 vermelho
    '\033[1;37;42m',      # 2 verde
    '\033[1;37;43m',      # 3 amarelo
    '\033[1;37;44m',      # 4 azul
    '\033[1;37;45m',      # 5 roxo
    '\033[7;30m',       # 6 branco
)


def titulo(txt, c=0):
    linha = '-=' * int((len(txt) + 10) / 2)
    espaço = ' ' * int((len(linha) - len(txt)) / 2)
    print(f'{cor[c]}{linha}-')
    print(f'{espaço}{txt}')
    print(f'{linha}-{cor[0]}')


def ajuda():
    from time import sleep
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', 2)
        f = str(input('Fução ou Biblioteca > ')).lower()
        if f in 'fim':
            titulo('ATÉ LOGO', 1)
            break
        titulo(f'Acessando o manual do comando [{f}]', 4)
        sleep(.3)
        print(cor[6], end='')
        help(f)
        print(cor[0], end='')
        sleep(1)


ajuda()
