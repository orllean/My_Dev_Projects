######## Input / Validação #########
try:
    n1 = float(
        input('MACHINE: Humano! Digite a primeiro seu peso(kg)(1/2): '))
    n2 = float(input(
        'MACHINE: Humano! Digite agora sua altura(m)(2/2): '))
except:
    print('MACHINE: Na próxima vez digite apenas números humano burro.')
    exit()
######## get imc #########
n3 = n1 / pow(n2, 2)
######## output #########
if n3 < 18.5:
    print(
        f'MACHINE: Seu IMC é de  [{n3:.1f}]. Você é um humano que está abaixo do peso.')
elif n3 < 25:
    print(
        f'MACHINE: Seu IMC é de  [{n3:.1f}]. Parbéns! Você é um humano que está com o peso ideal.')
elif n3 < 30:
    print(
        f'MACHINE: Seu IMC é de  [{n3:.1f}]. Você é um humano que está com o sobrepeso.')
elif n3 < 40:
    print(
        f'MACHINE: Seu IMC é de  [{n3:.1f}]. Você é um humano que está obeso.')
else:
    print(
        f'MACHINE: Seu IMC é de  [{n3:.1f}]. Meus pêsames! Você é um humano que está com obesidade morbida.')
