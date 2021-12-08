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


def maior(*num):
    linha()
    print(f'Analizando os valores passados...')
    if len(num) < 1:
        print(f'Foram informados 0 ao todo.\nO maior valor informado foi: 0')
        exit()
    else:
        for i in sorted(num):
            print(f'{i}', end=' ', flush=True)
            sleep(.7)
    print(
        f'Foram informados {len(num)} ao todo.\nO maior valor informado foi: {max(num)}')


maior(randint(1, 9),
      randint(1, 9),
      randint(1, 9),
      randint(1, 9),
      randint(1, 9))
maior(randint(1, 9),
      randint(1, 9),
      randint(1, 9))
maior(randint(1, 9),
      randint(1, 9))
maior(randint(1, 9))
maior()
