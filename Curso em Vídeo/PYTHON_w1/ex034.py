######## Input / Validação / Saida #########
try:
    sal = float(input('MACHINE: Humano! Digite o valor de seu sário: '))
except:
    print('MACHINE: Na próxima vez digite um número.')
    exit()
if sal <= 0:
    print('MACHINE: Na próxima vez digite um número maior que zero.')
elif sal <= 1250:
    print(f'MACHINE: Prabéns humano você recebeu um almento.\
        \nSeu novo salário é de R${sal * 1.15:.2f}')
else:
    print(f'MACHINE: Prabéns humano você recebeu um almento.\
        \nSeu novo salário é de R${sal * 1.1:.2f}')
