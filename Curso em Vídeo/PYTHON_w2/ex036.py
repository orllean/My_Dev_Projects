######## Input / Validação / Saida #########
try:
    n1 = float(
        input('MACHINE: Humano! Digite primeiro o valor de seu salário(1-3): '))
    n2 = float(
        input('MACHINE: Humano! Digite agora o valor da casa(2-3): '))
    n3 = float(
        input('MACHINE: Humano! Digite finalmente em quantos meses deseja pagar o emprestimo(3-3): '))
except:
    print('MACHINE: Na próxima vez digite apenas números.')
    exit()
prst = n2 / n3
######### Valida emprestimo / Output #########
if prst <= (n1 * .3):
    print(
        f'MACHINE: Parabéns humano! seu emprestimo foi aprovado. O valor da prestação é R${prst:0.2f}.')
else:
    print(f'MACHINE: Humano! seu emprestimo foi recusado.')
