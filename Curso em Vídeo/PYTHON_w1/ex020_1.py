# importar biblioteca
import random
# input usuário
alunos = input(
    'Digite o nome dos alunos separados por vírgula (Ex: joão, pedro): ')
if len(alunos) > 7 or alunos.find(',') != -1:
    arr = []
    # tratar string 1
    alunos = alunos.strip()
    comma = alunos.find(',')  # retorna index da string procurada
    # popula arr
    while comma is not -1:
        arr.append(alunos[:comma])
        alunos = alunos[comma + 1:]
        alunos = alunos.strip()
        comma = alunos.find(',')
    arr.append(alunos)
    print(arr)
    # embaralhando o arr - sortei da ordem de apresentação
    random.shuffle(arr)
    for e in range(len(arr)):
        print(f'O {e + 1}º a apresentar é: {arr[e]}')
else:
    print('Na proóxima vez tente digitar nomes com pelo menos 3 caracteres.')
