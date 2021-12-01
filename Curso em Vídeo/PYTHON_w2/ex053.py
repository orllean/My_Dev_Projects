print('{:=^60}'.format(' A FRASE É UM PALÍNDROMO OU NÃO É? '))
print('''
Ex: apos a sopa.
Ex: a sacada da casa.
Ex: a torre da derrota.
Ex: o lobo ama o bolo.
Ex: anotaram a data da maratona.
Todas essa frases podem ser lidas de frente para traz ou de traz para frente
''')
p = str(input(f'Digite uma frase (sem acentuacao): '))
k = p.replace(' ', '')
print(f'[{p}] é um palíndromo: {k == k[::-1]}')
