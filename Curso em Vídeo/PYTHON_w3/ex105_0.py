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


def notas(* n, sit=False):
    """
    -> Função para analizar notas de aluno.
    n: notas separadas por virgula. Ex.: 5, 4.5, 6
    sit: Se for 'True' exibe situação do aluno. Ex.: 2, 3, sit=Ture
    return: dicionário com analize do aluno
    """
    dic = {
        'Total': len(n),
        'Maior': max(n),
        'Menor': min(n),
        'Media': (sum(n) / len(n))
    }
    if sit:
        if dic['Media'] > 6.99:
            dic['Situação'] = 'Boa'
        elif dic['Media'] > 4.99:
            dic['Situação'] = 'Regular'
        else:
            dic['Situação'] = 'Ruim'
    return dic


cabeca('CADERNO DE NOTAS')
resp = notas(3.5, 2)
print(resp)
