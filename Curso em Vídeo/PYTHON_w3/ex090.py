# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 20}-{limpa}'
s = f'{negrito}{amarelo}{"-+" * 12}-{limpa}'
fim = (f'{negrito}{vermelho}{">>>" * 5} FINALIZADO {"<<<" * 5}{limpa}')
# start
print(borda)
print(f'{" ANALIZANDO NOTAS - DICIONÁRIO ": ^40}')
print(borda)
# receber nome e média aluno e armazenar em dict. retornar conteúdo estruturado
aluno = dict()
aluno['Nome'] = str(input('Nome: ')).capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] > 6.99:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] > 4.99:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(borda)
for k, i in aluno.items():
    print(f'{k:.<15}{amarelo}{i}{limpa}')
print(fim)
