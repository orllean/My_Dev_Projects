def area(l, c):
    print(f'A área de um terreno de {l:.1f} X {c:.1f} é de: {(l * c):.1f} m² ')


print('CONTROLE DE TERRENOS')
print('-' * 10)
L = float(input('LARGURA [m]: '))
C = float(input('COMPRIMENTO [m]: '))
area(L, C)
