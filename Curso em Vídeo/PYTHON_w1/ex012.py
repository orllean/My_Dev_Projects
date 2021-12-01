n = input('Digite o valor(R$): ')
if n.replace('.', '', 1).isnumeric():
    n = float(n)
    if n > 0:
        print(
            f'Parabéns! Você foi premiado com 5% de desconto. \nO produto que custava R${n:.2f} com desconto vai ficará R${n - (n * .05):.2f}')
    else:
        print('Na próxima vez digite um valor maior que zero')
        exit()
else:
    print('Na próxima vez digite um número ex: 1890.87!')
