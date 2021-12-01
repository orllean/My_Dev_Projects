######## Input / Validação / Saida #########
try:
    n1 = int(
        input('MACHINE: Humano! Digite o valor do comprimento de uma reta(1-3): '))
    n2 = int(
        input('MACHINE: Humano! Digite o valor do comprimento de outra reta(2-3): '))
    n3 = int(
        input('MACHINE: Humano! Digite o valor do comprimento da última reta(3-3): '))
except:
    print('MACHINE: Na próxima vez digite apenas números.')
    exit()
######### Valida triangulo #########
t = True if ((n1+n2) > n3) and ((n1+n3) > n2) and ((n3+n2) > n1) else False
######### Output #########
if t:
    print(
        f'MACHINE: Humano! com as retas {n1, n2, n3} você FORMA UM TRIÂNGULO.')
else:
    print(f'MACHINE: Humano! as retas {n1, n2, n3} NÃO FORMAM UM TRIÂNGULO.')
