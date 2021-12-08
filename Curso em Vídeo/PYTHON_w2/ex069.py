# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
maior18 = tot_m = tot_cad = tot_w = 0
# start
print(borda)
print(f'{"  CADASTRE UMA PESSOA  ": ^40}')
print(borda)
while True:
    # loop / input / checked age
    while True:
        try:
            idade = int(input(f'Idade:{amarelo} '))
            if idade == 0:
                idade / 0
            break
        except:
            print(
                f'{limpa}Digite um {vermelho}inteiro{limpa} maior que {vermelho}0{limpa}')
    # loop / input / sex checked
    while True:
        sexo = str(input(f'{limpa}Sexo [M/F]:{amarelo} ')
                   ).lower().strip().split()[0][0]
        if sexo in 'mf':
            break
        print(
            f'{limpa}Digite [{vermelho}M{limpa}] para Masculino ou [{vermelho}F{limpa}] para Feminino{limpa}')
    # majority
    if idade > 18:
        maior18 += 1
    # total man
    if sexo == 'm':
        tot_m += 1
    # total of women less than 20 years old
    if sexo == 'f' and idade < 20:
        tot_w += 1
    # loop / input / continues checked
    tot_cad += 1
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
print(f'{limpa}Total de cadastros: {amarelo}{tot_cad}')
print(f'{limpa}Total de pessoas com mais de 18 anos: {amarelo}{maior18}')
print(f'{limpa}Total de homens cadastrados: {amarelo}{tot_m}')
print(f'{limpa}Total de mulheres com menos de 20 anos: {amarelo}{tot_w}')
