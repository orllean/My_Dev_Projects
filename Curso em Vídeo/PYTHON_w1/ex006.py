n = input('Digite um número inteiro maior que zero: ')
if n.isnumeric():
    n = int(n)
    if n > 0:
        print(
            f'O número digitado foi: {n} \nO seu dobro é: {n * 2} \nO seu triplo é: {n * 3} \nA ariz quadrada é: {n ** (1/2):.2f}')
    else:
        print('Na próxima vez digite um número maior que zero')
        exit()
else:
    print('Na próxima vez digite um número inteiro')
