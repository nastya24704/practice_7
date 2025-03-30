n = int(input())
degree= 0
while 2**degree < n:
    degree+=1
if 2**degree == n:
    print('верно')
else:
    print('неверно')
