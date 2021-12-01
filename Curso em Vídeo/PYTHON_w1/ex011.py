n1 = input('Digite a altura da parede (em metros): ')
n2 = input('Digite a largura da parede (em metros): ')
if n1.replace('.', '', 1).isnumeric() and n2.replace('.', '', 1).isnumeric():
    n1 = float(n1)
    n2 = float(n2)
    print(
        f'A aréa da parede é de: {(n1 * n2):.1f} m² \nÉ nescessário: {(n1 * n2) / 2:.1f} litro(s) de tinta para pintar esta parede.')
else:
    print('Na próxima vez digite um número!')
