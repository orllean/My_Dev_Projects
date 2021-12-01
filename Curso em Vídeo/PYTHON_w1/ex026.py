texto = input('Digite uma texto: ').lower()
print(f'A letra [A] aparece {texto.count("a")} no texto\
    \nA 1ª ocorência é na posição: {texto.find("a") + 1}\
    \nE última ocorência é na posição: {texto.rfind("a",) + 1}')
