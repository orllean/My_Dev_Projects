from random import choice
n1 = input('1º aluno: ')
n2 = input('2º aluno: ')
n3 = input('3º aluno: ')
n4 = input('4º aluno: ')
lista = [n1, n2, n3, n4]
print(f'O aluno sorteado foi: {choice(lista)}')