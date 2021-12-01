s = '#'*10
print(s, 'TABUADA DE MELTIPLICAÇÃO v.2.0', s)
print('-'*46)

n = [r for r in range(1, 11)]
num = int(input('Digite um número: '))
print()

for r in n:
    # print(r, 'x', '=', r*num)
    print(f'{num} x {r:2} = {r * num}')

print('-'*46)
