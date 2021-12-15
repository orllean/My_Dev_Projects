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
    linha = '-=' * int((len(txt) + 18) / 2)
    espaço = ' ' * int((len(linha) - len(txt)) / 2)
    print(f'{cor[c]}{linha}-')
    print(f'{espaço}{txt}')
    print(f'{linha}-{cor[0]}')


def resumo(p, a=0, r=0):
    titulo('RESUMO DO VALOR')
    print(f'Preço analisado:\t{moeda(p):>9}')
    print(f'Dobro do preço:\t\t{dobro(p, True):>9}')
    print(f'Metade do preço:\t{metade(p, True):>9}')
    print(f'{a}% de aumento:\t\t{aumenta(p, a, f=True):>9}')
    print(f'{r}% de redução:\t\t{reduz(p, r, f=True):>9}')


def metade(p=0, f=False):
    return moeda(p / 2) if f else (p / 2)


def dobro(p=0, f=False):
    return moeda(p * 2) if f else (p * 2)


def aumenta(p=0, a=0, f=False):
    p = (p * (a/100 + 1))
    return moeda(p) if f else p


def reduz(p=0, r=0, f=False):
    p = (p * (1 - r/100))
    return moeda(p) if f else p


def moeda(m=0, n='R$'):
    m = (f'{n}{m:>6.2f}').replace('.', ',')
    return m
