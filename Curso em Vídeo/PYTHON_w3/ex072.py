# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
# set tupla
numExt = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze",
          "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
# loop / input / validation          
while True:
    try:
        num = int(input('Digite um número entre 0 e 20: '))
    except:
        print('Digite apenas números: ')
    if num >= 0 and num <= 20:
        break
    else:
        print('Tente novamente. Digite um número entre 0 e 20: ')
# output        
print(f'Você digitou o número {numExt[num]}')
