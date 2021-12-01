print('{:=^60}'.format(' Sequência de Fibonacci '))
cnt = int(input('Digite o número de elementos: \033[1;31m'))
ant = 1
num = 1
aux = 0
limp = '\033[0;0;0m'
cor1 = '\033[0;33m'
cor2 = '\033[1;31m'
print(f'{limp}{cor2}..{cor1}{ant}', end='')
print(f'{cor2}..{cor1}{num}', end='')
while cnt - 2 > 0:
    aux = num + ant
    ant = num
    num = aux
    print(f'{cor2}..{cor1}{aux}{limp} ', end='')
    cnt -= 1
