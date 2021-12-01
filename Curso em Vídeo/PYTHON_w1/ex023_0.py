num = int(input('Digite numero entre  9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'{u} unidade\
\n{d} dezena\
\n{c} centena\
\n{m} milhar')
