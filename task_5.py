n = int(input())
volume = []
a = 1
while a*a*a < n:
    volume.append(a*a*a)
    a+=1
print(' '.join(map(str, volume)))
