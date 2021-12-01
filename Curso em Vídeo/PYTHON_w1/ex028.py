######## Import #########
from time import sleep
from random import randint
######## Input / Validação #########
print('MACHINE: Sorteei um número inteiro entre 0 - 5')
try:
    u_num = int(input('MACHINE: Digite seu palpite: '))
except:
    print('MACHINE: Na próxima vez digite um número inteiro.')
    exit()
if u_num > 5:
    print('MACHINE: Na próxima vez digite um número entre 0 - 5.')
    exit()
######## Sorteio #########
num = randint(0, 5)
######## Processando #########
s = 'PROCESSANDO....'
for e in range(2):
    s = s[:len(s)-4]
    for e in range(4):
        # print(s)
        print(f'\r{s}', end='')
        s = s + '.'
        sleep(.5)
######## Output #########
print(f'\nMACHINE: {num}\
      \nHuman: {u_num}')
if u_num == num:
    print('MACHINE: Parabéns, você acertou!')
else:
    print('MACHINE: Que pena, você perdeu!')
