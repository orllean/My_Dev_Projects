tot_idade = 0
h_nome = ''
h_idade = 0
m_menor20 = 0
for p in range(1, 5):
    print('{:=^20}'.format(' ' + str(p) + '° ALUNO '))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()
    tot_idade += idade
    if p == 1 and sexo == 'm':
        h_nome = nome
        h_idade = idade
    if sexo == 'm' and h_idade < idade:
        h_nome = nome
        h_idade = idade
    if sexo == 'f' and idade < 20:
        m_menor20 += 1
print(f'A média de idade do grupo é de {(tot_idade / 4)} anos.')
print(f'O homem mais velho se chama {h_nome.capitalize} e tem {h_idade} anos.')
print(f'Ao todo são {m_menor20} mulheres menores de 20 anos.')
