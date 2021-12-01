n = input('Converte em multiplos e sub-multiplos. Entre com o valor em metros: ')
if n.replace('.', '', 1).isnumeric():
    n = float(n)
    if n > 0:
        print(
            f'{n} metros equivale a:\
             \n{n / 1000:.0f}km\
             \n{n / 100:.0f}hm\
             \n{n / 10:.0f}dam\
             \n{n * 10:.0f}dm\
             \n{n * 100:.0f}cm\
             \n{n * 1000:.0f}mm')
    else:
        print('Na próxima vez digite um valor maior que zero')
        exit()
else:
    print('Na próxima vez digite um número.')
