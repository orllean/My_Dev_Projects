from random import randint
# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
num_c = randint(0, 10)
parImpar = ''
jogo = 0
# start
print(borda)
print('PAR OU ÍMPAR')
print(borda)
# loop game
while True:
    num = int(
        input(F'Digite um valor? :{amarelo}'))
    # loop option
    while True:
        opt = str(
            input(f'{limpa}PAR ou ÍMPAR? [P/I]{amarelo} ')).lower().strip().split()[0][0].replace('í', 'i')
        if opt in 'pi':
            break
    # test choice
    parImpar = 'PAR' if (num + num_c) % 2 == 0 else 'ÍMPAR'
    # feedback
    print(
        f'{limpa}Você escolheu {negrito}{cinza}{num}{limpa} e o computador {negrito}{cinza}{num_c}{limpa}. Total de {num + num_c} deu {negrito}{vermelho}{parImpar} ')
    if (opt == 'p' and parImpar == 'PAR') or (opt == 'i' and parImpar == 'ÍMPAR'):
        print(f'{negrito}{amarelo}Você venceu! \n{limpa}Vamos jogar novamente...')
        jogo += 1
    else:
        print(f'Você perdeu!')
        break
print(borda)
print(f'Você ganhou {jogo} vezes.')
