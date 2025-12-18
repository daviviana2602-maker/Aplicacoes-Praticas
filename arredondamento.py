from math import floor, ceil
num = float(input('digite um número real: '))
if num - floor(num) < 0.50:
    print(f'o número arredondado é {floor(num)}')
elif num - floor(num) == 0.50:
    print(f'o número pode ser arredondado para cima ou para baixo, sendo {floor(num)} ou {ceil(num)}')
else:
    print(f'o número arredondado é {ceil(num)}')