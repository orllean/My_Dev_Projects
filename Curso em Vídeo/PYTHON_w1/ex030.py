######## Input / Validação / Saida #########
try:
    num = int(input('MACHINE: Digite um número inteiro positico: '))
except:
    print('MACHINE: Na próxima vez digite um número.')
    exit()
if num <= 0:
    print('MACHINE: Na próxima vez digite um número maior que zero.')
elif num % 2 == 0:
    print(f'MACHINE: O número {num} é par')
else:
    print(f'MACHINE: O número {num} é impar')
