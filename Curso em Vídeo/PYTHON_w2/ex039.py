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
if n2 < 18:
    print(
        f'MACHINE: Você é um humano menor de 18 anos de idade e você deve se alistar daqui a {18 - n2} anos.')
elif n2 > 18:
    print(
        f'MACHINE: Você é um humano maior de 18 anos de idade e você deveria ter se alistado há {n2 - 18} anos.')
else:
    print(f'MACHINE: Você é um humano com 18 anos. Está na hora de se alistar.')
