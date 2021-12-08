# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
s = f'{negrito}{amarelo}{"-+" * 12}-{limpa}'
fim = (f'>>> FINALIZADO <<<')
alunos = []
# start
print(borda)
print(f'{" ANALIZANDO NOTAS - LISTA COMPOSTA II ": ^40}')
print(borda)
# loop record
while True:
    # set ampty list cad
    cad = []
    # input number
    cad.append(str(input(f'{limpa}Nome:{negrito} {vermelho}')).upper())
    cad.append(float(input(f'{limpa}Nota_1:{negrito} {vermelho}')))
    cad.append(float(input(f'{limpa}Nota_2:{negrito} {vermelho}')))
    # add 1 cad to alunos
    alunos.append(cad[:])
    # test opt
    opt = str(
        input(f'{limpa}Quer continuar? [S/N]{negrito} {vermelho}').upper())
    if opt in 'Nn':
        break
print(s)
print(f'{"Nº":6}'f'{"NOME":12}'f'{"MÉDIA":6}')
print(s)
for e, i in enumerate(alunos):
    print(f'{e:<6}'f'{i[0]:12}'f'{(i[1] + i[2]) / 2:.2f}')
print(s)
while True:
    i = int(
        input(F'Mostrar notas de qual aluno? [999 para interromper]: '))
    if i > len(alunos) - 1:
        print(fim)
        break
    else:
        print(
            f'As notas de{amarelo} {alunos[i][0]}{limpa} são{amarelo} [ {alunos[i][1]} / {alunos[i][2]} ]{limpa} ')
        print(borda)
