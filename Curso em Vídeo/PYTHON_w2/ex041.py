from datetime import date
######## Input / Validação #########
try:
    n1 = int(
        input('MACHINE: Humano! Digite o ano de seu nascimento(aaaa): '))
except:
    print('MACHINE: Na próxima vez digite um número humano burro.')
    exit()
if len(str(n1)) != 4:
    print('MACHINE: Na próxima vez digite o ano com 4 dígitos(aaaa) humano burro.')
    exit()
######## get age #########
n3 = date.today().year
n2 = n3 - n1
######## Validação / output #########
if n2 < 10:
    print(
        f'MACHINE: Você é um humano de {n2} anos e sua categoria é MIRIM.')
elif n2 < 15:
    print(
        f'MACHINE: Você é um humano de {n2} anos e sua categoria é INFANTIL.')
elif n2 < 20:
    print(
        f'MACHINE: Você é um humano de {n2} anos e sua categoria é JUNIOR.')
elif n2 < 21:
    print(
        f'MACHINE: Você é um humano de {n2} anos e sua categoria é SÊNIOR.')
else:
    print(
        f'MACHINE: Você é um humano de {n2} anos e sua categoria é MASTER.')
