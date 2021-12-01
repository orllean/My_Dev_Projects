# importa biblioteca
from math import trunc
num = input('Digite um número decimal: ')
num = num.replace(',', '.', 1)
# valida input
if num.replace('.', '', 1).isnumeric():
    num = float(num)
    # valida valor
    if num > 0:
        print(
            f'A parte inteira do número digitado é: {trunc(num)}')
    else:
        print('Na próxima vez digite valores maiores que zero')
        exit()
else:
    print('Na próxima vez digite um número ex: 18!')
