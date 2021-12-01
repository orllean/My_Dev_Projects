print('{:=^60}'.format(' Sequência de Fibonacci '))
cnt = int(input(f'Digite o número de elementos: '))
ant = 1
num = 1
aux = 0
print(f'..{ant} ', end='')
print(f'..{num} ', end='')
while (cnt - 2) > 0:
    aux = num + ant
    ant = num
    num = aux
    print(f'..{aux} ', end='')
    cnt -= 1
