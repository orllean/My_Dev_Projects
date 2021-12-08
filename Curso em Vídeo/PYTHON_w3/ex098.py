from time import sleep


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


def valida(p):
    p = 1 if p == 0 else p
    p = (p * -1) if p < 0 else p
    return p


def crescente(i, f, p):
    f += 1
    for i in range(i, f, p):
        print(f'{i} ', end='', flush=True)
        sleep(.7)


def decrescente(i, f, p):
    f -= 1
    for i in range(i, f, (p * -1)):
        print(f'{i} ', end='', flush=True)
        sleep(.7)


def msg(i, f, p):
    print(f'Iniciando contagem de {i} até {f} de {p} em {p}:')


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    
    """
    linha()
    p = valida(p)
    msg(i, f, p)
    if i < f:
        crescente(i, f, p)
    else:
        decrescente(i, f, p)
    print(f'{cor(11)}{cor(1)}FIM!{cor(0)}')


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
