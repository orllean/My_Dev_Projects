num = int(input('Digite numero entre  9999: '))
mi = (num // 1000) * 1000
ce = ((num - mi) // 100) * 100
dz = ((num - (mi + ce)) // 10) * 10
print(f'{num - (mi + ce + dz)} unidade\
\n{(num - (mi + ce)) // 10} dezena\
\n{(num - mi) // 100} centena\
\n{num // 1000} milhar')
