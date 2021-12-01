print('{:=^60}'.format(' SUPER PROGREÇÃO ARITIMÉTRICA '))
i = int(input(f'Digite o início da PA: '))
p = int(input(f'Digite o razão da PA: '))
cnt = 1
num = 10
game = 1
e = 0
while game:
    e += num
    print(f'{i} ', end='')
    while cnt < num:
        i = i + p
        cnt += 1
        print(f'{i} ', end='')
    opt = int(input('\nDeseja mostra mais termos?\
     \nQauntos termos você quer digitar a mais? \
     \nPara sair digite [0]: '))
    if opt == 0:
        game = 0
        print(f'Foram exibidos {e} termos')
    else:
        cnt = 1
        num = opt
        i += p
print('GAME OVER')
