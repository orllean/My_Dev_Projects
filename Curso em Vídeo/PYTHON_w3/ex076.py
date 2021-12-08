# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
# set tupla
prod = ('caderno', 5, 'caneta', 3.5, 'monitor', 600,
        'papel', 35.5, 'copo', 1.5, 'cadeira', 103.5,)
# start
print(borda)
print(f'{" LISTAGEM DE PREÇOS - TUPLA ": ^40}')
print(borda)
# task listar os preços de forma tabular
for i in range(len(prod)):
    if i % 2 == 0:
        print(f'{limpa}{prod[i]:.<30}R${amarelo}{prod[i + 1]:9.2f} ')
print(borda)
