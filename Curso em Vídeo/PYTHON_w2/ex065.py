cont = True
cnt = tot = menor = maior = 0
while cont:
    num = int(input('Digite um número: '))
    cnt += 1
    tot += num
    if cnt == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont = True if input('Deseja continuar? [S/N]').lower() == 's' else False
print(
    f'Você digitou {cnt} números e a média foi {(tot/cnt)} \nO maior valor foi {maior} e o menor valor foi {menor}')
