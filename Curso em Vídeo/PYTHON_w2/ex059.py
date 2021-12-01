from time import sleep
game = True
x = int(input('Digite um número[1:2]: '))
y = int(input('Digite outro número[2:2]: '))
while game:
    print('''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
    ''')
    opt = input('Digite sua opção: ')
    sleep(1)
    if opt not in '1234':
        print('GAME OVER')
        exit()
    if opt == '4':
        x = int(input('Digite um número[1:2]: '))
        y = int(input('Digite outro número[2:2]: '))
        game = False
    if opt == '3':
        if x == y:
            print(f'{x} é igual a {y}!\n')
        elif x > y:
            print(f'{x} é maior que {y}!\n')
        else:
            print(f'{x} é menor que {y}!\n')
    if opt == '2':
        print(f'O produto de {x} por {y} é igual a {x * y}!\n')
    if opt == '1':
        print(f'A soma de {x} e {y} é igual a {x + y}!\n')
