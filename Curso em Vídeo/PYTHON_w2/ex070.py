# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
menor_p = maior1000 = tot = 0
produto = ''
# start
print(borda)
print(f'{"  CADASTRE UMA PESSOA  ": ^40}')
print(borda)
while True:
    # loop / input / name checked
    while True:
        nome = str(input(f'{limpa}Nome do produto:{amarelo} '))
        if len(nome) > 0:
            break
        print(
            f'{limpa}Digite ao menos {negrito}{vermelho}1{limpa} caracter')
    # loop / input / price checked
    while True:
        try:
            preco = float(input(f'Preço: R${amarelo} '))
            if preco == 0:
                preco / 0
            break
        except:
            print(
                f'{limpa}Digite um {vermelho}valor{limpa} maior que {vermelho}0{limpa}')
    # nome o prodoto com menor preço
    if tot == 0:
        menor_p = preco
    if preco < menor_p:
        menor_p = preco
        produto = nome
    # total produtos
    tot += preco
    # produtos > R$1000
    if preco > 1000:
        maior1000 += 1
    # loop / input / continuum checked
    while True:
        continua = str(input(f'{limpa}Quer continuar? [S/N]:{amarelo} ')
                       ).lower().strip().split()[0][0]
        if continua in 'sn':
            break
        print(
            f'{limpa}Digite [{vermelho}S{limpa}] para Sim ou [{vermelho}N{limpa}] para Não{limpa}')
    if continua == 'n':
        break
print(borda)
print(f'{limpa}Total da compra foi: {amarelo}R${tot:.2f}')
print(f'{limpa}Total de produtos acima de R$1.000: {amarelo}{maior1000}')
print(f'{limpa}O produto mais barato foi {amarelo}{produto}{limpa} por {amarelo}R${menor_p:.2f}')
