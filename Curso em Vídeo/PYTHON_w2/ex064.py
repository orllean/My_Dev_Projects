num = tot = 0
cnt = -1
while num != 999:
    cnt += 1
    tot += num
    num = int(input('Digite um número [para sair digite: 999]: '))
print(f'Você digitou {cnt} números e a soma deles é {tot}')
