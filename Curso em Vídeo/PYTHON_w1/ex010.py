n = input('Converte Real em Dollar [US$1.00 => R$5.55]. Digite um valor(R$): ')
d = 5.55
if n.replace('.', '', 1).isnumeric():
    n = float(n)
    if n > 0:
        print(f'R$ {n:.2f} equivale a U${n / d:.2f}')
    else:
        print('Na próxima vez digite um valor maior que zero')
        exit()
else:
    print('Na próxima vez digite um número ex: 1890.87!')
