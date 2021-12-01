# variaveis
cad = []
campo = ['o nome', 'a idade', 'o sexo']
bo_cad = True
# inicio loop cadastro
while bo_cad == True:
    # loop por aluno
    print('{:=^20}'.format(' CADASTRO '))
    aluno = []
    for j in range(3):
        # loop por campos
        aluno.append(str(input(f'Digite {campo[j]}: ')))
        cad.append(aluno)
    print(
        '''Digite:
        [ 0 ] Encerrar cadastro.
        [ 1 ] Novo cadastro.''', end='')
    cnt_cad = input(': ')
    bo_cad = True if cnt_cad == '1' else False
# media de idade do grupo
m_idade = 0
for e in cad:
    m_idade += int(e[1])
print(f'A média de idade do grupo é de {m_idade / len(cad)} anos.')
# homen mais velho
h_velho = 0
x = 0
for e in range(len(cad)):
    if cad[e][2] == 'm' and int(cad[e][1]) > h_velho:
        h_velho = int(cad[e][1])
        x = e
        # valida homem mais velho
        if h_velho != 0:
            print(
                f'O homen de mais velho é {cad[x][0].capitalize()}, com {cad[x][1]} anos.')
# qtd mulheres < 20 anos
t_mulher = 0
for e in range(len(cad)):
    if cad[e][2] == 'f' and int(cad[e][1]) < 20:
        t_mulher += 1
        # valida mulher menor de 20 anos
    if t_mulher != 0:
        print(
            f'O total de mulheres com menos de 20 anos é {t_mulher}.')
