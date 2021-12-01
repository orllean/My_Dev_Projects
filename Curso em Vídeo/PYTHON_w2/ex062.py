print('{:=^60}'.format(' PROGREÇÃO ARITIMÉTRICA '))
i = int(input(f'Digite o início da PA: '))
p = int(input(f'Digite o razão da PA: '))
cnt = 1
num = 10
game = 1
while game:
    print(f'{i} ', end='')
    while cnt < num:
        i = i + p
        cnt += 1
        print(f'{i} ', end='')
    opt = int(input(
        '\nDeseja mostra mais termos? Digite um valor maoir que 10. Para sair digite [0]: '))
    if opt < 11:
        game = 0
    else:
        cnt = 1
        num = opt
print('GAME OVER')
