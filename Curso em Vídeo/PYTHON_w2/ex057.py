s = True
while s:
    q = str(input('Digite o sexo [M/F]: ')).lower()
    s = False if q in 'mf' else True
