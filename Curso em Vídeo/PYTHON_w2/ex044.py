######## Input / Validação #########
try:
    n1 = float(
        input('MACHINE: Humano! Digite o valor da compra(R$): '))
except:
    print('MACHINE: Na próxima vez digite um número humano burro.')
    exit()
######## Input #########
pgto = input(
    'MACHINE: Humano! Digite [1] para pagamento à vista e [2] para parcelado: ')
######## Valida pgto #########
if pgto not in ['1', '2'] or len(pgto) > 1:
    print('MACHINE: Na próxima vez digite apenas [1] ou [2] humano burro.')
    exit()
if pgto == '1':
    ######## Input #########
    desc = input(
        'MACHINE: Humano! Digite [1] para dinheiro/cheque e [2] para cartão: ')
######## Valida desc #########
    if desc not in ['1', '2'] or len(pgto) > 1:
        print('MACHINE: Na próxima vez digite apenas [1] ou [2] humano burro.')
        exit()
######## get desc #########
    desc = .1 if desc == '1' else .05
    print(
        f'MACHINE: Parabéns humano! Você ganhou um desconto de {desc * 100}%.\
        \nO produto com valor de R${n1:.2f} vai ficar por apenas R${n1 * (1 - desc):.2f}')
else:
    ######## Input #########
    juro = input(
        'MACHINE: Humano! Digite [1] para 2x e [2] para 3x ou mais no cartão: ')
######## Valida juro #########
    if juro not in ['1', '2'] or len(pgto) > 1:
        print('MACHINE: Na próxima vez digite apenas [1] ou [2] humano burro.')
        exit()
######## get juro #########
    juro = 0 if juro == '1' else 1.2
    if juro == 0:
        print(
            f'MACHINE: Humano! Você vai pagar R${n1:.2f} em 2x sem juros de R${n1 / 2:.2f}')
    else:
        print(
            f'MACHINE: Humano! Haverá um acressimo de {(juro - 1) * 100:.0f}% sobre o valor de R${n1:.2f}.\
                \nVocê pode dividir R${n1*juro:.2f} em 3 ou mais vezes iguais')
