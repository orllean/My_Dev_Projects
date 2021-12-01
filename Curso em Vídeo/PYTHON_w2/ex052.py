print('{:=^60}'.format(' É PRIMO OU NÃO É? '))
n = int(input(f'Digite um número inteiro positivo: '))
p = 0
for i in range(1, (n + 1)):
    if n % i == 0:
        p += 1
print(f'{n} é um número PRIMO') if p == 2 else print(
    f'{n} NÃO é um número PRIMO')
