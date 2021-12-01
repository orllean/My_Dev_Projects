num = input('Digite numero entre  9999: ')
while len(num) < 4:
    num = '0' + num
print(f'{num[3]}: unidade \
      \n{num[2]}: dezena\
      \n{num[1]}: centena\
      \n{num[0]}: milhar')
