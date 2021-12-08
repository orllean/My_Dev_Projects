from time import sleep
from random import randint


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


def soma(l):
    s = 0
    for i in l:
        if i % 2 == 0:
            s += i
    print(f'A soma dos valores pares de {l}: {s}')


def sorteio(l):
    linha()
    print(f'Sorteando 5 valores da lista: ', end='')
    n = 0
    for i in range(5):
        n = randint(1, 9)
        l.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(.7)
    print(f'{cor(11)}{cor(1)}FIM{cor(0)}')


números = list()
sorteio(números)
soma(números)
