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


def voto(ano):
    from datetime import date
    i = date.today().year - ano
    if i < 16:
        return f'Com {i} anos:{cor(11)}{cor(1)} NÃO VOTA!'
    elif i > 64 or 16 <= i < 18:
        return f'Com {i} anos:{cor(11)}{cor(1)} VOTO OPCIONAL!'
    else:
        return f'Com {i} anos:{cor(11)}{cor(1)} VOTO OBRIGATÓRIO!'


ano = int(input('Em que ano você nasceu? '))
linha()
print(voto(ano))
