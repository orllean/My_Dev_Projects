def dinheiro(msg):
    while True:
        d = str(input(msg)).strip().replace(',', '.')
        alerta = f'\033[1;31;47m>>> ERRO: "{d}" é um preço inválido!\033[0;0;0m'
        if valida(d):
            return float(d)
        else:
            print(alerta)


def valida(d):
    try:
        float(d)
        return True
    except:
        pass
    return False