# set colors
limpa = '\033[0;0;0m'
fx = {
    'none': '\033[0m',
    'bold': '\033[1m',
    'italic': '\033[4m',
    'inverse': '\033[7m'
}
txt_cores = {'branco': '\033[30m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'amarelo': '\033[33m',
             'azul': '\033[34m',
             'roxo': '\033[35m',
             'cian': '\033[36m',
             'cinza': '\033[37m'
             }
bg_cores = {'branco': '\033[40m',
            'vermelho': '\033[41m',
            'verde': '\033[42m',
            'amarelo': '\033[43m',
            'azul': '\033[44m',
            'roxo': '\033[45m',
            'cian': '\033[46m',
            'cinza': '\033[47m'
            }
# initialize variables
negrito = fx["bold"]
vermelho = txt_cores["vermelho"]
amarelo = txt_cores["amarelo"]
cinza = txt_cores["cinza"]

borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
# loop while
while True:
    print(
        f'{negrito}{vermelho}[{limpa}PARA SAIR... digite um valor menor que 1{negrito}{vermelho}]{limpa}')
    num = int(
        input(F'Quer ver a tabuada de qual valor? :{negrito}{amarelo}'))
    print(borda)
    if num < 1:
        print(f'{negrito}{amarelo}Programa encerrado!{limpa}')
        break
    for i in range(1, 11):
        print(
            f'{cinza}{num} {vermelho}x {cinza}{i:2} {vermelho}= {amarelo}{(num * i):2}{limpa}')
    print(borda)
