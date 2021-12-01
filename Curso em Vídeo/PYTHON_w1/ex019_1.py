# importar biblioteca
import random
# input usuário
alunos = input(
    'Digite o nome dos alunos separados por vírgula (Ex: joão, pedro): ')
if len(alunos) > 7:
    comma = alunos.find(',')  # retorna int ref a busca
    arr = []
    # tratar string 1
    alunos = alunos.strip()
    while comma is not -1:
        arr.append(alunos[:comma])
        alunos = alunos[comma + 1:]
        alunos = alunos.strip()
        comma = alunos.find(',')
    arr.append(alunos)
    #print(f'O aluno sorteado foi: {arr[random.randint(1,len(arr) - 1)]}')
    print(f'O aluno sorteado foi: {random.choice(arr)}')
else:
    print('Na proóxima vez tente digitar nomes com pelo menos 3 caracteres.')
