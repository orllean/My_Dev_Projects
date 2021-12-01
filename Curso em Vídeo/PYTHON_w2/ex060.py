x = int(input('Digite um número inteiro positivo: '))
f = x
cnt = x - 1
while cnt > 0:
    f = f * cnt
    cnt -= 1
print(f'O fatorial de {x} é {f}')
