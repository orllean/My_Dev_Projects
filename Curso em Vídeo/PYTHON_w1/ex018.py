import math
grau = input('Digite o valor do ângulo: ')

# valida input
if grau.replace('.', '', 1).isnumeric():
    grau = float(grau)
    # valida valor
    if grau > 0:
        print(
            # faz-se nescessário converter o valor dos graus em radianos math.sin(math.radians(grau)
            f'O seno de {grau}° é {math.sin(math.radians(grau)):.2f} rad\
                \nO coseno de {grau}° é {math.cos(math.radians(grau)):.2f} rad\
                \nA tangente de {grau}° é {math.tan(math.radians(grau)):.2f} rad')
    else:
        print('Na próxima vez digite valores maiores que zero')
        exit()
else:
    print('Na próxima vez digite um número ex: 18!')
