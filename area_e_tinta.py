ap = float(input('qual é a altura da parede em metros? '))
lp = float(input('qual é a largura da parede em metros?'))
área = ap * lp / 2
print(f' a área da parede é de {área:.2f}m²')
print(f'a quantia de tinta necessária para pintar esta parede é de {área / 2:.2f} litros de tinta, considerando que cada litro pinta 2m²')