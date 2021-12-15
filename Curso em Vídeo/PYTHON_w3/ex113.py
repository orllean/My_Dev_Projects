def leiaInt(i):
    try:
        int(i)
    except:
        print(f'\033[1;31;47m ERRO! Digite um valor válido. \033[0;0;0m')
    else:
        return True


def leiaFloat(f):
    try:
        float(f)
    except:
        print(f'\033[1;31;47m ERRO! Digite um valor válido.\033[0;0;0m')
    else:
        return True


def principal():
    while True:
        int = str(input('Digite um valor INTEIRO: '))
        if leiaInt(int):
            break
    while True:
        real = str(input('Digite um valor REAL: '))
        if leiaFloat(real):
            break
    print(f'O valor inteiro foi {int} e o valor real foi {real} ')


principal()
