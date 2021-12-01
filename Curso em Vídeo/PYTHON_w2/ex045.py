from random import randint
from time import sleep
print('{:=^60}'.format(' PEDRA X PAPEL X TESOURA '))
print('''MACHINE: O que vai ser humano?
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA
''')
######## h_input #########
h = str(input('JOGADA HUMANO: '))
######## valida h_input #########
if (h) not in ['0', '1', '2']:
    print('MACHINE: Humano burro! Na próxima vez jogue [ 1 ] [ 2 ] ou [ 3 ]!')
    exit()
else:
    ppt = ['PEDRA', 'PAPEL', 'TESOURA']
    ######## m_input #########
    m = randint(0, 2)
    h = int(h)
    ######## let's play #########
    sleep(.1)
    print('JO')
    sleep(.3)
    print('KEN')
    sleep(.6)
    print('PO!!!')
    sleep(.8)
    ######## caso empate #########
    if h == m:
        print(('=-' * 30) + '=')
        print(f'HUMANO: {ppt[int(h)]}\
            \nMACHINE: {ppt[int(m)]}\
            \nIsso foi um empate!')
######## 0 > 2 - 1 > 0 - 2 > 1 ########
    ######## caso vitoria #########
    elif (h == 0 and m == 2) or\
        (h == 1 and m == 0) or\
            (h == 2 and m == 1):
        print(('=-' * 30) + '=')
        print(f'HUMANO: {ppt[h]}\
            \nMACHINE: {ppt[m]}\
            \nHumano venceu!')
    ######## caso derrota #########
    else:
        print(('=-' * 30) + '=')
        print(f'HUMANO: {ppt[h]}\
            \nMACHINE: {ppt[m]}\
            \nMACHINE WIN!')
