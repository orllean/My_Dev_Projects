print('{:=^60}'.format(' PROGREÇÃO ARITIMÉTRICA '))
i = int(input(f'Digite o início da PA: '))
p = int(input(f'Digite o razão da PA: '))
f = i + (10 * p)
e = 0
for c in range(i, f, p):
    e += 1
    print(f'{e}º elemento da PA {c}')
