print('{:=^60}'.format(' PROGREÇÃO ARITIMÉTRICA '))
i = int(input(f'Digite o início da PA: '))
p = int(input(f'Digite o razão da PA: '))
cnt = 1
print(f'{i} ', end='')
while cnt < 10:
    i = i + p
    cnt += 1
    print(f'{i} ', end='')
