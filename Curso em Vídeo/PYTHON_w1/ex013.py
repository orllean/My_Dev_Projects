n = input('Digite o valor do salário(R$): ')
if n.replace('.', '', 1).isnumeric():
    n = float(n)
    if n > 0:
        print(
            f'O salário R${n:.2f} com aumento de 15% ficará R${n + (n * .15):.2f}')
    else:
        print('Na próxima vez digite um valor maior que zero')
        exit()
else:
    print('Na próxima vez digite um número ex: 1890.87!')
