from math import hypot

n_co = input('Digite o valor do cateto oposto: ')
n_ca = input('Digite o valor do cateto adjacente: ')

# valida input
if n_co.replace('.', '', 1).isnumeric() and n_ca.replace('.', '', 1).isnumeric():
    n_co = float(n_co)
    n_ca = float(n_ca)
    # valida valor
    if n_co > 0 and n_ca > 0:
        print(
            f'O valor da hipotenusa é: {hypot(n_co, n_ca):.2f}')
    else:
        print('Na próxima vez digite valores maiores que zero')
        exit()
else:
    print('Na próxima vez digite um número ex: 18!')
