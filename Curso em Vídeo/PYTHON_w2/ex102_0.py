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


def fatorial(num=0, show=False):
    """
    -> Calcula o Fatorial de um número
    num: Número a ser calculado
    show: (opcional) Mostra ou não o calculo na tela.
    return: O valor do Fatorial do número.
    """
    num = 1 if num == 0 else num
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


cabeca('CALCULANDO FATORIAL')
n = int(input('Digite um número: '))
print(fatorial(n, True))
