from tools import moeda

p = 100  # float(input('Digite o preço: R$'))
print(f'{moeda.moeda(p)}')
print(f'{moeda.moeda(moeda.dobro(p))} ')
print(f'{moeda.moeda(moeda.metade(p))} ')
print(f'{moeda.moeda(moeda.aumenta(p, 10))} ')
print(f'{moeda.moeda(moeda.reduz(p, 10))} ')
