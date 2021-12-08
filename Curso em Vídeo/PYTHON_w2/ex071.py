# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
c50 = c20 = c10 = 0
# start
print(borda)
print(f'{"  BANCO CEV  ": ^40}')
print(borda)
num = int(input(f'Digite o valor que deseja sacar: {amarelo}R$'))
# task: fatorar o valor entre 50 / 20 / 10 / 1
c50 = num // 50
if c50 > 0:
    print(f'{limpa}Total de {amarelo}{c50:2}{limpa} cédullas de R$50')
num = num % 50
c20 = num // 20
if c20 > 0:
    print(f'Total de {amarelo}{c20:2}{limpa} cédullas de R$20')
num = num % 20
c10 = num // 10
if c10 > 0:
    print(f'Total de {amarelo}{c10:2}{limpa} cédullas de R$10')
num = num % 10
if num > 0:
    print(f'Total de {amarelo}{num:2}{limpa} cédullas de R$1')
print(borda)
