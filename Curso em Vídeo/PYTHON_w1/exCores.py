# cores no terminal - utilizando código ANSI
# inicia com '\033[' e fecha com 'm'
# aceita 3 argumentos: style(0 = none, 1 = bold, 4 = underline e 7 = inverse) ; text(sequencia de 30 ate 37) ; bg(sqc de 40 ate 47). separados por dois pt e virgula

nome = 'orlean costa'.title()
limpa = '\033[0;0;0m'
txt_fx = {
    'none': '\033[0m',
    'bold': '\033[1m',
    'italic': '\033[4m',
    'inverse': '\033[7m'
}
txt_cores = {'branco': '\033[30m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'amarelo': '\033[33m',
             'azul': '\033[34m',
             'roxo': '\033[35m',
             'cian': '\033[36m',
             'cinza': '\033[37m'
             }
bg_cores = {'branco': '\033[40m',
            'vermelho': '\033[41m',
            'verde': '\033[42m',
            'amarelo': '\033[43m',
            'azul': '\033[44m',
            'roxo': '\033[45m',
            'cian': '\033[46m',
            'cinza': '\033[47m'
            }
print(
    f'Olá! Muito prazer em te conhecer {txt_fx["bold"]}{txt_cores["vermelho"]}{bg_cores["amarelo"]} {nome} {limpa}!!!')
