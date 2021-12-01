print('{:=^60}'.format(' É PRIMO OU NÃO É ? '))
n = int(input(f'Digite um número inteiro positivo: '))
p = 0
for i in range(1, (n + 1)):
    if n % i == 0:
        p += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print(f'\n{n} é um número PRIMO') if p == 2 else print(
    f'\n\033[31m{n} NÃO é um número PRIMO')
