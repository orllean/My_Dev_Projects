######## Input / Validação / Saida #########
try:
    kmh = int(input('MACHINE: Qual a sua velocidade(km/h)? '))
except:
    print('MACHINE: Na próxima vez digite um número.')
    exit()
if kmh <= 0:
    print('MACHINE: Na próxima vez digite um número maior que zero.')
elif kmh > 80:
    print(f'MACHINE: Você ultrapasou o limite de velocidade de 80Km/h.\
        \nO valor da multa é: R${(kmh - 80)*7:.2f} ')
else:
    print('MACHINE: Parabéns humano, você está dirigindo dentro do limite de velocidade.')
