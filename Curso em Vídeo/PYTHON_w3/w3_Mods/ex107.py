from tools import moeda

p = 100  # float(input('Digite o preço: R$'))
print(f'{moeda.dobro(p)} ')
print(f'{moeda.metade(p)} ')
print(f'{moeda.aumenta(p, 10)} ')
print(f'{moeda.reduz(p, 10)} ')
