from math import factorial
x = int(input('Digite um número inteiro positivo: '))
f = factorial(x)
cnt = x
print(f'Calculando... {x}! =', end='')
while cnt > 0:
    print(f' {cnt} ', end='')
    print('X', end='') if cnt > 1 else print('= ', end='')
    cnt -= 1
print(f'{f}')