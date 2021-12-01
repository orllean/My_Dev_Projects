km = input('Digite quantos km foram rodados: ')
dias = input('Digite quantos por quantos dias: ')
# valida input
if km.replace('.', '', 1).isnumeric() and dias.replace('.', '', 1).isnumeric():
    km = float(km)
    dias = float(dias)
    # valida valor
    if km > 0 and dias > 0:
        print(
            # R$ 60,00 por dia e R$ 0,15 por km
            f'O total a pagar é de R${(km * .15)+(dias * 60):.2f}')
    else:
        print('Na próxima vez digite valores maiores que zero')
        exit()
else:
    print('Na próxima vez digite um número ex: 18!')
