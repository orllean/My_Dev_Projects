# importar biblioteca
import random
# popular array
arr = []
for a in range(4):
    alunos = input(
        f'Digite o nome do aluno {a + 1}º: ')
    arr.append(alunos)
# sorteio
print(f'O aluno sorteado para foi {arr[random.randint(0, 3)].upper()}')
