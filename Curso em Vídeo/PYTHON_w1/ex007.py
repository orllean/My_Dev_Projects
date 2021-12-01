n1 = input('Digite a primeira nota: ')
n2 = input('Digite a segunda nota: ')
if n1.isnumeric() and n2.isnumeric():
    n1 = float(n1)
    n2 = float(n2)
    print(
        f'A primeira nota foi: {n1:.2f} \nA segunda nota foi: {n2:.2f} \nA média é: {(n1 + n2) / 2:.2f}')
else:
    print('Na próxima vez digite um número em cada nota!')
