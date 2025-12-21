from math import floor
number = float(input('enter a number: '))
if number - floor(number) == 0.5:
   print('the number can be rounded up or down, ')
else:
    rounded_number = round(number)
    print(f'the rounded number is: {rounded_number}') 