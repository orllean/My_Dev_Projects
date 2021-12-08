from datetime import date
# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
separador = f'{negrito}{amarelo}{"-+" * 12}-{limpa}'
fim = (f'{negrito}{vermelho}{">>>" * 5} FINALIZADO {"<<<" * 5}{limpa}')
# start
print(borda)
print(f'{" ANALIZANDO CADASTRO - DICIONÁRIO ": ^40}')
print(borda)
pessoa = dict()
# get data
pessoa['Nome'] = str(input('Nome: ')).capitalize()
ano = int(input('Nasc [aaaa]: '))
idade = (date.today().year) - ano
pessoa['Idade'] = idade
ctps = int(input('Nº Carteira de trabalho [0 se não se aplica]: '))
if ctps > 0:
    pessoa['CTPS'] = ctps
    pessoa['Admissão'] = int(input('Ano de admissão [aaaa]: '))
    pessoa['Aposentadoria'] = pessoa['Admissão'] + 35
    pessoa['Salário'] = float(input('Salário: R$'))
print(separador)
# output
for k, i in pessoa.items():
    if k == 'Salário':
        print(f'{k:.<20}{i:.2f}')
    else:
        print(f'{k:.<20}{i}')
print(fim)
