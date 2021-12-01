print('{:=^60}'.format(' SOMA ENTRE NÚMEROS IMPARES E MULTIPLOS DE 3 ENTRE 1 - 500 '))
s = 0
for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            s += c
print(f'# {s}')
