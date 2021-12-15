from tools import moeda

p = 100  # float(input('Digite o preço: R$'))
print(f'{moeda.dobro(p, True)} ')
print(f'{moeda.metade(p, True)} ')
print(f'{moeda.aumenta(p, 10, True)} ')
print(f'{moeda.reduz(p, 10, True)} ')
