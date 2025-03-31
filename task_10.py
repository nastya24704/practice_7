number = float(input())
k = 0
while number > 0:
    number_2 = float(input())
    if number_2 < number:
        k+=1
    number = number_2
print(k-1)
