import math
number = float(input())
while (math.sqrt(number))**2 % number > 0:
    print('введите другое число')
    number = float(input())
print('число', number, 'является полным квадратом')
