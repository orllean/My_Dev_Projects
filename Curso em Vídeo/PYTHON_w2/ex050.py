print('{:=^60}'.format(' SOMA APENA PARES '))
s = 0
for c in range(6):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos números pares é {s}')
