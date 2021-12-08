# set colors
limpa = '\033[0;0;0m'
negrito = '\033[1m'
vermelho = '\033[31m'
amarelo = '\033[33m'
cinza = '\033[37m'
# initialize variables
borda = f'{negrito}{vermelho}{"-+" * 60}-{limpa}'
# set tupla
clasBras21 = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleza', 'Fluminense', 'América-MG', 'Ceará', 'Internacional',
              'Santos', 'São Paulo', 'Atlético Goianiense', 'Juventude', 'Cuiabá', 'Athletico-PR', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')
# tasks show (1 top 5, 2. last four, 3. list order alphabetize, 4. index Corinthians
# start
print(borda)
print(f'{"  BRASILEIRO 2021  ": ^110}')
print(borda)
print(f'{negrito}{vermelho}top 5:{limpa}{amarelo} {clasBras21[0:5]}')
print(
    f'{negrito}{vermelho}last 4:{limpa}{amarelo} {clasBras21[len(clasBras21)-4:]}')
print(f'{negrito}{vermelho}alphabetize:{limpa}{amarelo} {sorted(clasBras21)}')
# update
clasBras21 = sorted(clasBras21)
print(f'{negrito}{vermelho}index Corinthians:{limpa}{amarelo} {clasBras21.index("Corinthians")}')
