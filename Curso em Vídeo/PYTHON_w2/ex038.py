######## Input / Validação #########
try:
    n1 = int(
        input('MACHINE: Humano! Digite um número(1/2): '))
    n2 = int(input(
        'MACHINE: Humano! Digite outro um número(2/2): '))
except:
    print('MACHINE: Na próxima vez digite um número humano burro.')
    exit()
######## Validação / output #########
if n1 > n2:
    print(f'MACHINE: O primeiro valor [{n1}] é o maior.')
elif n2 > n1:
    print(f'MACHINE: O segundo valor [{n2}] é o maior.')
else:
    print(f'MACHINE: Os valores [{n2}] são iguais.')
