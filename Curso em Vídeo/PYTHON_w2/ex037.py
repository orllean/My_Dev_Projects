######## Input / Validação #########
try:
    num = int(
        input('MACHINE: Humano! Digite um número inteiro positico maior que zero: '))
    opt = int(input(
        'MACHINE: Humano! Digite [1] para binario [2] para octal ou [3] para hexadecimal: '))
except:
    print('MACHINE: Na próxima vez digite um humano burro.')
    exit()
######## Validação inteiro positivo > 0 #########
if num <= 0 or opt <= 0:
    print('MACHINE: Na próxima vez digite um número maior que zero humano burro.')
    exit()
######## Validação conversão #########
if opt == 1:
    print(f'MACHINE: O número {num} em binário é: {bin(num)}')
elif opt == 2:
    print(f'MACHINE: O número {num} em octa é: {oct(num)}')
elif opt == 3:
    print(f'MACHINE: O número {num} em hexadecimal é: {hex(num)}')
else:
    print(f'MACHINE: Humano burro! {opt} não é uma opção válida')
