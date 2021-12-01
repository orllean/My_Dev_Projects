from time import sleep
print('{:=^60}'.format(' CONTAGEM REGRASSIVA '))
for c in range(10, -1, -1):
    print(f'\rEm: {c}', end='')
    sleep(1)
