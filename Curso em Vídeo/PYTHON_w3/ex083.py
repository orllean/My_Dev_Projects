# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
l = []
# start
print(borda)
print(f'{" ANALIZANDO EXPRESSÕES VI - LISTA ": ^40}')
print(f'{" valida os parênteses de uma expressão ": ^40}')
print(borda)
# user input
exp = str(input(f'Digite a expressão:{amarelo} '))
# loop / set list
for i in exp:
    if i in '()':
        l.append(i)
# check if input is true
cont = l.count(')')
err = False
while True:
    if l.count(')') != l.count('(') or l[0] == ')' or l[len(l) - 1] == '(':
        print(f'Sua expressão está{negrito}{vermelho} ERRADA{limpa}')
        err = True
        break
    for i in range(cont):
        x = l.index(')')
        if l[x - 1] == '(':
            l.pop(x)
            l.pop(x - 1)
            cont -= 1
        else:
            print(f'Sua expressão está{negrito}{vermelho} ERRADA{limpa}')
            err = True
            break
    if cont == 0 or err == True:
        break
# output if no erro
if err == False:
    print(f'Sua expressão está{negrito}{amarelo} CORRETA{limpa}')
