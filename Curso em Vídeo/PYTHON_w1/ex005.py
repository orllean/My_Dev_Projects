n = input('Digite um número inteiro maior que zero: ')
if n.isnumeric():
    n = int(n)
    if n > 0:
        print(
            f'O número digitado foi: {n} \nO seu antecessor é: {n - 1} \nO seu posterior é: {n + 1}')
    else:
        print('Na próxima vez digite um número maior que zero')
        exit()
else:
    print('Na próxima vez digite um número inteiro')
