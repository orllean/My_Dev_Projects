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
    # sortei da ordem de apresentação
    arr_random = []
    while len(arr) != len(arr_random):
        r = random.randint(0, len(arr)-1)
        if arr[r] not in arr_random:
            arr_random.append(arr[r])
    for e in range(len(arr)):
        print(f'O {e + 1}º a apresentar é: {arr_random[e]}')
else:
    print('Na proóxima vez tente digitar nomes com pelo menos 3 caracteres.')
