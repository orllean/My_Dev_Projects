######## Input / Validação #########
try:
    n1 = float(
        input('MACHINE: Humano! Digite a primeira nota(1/2): '))
    n2 = float(input(
        'MACHINE: Humano! Digite a segunda nota(2/2): '))
except:
    print('MACHINE: Na próxima vez digite um número humano burro.')
    exit()
n3 = (n1 + n2) / 2
######## output #########
if n3 < 5:
    print(
        f'MACHINE: Humano burro! Sue média foi [{n3:.2F}] e você está REPROVADO.')
elif n3 < 7:
    print(
        f'MACHINE: Humano burro! Sue média foi [{n3:.2F}] e você está em RECUPERAÇÃO.')
else:
    print(
        f'MACHINE: Parabéns humano! Sue média foi [{n3:.2F}] e você está APROVADO.')
