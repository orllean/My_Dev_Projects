######## Input / Validação / Saida #########
try:
    n1 = int(input('MACHINE: Digite um número(1-3): '))
    n2 = int(input('MACHINE: Digite outro número(2-3): '))
    n3 = int(input('MACHINE: Digite um outro número(3-3): '))
except:
    print('MACHINE: Na próxima vez digite apenas número.')
    exit()
print(f'MACHINE: O maior valor número digitado foi: {max(n1, n2, n3)}.')
print(f'MACHINE: O menor valor número digitado foi: {min(n1, n2, n3)}.')
