######## Input / Validação / Saida #########
try:
    ano = int(input('MACHINE: Digite um ano e eu lhe digo se ele é bissesto: '))
except:
    print('MACHINE: Na próxima vez digite um número.')
    exit()
if ano <= 0:
    print('MACHINE: Na próxima vez digite um número maior que zero.')
elif ((ano % 4 == 0) or (ano % 400 == 0)) and (ano % 100 != 0):
    print(f'MACHINE: O {ano} é bissesto.')
else:
    print(f'MACHINE: O {ano} não é bissesto.')
