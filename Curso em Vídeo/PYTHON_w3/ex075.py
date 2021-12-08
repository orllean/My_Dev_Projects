# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
num_lista = ''
# start
print(borda)
print(f'{" ANALIZANDO NÚMEROS - TUPLA ": ^40}')
print(borda)
# loop / input
for i in range(4):
    s = str(input(f'{limpa}Digite um número: {amarelo}'))
    num_lista = num_lista + ' ' +  s
# set tuple
t = tuple(int(i)for i  in num_lista.strip().split(' '))
# task : n vezes num 9? index primeiro 3? list num pares
# output
cont_9 = t.count(9)
print(f'{limpa}Você digitou os valores: {amarelo}{t}')
print(f'{limpa}Número de vezes que o 9 apareceu: {amarelo}{cont_9}')
num_3 = t.count(3)
if num_3 == 0:
    print(f'{limpa}O número 3 não apareceu!')
else:
    print(f'{limpa}O index do número 3 é: {amarelo}{t.index(3)}')
print(f'{limpa}Os Números pares digitados foram: ', end='')
for i in t:
    if int(i) % 2 == 0:
        print(f'{amarelo}{i} ', end='')
