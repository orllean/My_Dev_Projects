from typing import List
from lib.dados import *
from time import sleep


path = 'Curso em Vídeo/PYTHON_W3/ex115/lib/dados/'
arq = 'cadastro.txt'


listaMenu = ['Ver pessoas cadastradas',
             'Cadastrar nova pessoa',
             'Sair do sistema'
             ]


cor = ('\033[0;0;0m',       # 0 - limpa
       '\033[33m',          # 1 - amarelo
       '\033[36m',          # 2 - azul
       '\033[1;31;47m'      # 3 - vermehlo
       )


def linha(tamanho=42):
    return '-' * tamanho


def cabeça(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1
    for l in lista:
        print(f'{cor[1]}{c} - {cor[2]}{l}{cor[0]} ')
        c += 1
    print(linha())


def éInt(i):
    try:
        i = int(i)
    except (ValueError, TypeError):
        print(f'{cor[3]} ERRO! Apenas valores numéricos. {cor[0]}')
    except (KeyboardInterrupt):
        print(f'{cor[3]} ERRO! Valor não informado. {cor[0]}')
    else:
        return i


def opt_1():
    arquivo = arqLer(path, arq)
    if arquivo:
        for a in arquivo:
            dado = a.split(';')
            print(f'{dado[0].title():.<20}{dado[1][:-1]:>3} anos')
    else:
        print(f'{cor[3]}ERRO! Não foi possível visualizar o cadastro.{cor[0]}')


def opt_2():
    nome = str(input('Nome: '))
    while True:
        idade = éInt(str(input('Idade: ')))
        if idade:
            break
    cad = arqCadastro(path, arq, nome, idade)
    if cad:
        print(
            f'{cor[2]}Cadastro de [{nome.upper()}] realizado com sucesso.{cor[0]}')
    else:
        print(f'{cor[3]}ERRO! Não foi possível realizar o cadastro.{cor[0]}')


def opção(lista):
    opt = éInt(str(input(f'{cor[1]}Sua opção:{cor[0]} ')))
    if opt:
        if opt > len(lista):
            print(f'{cor[3]} ERRO! Digite uma opção válida. {cor[0]}')
        elif opt == 1:
            cabeça(lista[0])
            opt_1()
        elif opt == 2:
            cabeça(lista[1])
            opt_2()
        elif opt == 3:
            cabeça(f'{lista[2]}... Até logo!')
            return True


def bd():
    existe = arqExiste(path, arq)
    if not existe:
        criar = arqCriar(path, arq)
        return criar
    else:
        return existe


def principal():
    if bd():
        while True:
            cabeça('Menu Principal')
            menu(listaMenu)
            resposta = opção(listaMenu)
            if resposta:
                break
            sleep(2)
    else:
        print(
            f'{cor[3]} ERRO! Arquivo de dados não encontrado e impossível de ser criado. :({cor[0]} ')
