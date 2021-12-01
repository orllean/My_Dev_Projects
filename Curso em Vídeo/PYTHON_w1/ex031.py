######## Input / Validação / Saida #########
try:
    km = int(input('MACHINE: Digite quantos Km até o destino: '))
except:
    print('MACHINE: Na próxima vez digite um número.')
    exit()
if km <= 0:
    print('MACHINE: Na próxima vez digite um número maior que zero.')
elif km <= 200:
    print(f'MACHINE: O valor da passagem é de R${km * .5:.2f}')
else:
    print(f'MACHINE: O valor da passagem é de R${km * .45:.2f}')
