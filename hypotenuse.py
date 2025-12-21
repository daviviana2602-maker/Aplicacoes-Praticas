from math import sqrt
c1 = float(input('enter first cathetus value: '))
c2 = float(input('enter second cathetus value: '))
hypotenuse_squared = (c1 **2 + c2 ** 2)
hypotenuse = sqrt(hypotenuse_squared)
print(f'the hypotenuse is: {hypotenuse:.2f}')