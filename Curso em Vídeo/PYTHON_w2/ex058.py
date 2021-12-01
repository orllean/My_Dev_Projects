from random import randint
cnt = 0
game = True
num = randint(0, 10)
print('MACHINE: Sorteei um número inteiro entre 0 - 10')
while game:
    cnt += 1
    u_num = int(input('MACHINE: Digite seu palpite: '))
    if u_num == num:
        print(
            f'MACHINE: Parabéns, você acertou o número {num} em {cnt} tentativas')
        game = False
    else:
        print('MACHINE: Muito alto! tente um número menor') if u_num > num else print(
            'MACHINE: Muito baixo! tente um número maior')
